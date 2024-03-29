-- Script: 1-create_user.sql
-- Description: Query to create user_0d_1 if it does not exist
-- Query to grant all privileges to user_0d_1

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
