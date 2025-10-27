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

SELECT name FROM hr.departments;

--! Delete table itself

--* drop table hr.departments ;


--^ Distinct: remove duplicates

select distinct * from hr.departments

--!  distinct here won't remove the duplicates, because it works on full duplicates rows not only single field


--^ Null

insert into hr.departments(departmentid,name,managerid) values(10," ",1);
insert into hr.departments(departmentid,name,managerid) values(11,"",2);
insert into hr.departments(departmentid,name,managerid) values(12,NULL,NULL);

--^ null and (is) clause
select * from hr.departments where name is null;

--^ NULL and or operator
select * from hr.departments where name is null or managerid is null;

--^ Exclude NULL
select * from hr.departments where name is not null;

--^ Replace NULL

select departmentid,coalesce(name,"NO Dept") as name_not_null, managerid from hr.departments

--^ note:
--* instead of coalesce in postgres, in my sql there is: nvl(name,"NO dept")

--*=====================================================================================

--! filtering: 30. Employees Where conditions

select employeeid,firstname,lastname,birthdate,notes from employees

--^ filtering using where clause

select employeeid,firstname,lastname from employees where employeeid =1

select employeeid,firstname,lastname from employees where employeeid < 5

select employeeid,firstname,lastname from employees where employeeid <= 5

--~ between include 3 and 5
select employeeid,firstname,lastname from employees where employeeid between 3 and 5

--~ in certain range
select employeeid,firstname,lastname from employees where employeeid in (1,3,7,9)


--*=====================================================================================

--! 31. Conditions and Sorting

--^ wildcard:

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

--! Exercise

--^ Req: list all employess that their departments already exist in the company

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

select * from departments d ;
select * from employees e ;

--* start by writing inner query
--* outer query will execute after inner query

--* use (in) when inner query return mulit-values
select * from employees where departmentid in (select department_id from departments)

--* use (=) when inner query return single value
select * from employees where departmentid = (select department_id from departments = 1)


--^ Req: list all employess that their departments already exist in the company

--~ Second method, subquery: more complex ad less efficient

SELECT e.firstname || ' ' || e.lastname AS fullname,
       (SELECT d."name"
        FROM departments d
        WHERE d.departmentid = e.department_id) AS departName
FROM employees e
WHERE e.department_id IN (SELECT departmentid FROM departments);

--*============================================================================

--! 35. Union and Union ALL

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

--* Used alot in report writing, data analysis and data engineering
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
select orderid , sum(quantity) as items_sold_per_order from order_detai

--*=====================================================================================

--! 37 Window Functions

--* let's say we have 3 departments in a company, and every department there are 10 employees with 10 salaries
--* req: sort salaries for each department apart