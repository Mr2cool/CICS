from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import ibm_db
import os
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

app = FastAPI(
    title="Retirement API with DB2",
    description="API for retirement data from DB2 with TRP",
    version="3.0.0"
)

# --- Authentication Setup ---
SECRET_KEY = "your-secret-key"  # In production, use a strong, securely stored key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Dummy User Database ---
dummy_users_db = {
    "testuser": {
        "username": "testuser",
        "full_name": "Test User",
        "email": "testuser@example.com",
        "hashed_password": pwd_context.hash("testpassword"),
        "disabled": False,
    }
}

# Model for Retirement Data
class RetirementData(BaseModel):
    employee_id: int
    name: str
    age: int
    retirement_date: str
    trp: float  # Total Retirement Portfolio

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# --- DB2 Connection Details ---
# Set these as environment variables or replace with your actual DB2 credentials
DB2_HOST = os.getenv("DB2_HOST", "your-db2-host")
DB2_PORT = os.getenv("DB2_PORT", "50000")
DB2_DBNAME = os.getenv("DB2_DBNAME", "your-db")
DB2_USER = os.getenv("DB2_USER", "your-user")
DB2_PASSWORD = os.getenv("DB2_PASSWORD", "your-password")

def get_db2_conn():
    """Establishes a connection to the DB2 database."""
    conn_str = (
        f"DATABASE={DB2_DBNAME};"
        f"HOSTNAME={DB2_HOST};"
        f"PORT={DB2_PORT};"
        f"PROTOCOL=TCPIP;"
        f"UID={DB2_USER};"
        f"PWD={DB2_PASSWORD};"
    )
    try:
        conn = ibm_db.connect(conn_str, "", "")
        return conn
    except Exception as e:
        # In a real app, you'd want to log this error.
        raise HTTPException(status_code=500, detail=f"DB2 Connection failed: {str(e)}")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(dummy_users_db, form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/retirement/{employee_id}", response_model=RetirementData, summary="Get retirement data by employee ID from DB2")
def get_retirement_data(employee_id: int, token: str = Depends(oauth2_scheme)):
    """
    Get retirement data for a specific employee by their ID from the DB2 database.
    Requires authentication.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(dummy_users_db, token_data.username)
    if user is None:
        raise credentials_exception

    conn = get_db2_conn()
    # Note: Using f-strings for SQL queries is unsafe and vulnerable to SQL injection.
    # Use parameterized queries instead for production code.
    sql = f"SELECT EMPLOYEE_ID, NAME, AGE, RETIREMENT_DATE, TRP FROM RETIREMENT WHERE EMPLOYEE_ID = {employee_id}"
    
    try:
        stmt = ibm_db.exec_immediate(conn, sql)
        result = ibm_db.fetch_assoc(stmt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query failed: {str(e)}")
    finally:
        ibm_db.close(conn)
        
    if not result:
        raise HTTPException(status_code=404, detail=f"Employee with ID {employee_id} not found")
    
    # The DB2 driver returns keys in uppercase. We need to map them to our Pydantic model fields.
    return RetirementData(
        employee_id=result['EMPLOYEE_ID'],
        name=result['NAME'],
        age=result['AGE'],
        retirement_date=str(result['RETIREMENT_DATE']),
        trp=result['TRP']
    )
