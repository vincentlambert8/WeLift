CREATE DATABASE welift;
USE welift;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS Trips;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS Destination_pictures;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Comments;

CREATE TABLE Users(id int AUTO_INCREMENT, email varchar(254) NOT NULL, password varchar(254) NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(50) NOT NULL, gender enum('Male', 'Female', 'Other') NOT NULL, birthdate char(10), region varchar(50), phone varchar(25) NOT NULL, balance float, primary key (id));


CREATE TABLE Cars(license varchar(25), id_driver int, brand varchar(25), model varchar(25), capacity integer NOT NULL, year integer, color varchar(25), primary key (license));


CREATE TABLE Trips(id int AUTO_INCREMENT, date timestamp DEFAULT CURRENT_TIMESTAMP, departure varchar(50) NOT NULL, destination varchar(50) NOT NULL, distance float, seats_available integer, stopover integer, id_driver int, id_passengers varchar(2592), price float, license varchar(25), primary key (id), foreign key (license) references Cars(license), foreign key (id_driver) references Users(id));
CREATE INDEX locationIndex USING BTREE ON Trips(departure, destination, date);
CREATE INDEX idIndex USING HASH ON Trips(id);
CREATE INDEX driverIndex USING HASH ON Trips(id_driver);


CREATE TABLE Destination_pictures(destination varchar(30), picture varchar(100), primary key (destination));
CREATE INDEX destinationIndex USING HASH ON Destination_pictures(destination);



CREATE TABLE Transactions(id int AUTO_INCREMENT, id_transmitter int, id_recipient int, amount float, date timestamp, primary key (id), foreign key (id_transmitter) references Users(id), foreign key (id_recipient) references Trips(id_driver));

CREATE TABLE Comments(id int AUTO_INCREMENT, message varchar(300), score int, id_passenger int, id_driver int, primary key (id), foreign key (id_passenger) references Users(id), foreign key (id_driver) references Trips(id_driver));
CREATE INDEX idIndex USING HASH ON Comments(id_driver);


INSERT INTO Users VALUES (NULL, 'lamby@ulaval.ca', MD5('lamby'), 'Vincent', 'Lambert', 'Male', '1998-01-01', 'Québec', '(418) 507-0000', 150);
INSERT INTO Users VALUES (NULL, 'yuk@ulaval.ca', MD5('yuk'), 'Yuxuan', 'Zhao', 'Male', '1998-01-01', 'Québec', '(418) 507-0000', 250);
INSERT INTO Users VALUES (NULL, 'jean@ulaval.ca', MD5('jean'), 'JC', 'Drouin', 'Male', '1998-01-01', 'Québec', '(418) 507-0421', 50);
INSERT INTO Users VALUES (NULL, 'claude@ulaval.ca', MD5('claude'), 'claude', 'Drouin', 'Male', '1997-01-01', 'Saguenay', '(418) 523-8542', 20);
INSERT INTO Users VALUES (NULL, 'roland@ulaval.ca', MD5('roland'), 'roland', 'charest', 'Male', '1980-10-02', 'Montréal', '(418) 507-1234', 100);
INSERT INTO Users VALUES (NULL, 'robert@ulaval.ca', MD5('robert'), 'Robert', 'Lavoie', 'Male', '1998-01-01', 'Mauricie', '(418) 645-0530', 503);
INSERT INTO Users VALUES (NULL, 'jacques@ulaval.ca', MD5('jacques'), 'Jacques', 'Christophe', 'Male', '1995-03-12', 'Gaspésie', '(418) 507-0000', 27);
INSERT INTO Users VALUES (NULL, 'damien@ulaval.ca', MD5('damien'), 'Damien', 'Ferland', 'Male', '1970-01-11', 'Montréal','(418) 505-0021' , 59);
INSERT INTO Users VALUES (NULL, 'james@ulaval.ca', MD5('james'), 'James', 'Bouchard', 'Male', '1950-10-10', 'Québec', '(418) 222-0200', 74);
INSERT INTO Users VALUES (NULL, 'joe@ulaval.ca', MD5('joe'), 'Joe', 'Joe', 'Male', '1998-01-01', 'Québec', '(418) 507-0000', 52);
INSERT INTO Users VALUES (NULL, 'jeanne@ulaval.ca', MD5('jeanne'), 'Jeanne', 'Lacroix', 'Female', '1979-01-10','Saguenay' , '(418) 536-3223', 52);
INSERT INTO Users VALUES (NULL, 'catherine@ulaval.ca', MD5('catherine'), 'Catherine', 'Jean', 'Female', '1944-01-01', 'Québec','(418) 514-4234' , 52);
INSERT INTO Users VALUES (NULL, 'roxanne@ulaval.ca', MD5('roxanne'), 'Roxanne', 'Dorval', 'Female', '1998-12-12', 'St-Tite','(418) 512-5433' , 52);
INSERT INTO Users VALUES (NULL, 'celine@ulaval.ca', MD5('celine'), 'Celine', 'Dion', 'Female', '1970-02-12', 'Québec', '(418) 534-2534', 52);

INSERT INTO Cars VALUES ("AAA AAA", 1, "Toyota", "yaris", 4, 2000, "black");
INSERT INTO Cars VALUES ("BBB BBB", 2, "Mazda", "3", 4, 2005, "black");
INSERT INTO Cars VALUES ("CCC CCC", 4, "Tesla", "X", 4, 2018, "Green");
INSERT INTO Cars VALUES ("DDD DDD", 6, "Honda", "Civic", 4, 1999, "White");
INSERT INTO Cars VALUES ("EEE EEE", 7, "Volvo", "p250", 4, 2009, "black");


INSERT INTO Trips VALUES (NULL, "2020-05-05 08:00:00", 'Saguenay', 'Quebec', 150, 4, 2, 5, "/1/2/3", 90, "AAA AAA" );
INSERT INTO Trips VALUES (NULL, "2020-06-20 08:00:00", 'Montréal', 'Saguenay', 300, 3, 0, 10, "/1/5/3", 120, "BBB BBB" );
INSERT INTO Trips VALUES (NULL, "2020-07-10 08:00:00", 'Saguenay', 'Quebec', 150, 6, 1, 8, "/1/2/3/5", 30, "CCC CCC" );
INSERT INTO Trips VALUES (NULL, "2020-05-14 08:00:00", 'St-Tite', 'Trois-Rivières', 200, 2, 2, 9, "/2/3", 150, "DDD DDD" );






INSERT INTO Destination_pictures VALUES ('default', '../../static/images/welift.jpg');
INSERT INTO Destination_pictures VALUES ('gaspesie', '../../static/images/gaspesie.jpg');
INSERT INTO Destination_pictures VALUES ('gatineau', '../../static/images/gatineau.jpg');
INSERT INTO Destination_pictures VALUES ('montreal', '../../static/images/montreal.jpg');
INSERT INTO Destination_pictures VALUES ('riviere-du-loup', '../../static/images/riviere-du-loup.jpg');
INSERT INTO Destination_pictures VALUES ('st-tite', '../../static/images/st-tite.jpg');
INSERT INTO Destination_pictures VALUES ('trois-riviere', '../../static/images/trois-rivieres.jpg');


DELIMITER //
CREATE TRIGGER negativeBalance
BEFORE INSERT ON Users
FOR EACH ROW
BEGIN
    IF NEW.balance < 0
    THEN SET NEW.balance = 0;
    END IF;
END//
DELIMITER ;
