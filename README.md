# Tax Receipt Calculator



Calculator to generate a reciept based on item type.


## Features

- Backend based on FastApi
- Mysql for datastorage
- Item type analyser based on diflibb Python
- Frontend based on Vue js
- Data Type checking
- Data Migrations using Alembic


## Problem being tackled
Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical
products that are exempt. Import duty is an additional sales tax
applicable on all imported goods at a rate of 5%, with no exemptions. When I purchase items
I receive a receipt which lists the name of all the items and their price (including tax),
finishing with the total cost of the items,
and the total amounts of sales taxes paid. The rounding rules for sales tax are that for a tax
rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of
sales tax.


## WorkFlow

Frontend is used to work with the backend. Data can be entered in the text bar on the main page.
To add each item after type add button needs to be pressed which puts the item in the list.
After list is completed generate button can be pressed to generate the reciept.
Frontend does the initial data cleaning and makes a request to the backend to know the type of item.
The response returns item type which is used to create another object which is again passed to the backend with item details. Backend then responds with the tax and sales tax calculation.
After all items have been processed this way a receipt is generated including all the prices and items.


## Tech

This project uses number of open source projects to work properly:

- [FastApi] - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [MySql] - MySQL is a relational database management system (RDBMS) developed by Oracle that is based on structured query language (SQL). 
- [Alembic] - Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python. 
- [DOCKER] - Docker.
- [Vue Js] - Vue.js is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications.


## Installation
This project is based on Python 3.8.
To create a virtual environment following steps can be followed:
```sh
python3 -m venv <youeENVname>
```
To activate conda environment:
```sh
source <yourENVnam>/bin/activate
```
Install the required packages and libraries:

```sh
pip3 install -r requirements.txt
```

Copy .env.example to .env and set the environment variables accordingly.


- DB_DATA_PATH - This is the path to mount the database data to, to persist it on your local machine
It can either be a path /some/folder or just a string like db-data

Environment Variables

This project requires MySQL server to run on localhost.
If local server is not available the said can be run on docker by running the following:

```sh
docker-compose up -d
```


## Starting up

Change .env.example to .env

Start script creates database and table in the mySql server and then the server is initiated
```sh
python3 start.py
```

## Running Frontend
This project requires running frontend to work with the backend.
NPM is required to start and install the required packages for the project. 

To install all the dependencies please run the following:
```sh
npm install
```

to inititate the project for testing purposes:
```sh
npm run serve
```

## Tests
Tests can be performed for the backend by running the following command:
```sh
 coverage run --branch -m pytest tests
```

## Deloyement
Backend can be deloyed on the docker but its advised to be run on the env.

## Difflibb for Item type analysis

This package is used to analyse and know the item similarity from a list of food, medical and books. If the item doesnt match any of the above tpye "other" is returned.



[//]: # 

   [FastApi]: <hhttps://fastapi.tiangolo.com>
   [MySql]: <https://www.mysql.com/de>
   [Alembic]: <https://alembic.sqlalchemy.org/en/latest/>
   [DOCKER]: <https://www.docker.com>
   [Vue Js]: <https://vuejs.org>
   