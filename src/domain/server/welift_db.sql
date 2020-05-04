CREATE DATABASE welift;
USE welift;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS Trips;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS Historique;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Comments;

CREATE TABLE Users(id int AUTO_INCREMENT, email varchar(254) NOT NULL, password varchar(254) NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(50) NOT NULL, gender enum('Male', 'Female', 'Other') NOT NULL, birthdate char(10), country varchar(50), phone varchar(25) NOT NULL, balance float, primary key (id));
CREATE INDEX emailIndex USING HASH ON Users(email);

CREATE TABLE Cars(license varchar(25), brand varchar(25), model varchar(25), year integer, color varchar(25), primary key (license));

CREATE TABLE Trips(id int AUTO_INCREMENT, date timestamp NOT NULL, departure varchar(50) NOT NULL, destination varchar(50) NOT NULL, distance float, capacity integer NOT NULL, stopover integer, id_driver int, id_passengers varchar(2592), price float, license varchar(25), primary key (id), foreign key (license) references Cars(license));
CREATE INDEX tripIndex USING HASH ON Trips(departure, destination);

CREATE TABLE Historique(id int AUTO_INCREMENT, id_trips int, primary key (id), foreign key (id) references Users(id));

CREATE TABLE Transactions(id int AUTO_INCREMENT, id_transmitter int, id_recipient int, amount float, date timestamp, primary key (id));

CREATE TABLE Comments(id int AUTO_INCREMENT, message varchar(300), score float, id_passenger int, id_driver int, primary key (id));
CREATE INDEX idIndex USING HASH ON Comments(id_driver);