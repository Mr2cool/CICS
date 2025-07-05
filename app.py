from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Retirement API",
    description="API for dummy retirement data with TRP",
    version="1.0.0"
)

# Model for Retirement Data
class RetirementData(BaseModel):
    employee_id: int
    name: str
    age: int
    retirement_date: str
    trp: float  # Total Retirement Portfolio

@app.get("/retirement/api1", response_model=RetirementData, summary="Get dummy retirement data 1")
def get_retirement_api1():
    """
    Get dummy retirement data for API 1
    """
    return RetirementData(
        employee_id=101,
        name="Alice Smith",
        age=59,
        retirement_date="2030-08-15",
        trp=950000.0
    )

@app.get("/retirement/api2", response_model=RetirementData, summary="Get dummy retirement data 2")
def get_retirement_api2():
    """
    Get dummy retirement data for API 2
    """
    return RetirementData(
        employee_id=202,
        name="Bob Johnson",
        age=62,
        retirement_date="2027-05-01",
        trp=1200000.0
    )
