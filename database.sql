-- Create the database
CREATE DATABASE FaceRecognitionDB;

-- Use the database
USE FaceRecognitionDB;

-- Create the table to store user data
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    address VARCHAR(255)
);

