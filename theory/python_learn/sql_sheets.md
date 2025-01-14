------------------------------------------------------------------------------------------------------------
SHEET 1 
------------------------------------------------------------------------------------------------------------


CREATE TABLE Employee (
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

INSERT INTO Employee (Name, Age, Department, Salary) VALUES
    ('Ramesh', 20, 'Finance', 0000.00),
    ('Deep', 25, 'Sales', 30000.00),
    ('Suresh', 22, 'Finance', 50000.00),
    ('Ram', 28, 'Finance', 20000.00),
    ('Pradeep', 22, 'Sales', 20000.00);
    
    

 
 
 SELECT 
    Name, 
    Age, 
    Department, 
    Salary,
    Avg_Salary
FROM (
    SELECT 
        Name, 
        Age, 
        Department, 
        Salary,
        AVG(Salary) OVER (PARTITION BY Department) AS Avg_Salary,
        ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS salary_rank
    FROM 
        employee
) ranked_employee
WHERE 
    salary_rank <= 2;





 SELECT 
        Name,
        Age,
        Department,
        Salary,
        ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS salary_rank
    FROM 
        employee;
        
        
SELECT 
    Name,
    Age,
    Department,
    Salary,
    ROW_NUMBER() OVER (PARTITION BY Department, Age ORDER BY Salary DESC) AS salary_rank
FROM 
    employee;

 


------------------------------------------------------------------------------------------------------------
SHEET 2 
------------------------------------------------------------------------------------------------------------






CREATE TABLE Employee (
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

INSERT INTO Employee (Name, Age, Department, Salary) VALUES
    ('Ramesh', 20, 'Finance', 0000.00),
    ('Deep', 25, 'Sales', 30000.00),
    ('Suresh', 22, 'Finance', 50000.00),
    ('Ram', 28, 'Finance', 20000.00),
    ('Pradeep', 22, 'Sales', 20000.00);
    
    

 
 
 SELECT 
    Name, 
    Age, 
    Department, 
    Salary,
    Avg_Salary
FROM (
    SELECT 
        Name, 
        Age, 
        Department, 
        Salary,
        AVG(Salary) OVER (PARTITION BY Department) AS Avg_Salary,
        ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS salary_rank
    FROM 
        employee
) ranked_employee
WHERE 
    salary_rank <= 2;





 SELECT 
        Name,
        Age,
        Department,
        Salary,
        ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS salary_rank
    FROM 
        employee;
        
        
SELECT 
    Name,
    Age,
    Department,
    Salary,
    ROW_NUMBER() OVER (PARTITION BY Department, Age ORDER BY Salary DESC) AS salary_rank
FROM 
    employee;

 

 SHEET - 3


 CREATE TABLE Employee (
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);
INSERT INTO Employee (Name, Age, Department, Salary) VALUES
    ('Sunny', 20, 'Finance',90000.00),
    ('Sonu', 25, 'Sales', 50000.00),
    ('Yashi', 22, 'Finance', 70000.00),
    ('Ram', 28, 'Finance', 20000.00),
    ('Pradeep', 22, 'Sales', 20000.00),
    ('Sp', 22, 'Finance', 70000.00),
    ('Aju', 28, 'Finance', 2000.00),
    ('Pradeep', 22, 'Sales', 20000.00);
 

SELECT 
    Name,
    Age,
    Department,
    Salary,
    ROW_NUMBER() OVER(PARTITION BY department order by salary desc) as rn,
	LAG(Salary, 1, 0) OVER(PARTITION BY department order by salary desc) as prev_sal,
    LEAD(Salary,1,0) OVER(PARTITION BY department order by salary desc) as next_sal,
    FIRST_VALUE(Name) OVER(PARTITION BY department order by salary desc) as first_val,
    LAST_VALUE(Name) OVER(PARTITION BY department order by salary desc RANGE BETWEEN unbounded preceding and unbounded following) as last_val,
    ntile(3) OVER(PARTITION by department order by salary desc) as bucket
FROM 
    employee;



SHEET - 4



CREATE TABLE Employee (
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);
INSERT INTO Employee (Name, Age, Department, Salary) VALUES
    ('Sunny', 20, 'Finance',90000.00),
    ('Sonu', 25, 'Sales', 50000.00),
    ('Yashi', 22, 'Finance', 70000.00),
    ('Ram', 28, 'Finance', 20000.00),
    ('Pradeep', 22, 'Sales', 20000.00),
    ('Sp', 22, 'Finance', 70000.00),
    ('Aju', 28, 'Finance', 2000.00),
    ('Pradeep', 22, 'Sales', 20000.00);
 
SELECT Name,bucket, 
CASE when x.bucket=1 then 'High'
	when x.bucket=2 then 'Mid'
	when x.bucket=3 then 'Low' END done
from (
SELECT 
    Name,
    Age,
    Department,
    Salary,
    ntile(3) OVER(PARTITION by department order by salary desc) as bucket
FROM 
    employee 
) x;
