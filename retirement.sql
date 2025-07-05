-- Sample DB2 DDL and dummy data for the 'retirement' table

CREATE TABLE retirement (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    retirement_date DATE,
    trp DECIMAL(15,2)
);

INSERT INTO retirement (employee_id, name, age, retirement_date, trp) VALUES
    (101, 'Alice Smith', 59, '2030-08-15', 950000.00),
    (202, 'Bob Johnson', 62, '2027-05-01', 1200000.00),
    (303, 'Cathy Brown', 58, '2032-11-30', 850000.00),
    (404, 'David Lee', 60, '2029-03-20', 1000000.00);
