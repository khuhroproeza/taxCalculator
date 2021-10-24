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


## Installation amd Starting Up
This project can be run directly oon Docker.
Please follow the following instructions:
build docker-compose file
and then run 

to Build:
```sh
docker-compose build
```
To Run:
```sh
docker-compose up 
```

## Tests
Tests can be performed for the backend by running the following command in the backend directory:
```sh
 coverage run --branch -m pytest tests
```


## Difflibb for Item type analysis

This package is used to analyse and know the item similarity from a list of food, medical and books. If the item doesnt match any of the above tpye "other" is returned.



[//]: # 

   [FastApi]: <hhttps://fastapi.tiangolo.com>
   [MySql]: <https://www.mysql.com/de>
   [Alembic]: <https://alembic.sqlalchemy.org/en/latest/>
   [DOCKER]: <https://www.docker.com>
   [Vue Js]: <https://vuejs.org>
   
