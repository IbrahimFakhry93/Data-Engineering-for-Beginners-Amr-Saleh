
-- ^ look up the slides very important
CREATE TABLE hr.departments (
    departmentID int,
    name varchar(20),
    managerId int
);


SELECT * FROM hr.departments;

INSERT INTO hr.departments (departmentid, "name", managerid) 
VALUES (1, 'Engineering', 12);

INSERT INTO hr.departments (departmentid, "name", managerid) 
VALUES (2, 'Design', 4);

INSERT INTO hr.departments (departmentid, "name", managerid) 
VALUES (3, 'Marketing', 2);

--! Delete table data
--* delete from hr.departments where departmentid = 3;

SELECT * FROM hr.departments;

--! Delete table itself (Delete table structure)
drop table departments ;

--* show which schema we are on now:
SHOW search_path;


--^ Arithmetic

select departmentid, name,managerid, managerid+10 from hr.departments;


--^ Adding Column Alias

select departmentid, name,managerid, managerid+10 as new_manager_id from hr.departments;


--^ Concatenation: merge two columns

select departmentid || ' ' || name as department, managerid from hr.departments

SELECT * FROM hr.departments;

--^ Duplicates:

insert into hr.departments (departmentid,name,managerid) values (4,'other',13);
insert into hr.departments (departmentid,name,managerid) values (5,'other',14);
insert into hr.departments (departmentid,name,managerid) values (6,'other',15);

SELECT * FROM hr.departments;



--^ Distinct with columns: remove duplicates

select distinct name from departments
SELECT name FROM hr.departments;

--^ Distinct with select * (all rows)
select distinct * from departments;
--! it won't remove the duplicates, because * will work on row level where there are different values and no duplication
SELECT * FROM hr.departments;
--!  distinct here won't remove the duplicates, because it works on full duplicates rows not only single field


--^ Null

insert into hr.departments(departmentid,name,managerid) values(10," ",1);
insert into hr.departments(departmentid,name,managerid) values(11,"",2);
insert into hr.departments(departmentid,name,managerid) values(12,NULL,NULL);

--^ null doesn't work with (=) operator
--^ null and (is) clause
select * from hr.departments where name is null;

--^ NULL and or operator
select * from hr.departments where name is null or managerid is null;

--^ Exclude NULL
select * from hr.departments where name is not null;

--^ Replace NULL: use coalesce(col name,"replaced value")

select departmentid,coalesce(name,"NO Dept") as name_not_null, managerid from hr.departments;

--^ replace null but for numeric value as manager_id
select departmentid,coalesce(name,"NO Dept") as name_not_null, coalesce(manager_id,0) from hr.departments

--^ note:
--* instead of coalesce in postgres, in my sql there is: nvl(name,"NO dept")

--*=====================================================================================
-- ^ look up the slides very important
--! filtering: 30. Employees Where conditions

select employeeid,firstname,lastname,birthdate,notes from employees

--^ filtering using where clause

select employeeid,firstname,lastname from employees where employeeid =1

select employeeid,firstname,lastname from employees where employeeid < 5

select employeeid,firstname,lastname from employees where employeeid <= 5

--~ between include 3 and 5: continuos range
--^ Used when you want to filter rows within a continuous range of values.
select employeeid,firstname,lastname from employees where employeeid between 3 and 5

--~ in: set of numbers
--^ Used when you want to filter rows that match specific, discrete values (not necessarily continuous).
select employeeid,firstname,lastname from employees where employeeid in (1,3,7,9)


--*=====================================================================================

--! 31. Conditions and Sorting
-- ^ look up the slides very important

--^ wildcard: like + "_" or "%"

--* '_': single character
--* '%': multi characters or even no characters

select employeeid,firstname,lastname from employees where firstname like'n%';

select employeeid,firstname,lastname from employees where firstname like'an_r%';


--^ Multiple Conditions

--~ or operator:
select employeeid,firstname,lastname from employees where firstname like'n%' or firstname like 'a%';

--~ where not (attr or attr)

select employeeid,firstname,lastname from employees where not (employeeid = 3 or employeeid = 4);

--^ sorting: order by clause
--* sort order by default: asc
select employeeid,firstname,lastname from employees order by firstname asc;

select employeeid,firstname,lastname from employees order by firstname desc;

--*=====================================================================================
--! 32 Joins

-- ^ look up the slides very important
--*=====================================================================================
--! 33. Hands -on SQL Joins

--* Alter - add department id to employees table
ALTER TABLE employees ADD COLUMN Departmentid INT;

--* Update
UPDATE employees SET Departmentid = 1 WHERE employeeid BETWEEN 1 AND 4;
UPDATE employees SET Departmentid = 2 WHERE employeeid BETWEEN 5 AND 8;
UPDATE employees SET Departmentid = 4 WHERE employeeid BETWEEN 9 AND 12;

SELECT * FROM employees e;
SELECT * FROM departments d;

--* Join

SELECT e.employeeid,
       e.firstname,
       e.departmentid AS Emp_tbl_dept_id,
       d.departmentName,
       d.departmentid
FROM employees e
left JOIN departments d
  ON e.departmentid = d.departmentid
