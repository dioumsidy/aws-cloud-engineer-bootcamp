\# Week 3 — SQL and AWS Databases



This week focuses on relational databases, SQL, database security, and Amazon RDS.



\## Topics Covered



\- Relational databases

\- Tables, rows, and columns

\- Primary keys

\- Foreign keys

\- SELECT

\- WHERE

\- INSERT

\- UPDATE

\- DELETE

\- ORDER BY

\- GROUP BY

\- Aggregate functions

\- INNER JOIN

\- LEFT JOIN

\- Database users

\- Database permissions

\- GRANT

\- Least privilege

\- MariaDB

\- Amazon RDS

\- Database networking

\- TLS-secured database connections



\## SQL Lab



I created a `cloud\_company` database and practiced working with engineers, customers, and orders.



Example query:



```sql

SELECT c.name, SUM(o.price) AS total\_spent

FROM customers c

JOIN orders o

ON c.customer\_id = o.customer\_id

GROUP BY c.customer\_id, c.name

ORDER BY total\_spent DESC;

