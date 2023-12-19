# Job-Description-Generator
## Overview
This repository contains scripts that leverage OpenAI's GPT-3.5 model and a MySQL database connection to generate job descriptions. This script will automates the process of generating Job Description using the OpenAI API and stores the results in a MySQL database. These scripts offer various functionalities, including job description generation, database connectivity, and a Flask-based web service for easy access.


## Files

### 1. main.py
Description: This file contains the core functionality for generating job descriptions.

Dependencies:
- langchain
- pymysql
- json
- logging
- re
- db_connection

### 2. db_connection.py
Description: Manages the database connection and execution of SQL queries.

Dependencies:
- pymysql
- json

### 3. config.json
Description: Configuration file containing database server details and OpenAI API key.

#### Example Configuration:

                
    {
    "database": {
        "server": "localhost",
        "database_name": "your_database_name",
        "username": "your_username",
        "password": "your_password"
    },
    "OpenAI": {
        "key": "your_OpenAI_API_key"
    }
    }


### 4. app.py
Description: Implements a Flask-based web service for generating job descriptions via HTTP requests.

Dependencies:
- Flask
- langchain
- pymysql
- json
- logging
- re
- db_connection

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

## Setup Instructions:
#### Environment Setup:

Ensure Python is installed (preferably Python 3.x).
Install necessary dependencies using the command:

 `pip install -r requirements.txt.`

#### Database Configuration:
Update the `config.json` file with your specific database server details, including server address, database name, username, password and Api Key.

#### Running the Application:
Execute python file `app.py` to start the Flask-based web service for job description generation.

## Usage

#### main.py Usage:
Import JobDescriptionGenerator from `main.py`.
Initialize the JobDescriptionGenerator class with the path to the `config.json` file.
Call the generated_job_description() method to generate job descriptions.

#### Database Connection (db_connection.py):
Import the DatabaseConnection class from `db_connection.py`.
Instantiate DatabaseConnection to establish and manage database connections.

#### Web Service (app.py):
Run the Flask application `app.py` to create an endpoint (/test) for generating job descriptions via HTTP GET requests.


## Notes

1. Ensure proper setup of dependencies and correct configurations in config.json before executing the scripts.
2. Protect sensitive information such as API keys and database credentials.
