
1. **Connecting to a MySQL Database**
   ```sql
   mysql -u username -p
   ```
   This command is used to connect to a MySQL database. The `-u` option specifies the username, and `-p` prompts for the password.

2. **Creating a Database**
   ```sql
   CREATE DATABASE database_name;
   ```
   This command is used to create a new database.

3. **Selecting a Database**
   ```sql
   USE database_name;
   ```
   This command is used to select a specific database to work with.

4. **Creating a Table**
   ```sql
   CREATE TABLE table_name (
       column1_name column1_datatype,
       column2_name column2_datatype,
       ...
   );
   ```
   This command is used to create a new table in the database.

5. **Inserting Data into a Table**
   ```sql
   INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
   ```
   This command is used to insert data into a table.

6. **Selecting Data from a Table**
   ```sql
   SELECT * FROM table_name;
   ```
   This command is used to select and display all data from a table.

7. **Updating Data in a Table**
   ```sql
   UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
   ```
   This command is used to update existing data in a table.

8. **Deleting Data from a Table**
   ```sql
   DELETE FROM table_name WHERE condition;
   ```
   This command is used to delete data from a table.

9. **Finding Specific Data (WHERE Clause)**
   ```sql
   SELECT * FROM table_name WHERE condition;
   ```
   This command is used to select data that matches a specific condition.

10. **Joining Tables**
    ```sql
    SELECT columns FROM table1
    INNER JOIN table2 ON table1.column_name = table2.column_name;
    ```
    This command is used to join two tables based on a related column.

11. **Creating Indexes**
    ```sql
    CREATE INDEX index_name ON table_name (column_name);
    ```
    This command is used to create an index on a table column to improve search performance.

12. **Altering a Table Structure**
    ```sql
    ALTER TABLE table_name ADD column_name datatype;
    ```
    This command is used to modify the structure of an existing table, such as adding a new column.

13. **Dropping a Table**
    ```sql
    DROP TABLE table_name;
    ```
    This command is used to delete a table and its data.

14. **Dropping a Database**
    ```sql
    DROP DATABASE database_name;
    ```
    This command is used to delete a database.

15. **Exiting MySQL Command Line**
    ```sql
    exit
    ```
    