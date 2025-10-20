#
#! 11. Relational VS Non-Relational Databases (NoSQL)

# ? Relational Databases (RDBMS)
# * Data stored in structured tables (rows & columns).
# * Relationships enforced using Primary Keys and Foreign Keys.
# * Each table has a predefined schema → strict structure.
# * Schema is imposed at the time of writing data → "Schema on Write".
# * Example: Cannot insert a "Price" column unless it exists in the schema.
# * Very common: ~95% of databases you’ll encounter as a Data Engineer are relational.
# * Examples: MySQL, PostgreSQL, Oracle, SQL Server.

# ? Non-Relational Databases (NoSQL)
# * Data stored without a fixed schema (flexible / semi-structured / unstructured).
# * Can handle diverse data types: JSON, documents, key-value pairs, graphs, multimedia (video, audio, etc.).
# * Schema is applied only when reading data → "Schema on Read".
# * When querying, you must know/expect the structure of the data (e.g., field names).
# * Examples: MongoDB (document), Cassandra (wide-column), Redis (key-value), Neo4j (graph).

# ? Key Difference
# * Relational DB → Schema on Write (strict, structured, validated before insert).
# * Non-Relational DB → Schema on Read (flexible, validated when retrieved).

# *================================================================================================

#! 12. ACID Properties


# *================================================================================

#! 13. CAP Theorem (Brewer)
# & CAP Theorem in Distributed Systems

# ? Definition
# * CAP Theorem applies to any distributed system (including databases).
# * When data is partitioned across multiple servers, if one server goes down or network partitions occur,
# * the system must choose between Consistency and Availability (Partition Tolerance is always required).

# ? Key Concepts
# * Consistency → (System is always up) Every read receives the most recent write (all nodes show the same data).
# * Availability → Every request receives a response, even if some nodes are down (may not be the latest data).
# * Partition Tolerance → System continues to operate despite network failures or server partitions.

# ? Trade-offs
# * You cannot guarantee all three (C, A, P) simultaneously in a distributed system.
# * Must choose between Consistency and Availability when partitions happen.

# ? Use Cases
# ^ Consistency is critical for:
# *   - Banking transactions
# *   - Tax closure systems for government officials
# ^ Availability is preferred for:
# *   - Duolingo (NoSQL DB: Amazon Dynamo DB) → better to show slightly stale scores than crash the app
# *   - Real-time feeds (social media, news) → user experience > strict consistency

#! Why Duolingo use Amazon Dynamo DB as NO SQL DBMS?
# * Because Amazon Dynamo DB provides very high throughput with low latency

# ^ choosing availability means we choose (Eventual Consistency)

# ? Summary
# * CAP Theorem = Consistency vs Availability under Partition Tolerance.
# ^ Choice depends on business requirements:
# *   - Financial systems → Consistency first
# *   - User-facing apps → Availability first

# *=================================================================

#! 15. Types of Non-Relational Databases (MongoDB, Cassandra, DynamoDB)
# * Table in sql == collections in no sql
# * row in sql == document in no sql

# ^ watch lecture video

# *=================================================================

#! 16. Introduction to Entity Relationship Diagram and Data Modelling

# * Entity is a table


# *================================================

# ? primary key:
# * It's the (unique identifier column) of a row in a table


# ? Foreign Key:
# * it creates relation between two table
# *================================================

#! 18. Normalization and 3rd Normal Form

# * Normalization is very important topic in interviews


# *===============================================

#! 20. Real-world challenge, which DB to choose? (Advanced Topic)

# ^ open: Credit Card Transaction.pdf
# ^ check copilot conversation
# https://copilot.microsoft.com/shares/u4GR5ZYiiefiyK2Vdk2LE

# ^ check Article
# https://thenewstack.io/can-nosql-databases-be-acid-compliant/