ORDER BY employeeid ASC;

--* In industry, left join is more commonly used

--! Exercise

--^ Req: list all employees that their departments already exist in the company

--~ first method: (join): more efficient regarding performance

SELECT e.firstname || ' ' || e.lastname AS employeeName, d."name" AS departName
FROM employees e, departments d
  WHERE d.departmentid = e.department_id;

--~ or (same but different syntax)
SELECT e.firstname || ' ' || e.lastname AS employeeName, d."name" AS departName
FROM employees e
INNER JOIN departments d
  ON d.departmentid = e.department_id;


--*============================================================================

--! 34. SubQuery
-- ^ look up the slides very important
select * from departments d ;
select * from employees e ;

--^ Req: list all employees that their departments already exist in the company

--~ Second method, subquery: more complex and less efficient

--* start by writing inner query
--* outer query will execute after inner query

--* use (in) when inner query return multi-values
select * from employees where departmentid in (select department_id from departments)

--* use (=) when inner query return single value
select * from employees where departmentid = (select department_id from departments = 1)

--~ same requirement but we need to display department name

SELECT e.firstname || ' ' || e.lastname AS fullname,
       (SELECT d."name"
        FROM departments d
        WHERE d.departmentid = e.department_id) AS departName
FROM employees e
WHERE e.department_id IN (SELECT departmentid FROM departments);

--*============================================================================

--! 35. Union and Union ALL
-- ^ look up the slides very important
--TODO : List all possible names in the table whether are first name or last name

--! interview:

--^ Union: remove duplicates, so it's slower
--~ example: if first name and lastname have same values
select firstname as Name from employees
union 
select lastname as Name from employees;

--^ Union all: doesn't remove duplicates
select firstname as Name from employees
union all
select lastname as Name from employees;

--*=====================================================================================

--! 36 Aggregation
-- ^ look up the slides very important
--* Used a lot in report writing, data analysis and data engineering
--* تجميع داتا

select * from orders;

--^ How many orders:

--* count(orderid): exclude null values
SELECT COUNT(orderid) FROM orders;  

--* count(*): include null values
SELECT COUNT(*) FROM orders;  

--^ How many items got sold
SELECT SUM(quantity) FROM order_details od; --* 12743

SELECT ROUND(AVG(quantity), 2) FROM order_details;

--^ min / max quantities
SELECT MIN(quantity), MAX(quantity) FROM order_details;

SELECT * FROM order_details;

--^ Build a report to show the number of items sold (quantity) for each order.
select orderid , sum(quantity) as items_sold_per_order from order_details;

--*=====================================================================================

--! Coding Exercise 1: Top 5 employees by number of orders

select * from orders;

select e.firstname as emp_firstname,e.lastname as emp_lastname, count(o.orderid ) as no_orders from employees e ,orders o
where e.employeeid =o.employeeid  group by e.employeeid  order by no_orders  desc limit 5;

--*=====================================================================================

--! 37 Window Functions

--* window: to use subset of data 

-- ^ look up the slides very important
--! interview: types of window functions, most common in interview: Rank()/Dense_Rank

--* use cases: sort student rank for each school classes apart (ranking)


--? Example:
select * from products p;
--* products table: productname, supplier_id,categoryid,unit,price

--^ req: sort the products according to their prices (desc) per each category apart
--* هاتلى ترتيب المنتجات من اعلى سعر لاقل سعر لكل كاتورجي

select productname,categoryid,price ,rank() over(partition by categoryid order by price desc) as price_rank from products;  


--TODO : ranking
--* let's say we have 3 departments in a company, and every department there are 10 employees with 10 salaries
--! req: sort employees according to their salaries for each department apart

select e.firstname as emp_name, e.department_id, e.salary , rank() over(partition by e.department_id order by e.salary desc) as salary_rank from employees e


--^ to display department name, we use join

select e.firstname as emp_name, d."name" as depart_name, e.salary , 
rank() over(partition by e.department_id order by e.salary desc) as salary_rank from employees e inner join departments d on e.department_id =d.departmentid 



--^ lead or lag: (ask chatgpt)

--* to get for example the immediate student precedes a certain student
--* or to get the employee whose salary is immediate higher than a certain employee 

--^ Rank (ask chatgpt): skip the ranks when data is duplicated (ex. different products have same price)

--*=====================================================================================
--! 38 CTE

--* it's like virtual table which has result set, it's given a name
--* improves readability 

--~ CTE Method: (more readable)
--^  create temporary result set of customer and their orders dates before 30 days
with recent_orders as ( select customerid, orderdate from orders o where o.orderdate < current_date - interval '30 days') 
select customerid , count(*) as order_count from recent_orders group by customerid;

--~ subquery Method: (same result above but, less readable)

select customerid , count(*) as order_count from ( select customerid, orderdate from orders o where o.orderdate < current_date - interval '30 days') as recent_orders group by customerid;

--*=====================================================================================
--! 39. SQL Indexing:
--* index is like فهرس

--* too many indexes can hurt performance and increase storage
--*=====================================================================================


--!  40. SQL Performance Tuning