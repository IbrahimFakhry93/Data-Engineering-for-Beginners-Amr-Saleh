CREATE TABLE departments (
    departmentID int,
    name varchar(20),
    managerId int
);


SELECT * FROM departments;

INSERT INTO departments (departmentid, "name", managerid) 
VALUES (1, 'Engineering', 12);

INSERT INTO departments (departmentid, "name", managerid) 
VALUES (2, 'Design', 4);

INSERT INTO departments (departmentid, "name", managerid) 
VALUES (3, 'Marketing', 2);

--delete from hr.departments where departmentid = 3;

SELECT * FROM departments;

SHOW search_path;





-- Arithmetic

select departmentid, name,managerid, managerid+10 from hr.departments;


-- Adding Column Alias

select departmentid, name,managerid, managerid+10 as new_manager_id from hr.departments;


-- Concatenation: merge two columns

select departmentid || ' ' || name as department, managerid from hr.departments

SELECT * FROM departments;

-- Duplicates:

insert into departments (departmentid,name,managerid) values (4,'other',13);
insert into departments (departmentid,name,managerid) values (5,'other',14);
insert into departments (departmentid,name,managerid) values (6,'other',15);

--SELECT * FROM departments;

SELECT name FROM departments;
--drop table departments ;


-- Distinct: remove duplicates

select distinct name from departments


-- NULL

insert into departments(departmentid,name,managerid) values(10,' ',1);
insert into departments(departmentid,name,managerid) values(11,'',2);
insert into departments(departmentid,name,managerid) values(12,NULL,NULL);


select * from departments where name is null;

-- NULL and or operator
select * from departments where name is null or managerid is null;

-- Exclude NUL (filter)L
select * from departments where name is not null;

-- Replace NULL

select departmentid,coalesce(name,'NO Dept') as name_not_null, managerid from departments


select departmentid,coalesce(name,'NO Dept') as name_not_null, coalesce(managerid ,0) as manager_not_null from departments