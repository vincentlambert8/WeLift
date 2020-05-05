CREATE DATABASE welift;
USE welift;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS Trips;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS Destination_pictures;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Comments;

CREATE TABLE Users(id int AUTO_INCREMENT, email varchar(254) NOT NULL, password varchar(254) NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(50) NOT NULL, gender enum('Male', 'Female', 'Other') NOT NULL, birthdate char(10), country varchar(50), phone varchar(25) NOT NULL, balance float, primary key (id));
CREATE TRIGGER negativeBalande BEFORE INSERT ON Users FOR EACH ROW IF NEW.balance < 0 THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Montant invalide'; END IF; END


CREATE TABLE Cars(license varchar(25), id_driver int, brand varchar(25), model varchar(25), capacity integer NOT NULL, year integer, color varchar(25), primary key (license));


CREATE TABLE Trips(id int AUTO_INCREMENT, date timestamp DEFAULT CURRENT_TIMESTAMP, departure varchar(50) NOT NULL, destination varchar(50) NOT NULL, distance float, seats_available integer, stopover integer, id_driver int, id_passengers varchar(2592), price float, license varchar(25), primary key (id), foreign key (license) references Cars(license), foreign key (id_driver) references Users(id));
CREATE INDEX locationIndex USING BTREE ON Trips(departure, destination, date);
CREATE INDEX idIndex USING HASH ON Trips(id);
CREATE INDEX driverIndex USING HASH ON Trips(id_driver);


CREATE TABLE Destination_pictures(destination varchar(30), picture varchar(100), primary key (destination), foreign key (destination) references Trips(destination));
CREATE INDEX destinationIndex USING HASH ON Destination_pictures(destination)
INSERT INTO Destination_pictures VALUES ('default', '../../static/images/welift.jpg');
INSERT INTO Destination_pictures VALUES ('gaspesie', '../../static/images/gaspesie.jpg');
INSERT INTO Destination_pictures VALUES ('gatineau', '../../static/images/gatineau.jpg');
INSERT INTO Destination_pictures VALUES ('montreal', '../../static/images/montreal.jpg');
INSERT INTO Destination_pictures VALUES ('riviere-du-loup', '../../static/images/riviere-du-loup.jpg');
INSERT INTO Destination_pictures VALUES ('st-tite', '../../static/images/st-tite.jpg');
INSERT INTO Destination_pictures VALUES ('trois-riviere', '../../static/images/trois-rivieres.jpg');



CREATE TABLE Transactions(id int AUTO_INCREMENT, id_transmitter int, id_recipient int, amount float, date timestamp, primary key (id), foreign key (id_transmitter) references Users(id), foreign key (id_recipient) references Trips(id_driver));

CREATE TABLE Comments(id int AUTO_INCREMENT, message varchar(300), score int, id_passenger int, id_driver int, primary key (id), foreign key (id_passenger) references Users(id), foreign key (id_driver) references Trips(id_driver));
CREATE INDEX idIndex USING HASH ON Comments(id_driver);



INSERT INTO Users VALUES (NULL, 'lamby@ulaval.ca', MD5('12345'), 'Vincent', 'Lambert', 'Male', '1998-01-01', '(418) 507-0000', 'Canada', 50);
INSERT INTO Users VALUES (NULL, 'yuk@ulaval.ca', MD5('12345'), 'Yuxuan', 'Zhao', 'Male', '1998-01-01', '(418) 507-0000', 'Canada', 50);
INSERT INTO Users VALUES (NULL, 'jc@ulaval.ca', MD5('12345'), 'JC', 'Drouin', 'Male', '1998-01-01', '(418) 507-0000', 'Canada', 50);


INSERT INTO Comments (id, message, score, id_passenger, id_driver) VALUES (NULL, 'Mon criss', 5, 3, 1);
INSERT INTO Comments (id, message, score, id_passenger, id_driver) VALUES (NULL, 'Mon beau', 1, 2, 1);

