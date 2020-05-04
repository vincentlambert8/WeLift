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

CREATE TABLE Trips(id int AUTO_INCREMENT, date timestamp NOT NULL, departure varchar(50) NOT NULL, destination varchar(50) NOT NULL, distance float, capacity integer NOT NULL, stopover integer, id_driver int, id_passengers varchar(2592), price float, license varchar(25), primary key (id), foreign key (license) references Cars(license));
CREATE INDEX tripIndex USING HASH ON Trips(departure, destination);

INSERT INTO Trips VALUES (NULL, "2020-06-01 13:15:00", "quebec", "st-tite", NULL, 4, 1, NULL, NULL, 30.00, NULL);
INSERT INTO Trips VALUES (NULL, "2020-05-23 09:00:00", "montreal", "st-tite", NULL, 4, 1, NULL, NULL, 27.50, NULL);
INSERT INTO Trips VALUES (NULL, "2020-05-10 13:00:00", "trois-riviere", "gaspesie", NULL, 4, 1, NULL, NULL, 50.50, NULL);
INSERT INTO Trips VALUES (NULL, "2020-05-07 12:30:00", "quebec", "gatineau", NULL, 4, 1, NULL, NULL, 40.00, NULL);
INSERT INTO Trips VALUES (NULL, "2020-05-09 11:10:00", "montreal", "riviere-du-loup", NULL, 4, 1, NULL, NULL, 35.75, NULL);
INSERT INTO Trips VALUES (NULL, "2020-05-07 08:45:00", "st-tite", "trois-riviere", NULL, 4, 1, NULL, NULL, 25.50, NULL);


CREATE TABLE Cars(license varchar(25), brand varchar(25), model varchar(25), year integer, color varchar(25), primary key (license));

CREATE TABLE Historique(id int AUTO_INCREMENT, id_trips int, primary key (id), foreign key (id) references Users(id));

CREATE TABLE Transactions(id int AUTO_INCREMENT, id_transmitter int, id_recipient int, amount float, date timestamp, primary key (id));

CREATE TABLE Comments(id int AUTO_INCREMENT, message varchar(300), score float, id_passenger int, id_driver int, primary key (id));
CREATE INDEX idIndex USING HASH ON Comments(id_driver);