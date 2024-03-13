-- Script that creates a database and a table
-- Query to create database hbtn_0d_usa
-- Query to create table states if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
