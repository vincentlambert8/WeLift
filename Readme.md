# WeLift

As part of this project, we decided to create a carpooling application that will be used by travelers across Quebec to get around in a simple and ecological way.

### Requirements

##### 1. MySQL

- The project relies on **MySQL Server** as our database. Go ahead, and install it first from [this page](https://dev.mysql.com/downloads/installer/).

- Add a MySQL Server instance in the installer. Follow the instructions.

- Once the database is set up, open the MySQL Commend Line Client. It can be found from the system search bar. You will be asked to create an account.

- Copy paste the sql code from [here](src/domain/server/welift_db.sql).

- Create a file in [this directory](src/domain/server) called ```db.yaml``` and insert these information. The **mysql_password** is the one you configure previously.

  ```
  mysql_host: 'localhost'
  mysql_user: 'root'
  mysql_password: 'mypassword'
  mysql_db: 'welift'
  ```

##### 2. Install the project's libraries with the following command:

```
$ pip install -r requirements.txt
```

### Usage

1. Make sure you are using the virtual environment.

2. Run the program by opening the command line in the project's ```src``` directory and enter the following command:

   ```
   $ py app.py
   ```

3. Go to [this site](http://localhost:5000/home) and enjoy!