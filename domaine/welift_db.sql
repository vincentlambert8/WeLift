CREATE DATABASE welift;
USE welift;
CREATE TABLE Users(id char(36), email varchar(254), password char(32), first_name varchar(50), last_name varchar(50), gender enum('Male', 'Female', 'Other'), birthdate char(10), country varchar(50), phone varchar(25), balance float, primary key (id));
CREATE TABLE Trips(id char(36), date timestamp, departure varchar(50), destination varchar(50), distance float, capacity integer, stopover , id_driver char(36), id_passengers varchar(2592), primary key (id), foreign key (id_driver) references Users(id));
CREATE TABLE Cars(id char(36), license varchar(25), brand varchar(25), model varchar(25), year integer, color varchar(25), primary key (id));
CREATE TABLE History(id char(36), id_trips varchar(3600), primary key (id), foreign key (id) references Users(id));
CREATE TABLE Transactions(id char(36), id_transmitter char(36), id_recipient char(36), amount float, date timestamp, primary key (id));
CREATE TABLE Comments(id char(36), message varchar(300), score float, id_transmitter char(36), id_recipient char(36), primary key (id));
 
