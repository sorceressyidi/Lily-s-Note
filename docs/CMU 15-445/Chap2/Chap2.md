## Pre-Knoledge

Reference to https://runoob.com/sql/sql-update.html

### Fundamentals

#### SQL SELECT

```sql
SELECT column1, column2, ...
	FROM table_name;
SELECT column1, column2, ...
	FROM table_name;
SELECT DISTINCT column1, column2, ...
	FROM table_name;

```

#### SQL WHERE

```sql
SELECT column1, column2, ...
	FROM table_name WHERE condition;
SELECT column1, column2, ...
	FROM table_name
	ORDER BY column1, column2, ... ASC|DESC;
```

#### SQL INSERT

* id 列是自动更新的，表中的每条记录都有一个唯一的数字。

```sql
INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);
```

#### SQL Update

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

![3](3.png)

#### SQL DELETE

```sql
DELETE FROM table_name WHERE condition;
DELETE FROM table_name;
```

## Aggregations + Group By

#### Aggregations

![2](2.png)

![1](1.png)

* Aggregate functions can (almost) only be used in

  the **SELECT** output list.

* COUNT, SUM, AVGsupport DISTINCT

```sql
SELECT COUNT(DISTINCT login)
	FROM student WHERE login LIKE "%@cs"
```

* Multiple Aggregates

```sql
SELECT AVG(gpq),COUNT(sid)
	FROM student WHERE login LIKE '%@cs'
```

* Output of other columns outside of an aggregate is

  undefined.

Cause ERROR

```sql
SELECT AVG(s.gpa), e.cid
	FROM enrolled AS e JOIN student AS s
		ON e.sid = s.sid
```

* To fix it -- Group By

#### Group By

```sql
SELECT AVG(s.gpa), e.cid
	FROM enrolled AS e JOIN student AS s
		ON e.sid = s.sid
	GROUP BY e.cid
```

#### Having

![4](4.png)

* We cannot use **Aggregations** to FILTER tuples because we have not computed it yet

![5](5.png)

## String / Date / Time Operations

![6](6.png)

### String Operations

#### LIKE

* LIKE is used for string matching.

* String-matching operators
	>`%` matches any sequence of characters, including zero characters. 
	In other words, `%` can match any string of any length, including an empty string. 
	* For example, `'15%'` matches any string starting with "15", `'%15'` matches any string ending with "15", and `'%15%'` matches any string containing "15" anywhere.

```sql
SELECT * FROM enrolled AS e
	WHERE e.cid LIKE '15-%'
```

> `_` matches any single character. 
> It's used to specify that at a particular position, any character must match, but it doesn't matter which character. For example, `'15_'` matches "150", "151", "152", etc., but not "15" etc.
```sql
SELECT * FROM student AS s
	WHERE s.login LIKE '%@c_'
```
#### SUBSTRING
```sql
SELECT SUBSTRING(name,1,5) AS abbrv_name
	FROM student WHERE sid = 53688
```
#### UPPER

```sql
SELECT * FROM student AS s
	WHERE UPPER(s.name) LIKE 'KAN%'
```

#### `||`
* SQL standard says to use ||operator to concatenate two or more strings together.

`SQL-92`
```sql
SELECT name FROM student
	WHERE login = LOWER(name) || '@cs'
```

`MSSQL`
```sql
SELECT name FROM student
	WHERE login = LOWER(name) + '@cs'
```

`MySQL`
```sql
SELECT name FROM student
	WHERE login = CONCAT(LOWER(name), '@cs')
```

* Also like `'Li''ly'`  will automatically concatenate

### Date/Time Operations
![7](7.png)

## Output Control + Redirection
Store query results in another table:
→ Table must not already be defined.
→ Table will have the same # of columns with the same types as the input.
## Nested Queries

## Common Table Expressions

## Window Functions
