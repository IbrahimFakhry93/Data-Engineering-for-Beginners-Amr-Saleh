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

--! 35. Union and Union ALL




--*=====================================================================================

--! 36 Aggregation

--* Used alot in report writing, data analysis and data engineering
--* تجميع داتا


--*=====================================================================================

--! 37 Window Functions

--* let's say we have 3 departments in a company, and every department there are 10 employees with 10 salaries
--* req: sort salaries for each department apart