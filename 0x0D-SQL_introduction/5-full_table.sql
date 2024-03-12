-- Script: 5-full_table.sql
-- Description: Prints the full description of the table first_table

SELECT *
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
