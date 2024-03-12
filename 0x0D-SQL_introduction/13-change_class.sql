-- Script: 13-remove_low_scores.sql
-- Description: Removes all records with a score <= 5 in the table second_table

DELETE FROM second_table
WHERE score <= 5;
