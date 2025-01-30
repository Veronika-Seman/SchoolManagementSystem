README – School Management System (3-Layer Architecture)

This project was developed in Python and is structured according to a 3-layer architecture:

Data Layer
This layer is responsible for managing all data-related operations, including storage, retrieval, and maintaining connections to the database. Its main goal is to handle direct communication with the database.

Logic Layer
The Logic Layer receives data from the Data Layer and delivers it to the User Interface Layer in a format suitable for user interaction. It can also process or validate data before sending it back to the Data Layer for storage or updates.

User Interface (UI) Layer
The UI Layer handles all interaction with the end user. It communicates only with the Logic Layer and never directly with the Data Layer.

Each layer has a specific role and a strict communication flow:

The Data Layer can only communicate with the Logic Layer.
The UI Layer can only communicate with the Logic Layer.
No direct communication is allowed between the Data Layer and the UI Layer.
Running the Project
Below are the steps required to set up and run the system. Make sure you follow each step in order.

Step 1: Connect to the Database
Install the mysql-connector-python package
If you don’t have the MySQL connector package, install it via:

Copy
Edit
pip install mysql-connector-python
Establish connection

Go to the file: /pyFinalProject/data_access/sqlConnect.py.
Change the password to your own MySQL password in this file.
Run the method create_new_database(). This will create a new database.
Then run the method get_connection() which creates a connection to your MySQL database and returns the connection object.
Step 2: Build the Tables
The file /pyFinalProject 5/data_access/init_db.py contains methods for creating each table if it does not already exist.
Once you run the file, it automatically calls the method create_all_tabels, which triggers all the individual table-creation methods in the file.
This process sets up all the necessary tables in the database.
Step 3: Loading Dummy Data
Navigate to the data folder, where you’ll insert dummy records into the tables.
This folder contains JSON files, each holding data for a specific table, and also includes a file called load_data.py. Within load_data.py, you will find code snippets (enclosed in """) for inserting the JSON data into the tables.
For each table, set the correct file_path for the respective JSON file, remove the enclosing """ from the code snippet you want to run, execute it, then add the """ back afterward. (It is important to restore the """ after each run.)
Perform this process for all tables except the students and parents tables—just update their file_path and run the file named creat_data.py.
Step 4: Run the User Interface
After you have successfully completed steps 1–4 without errors, you can run the user interface.
The user interface is launched from /pyFinalProject 5/presentation/main.p (located in /pyFinalProject 5/presentation).
Execute this file. This starts the UI, allowing you to log in to the system and perform various operations depending on each user’s role.
Log in by providing an email and password corresponding to an existing user in the system.
Following these steps should allow you to set up and use the School Management System according to the 3-layer architecture requirements. Good luck and enjoy the project!