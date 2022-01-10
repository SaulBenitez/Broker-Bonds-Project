# Bonds REST API project 

## Description

The current project is a demo broker for selling and buying bonds. For this, only registered and authenticated users can create orders to sell bonds. In the same way, those users can buy bonds that have not been bought or are put in sale order by the buyer user. 

## Aims
The particular aims for the current project are:
- Develop an API:
  - Incorporate user authentication.
  - Limit the calls rate to 1000 calls/min.
- Integrate external APIs.
- Model the problem.
- Handle errors.
- Employ Git tool.
- Document the project.
- Incorporate unit tests.
- Create a container in Docker.

## Problem considerations

### Problem requirments

Sell orders:

- The user can publish one or more bonds for sale. 
- The published item includes the following:
  - Unique identification number (id) for each publication.
  - Name of the bond (unique): string with a minimum of 3 and maximum of 40 alphanumeric chars.
  - Number of bonds for sale: integer in the range of [1, 10,000].
  - Selling price of the total number of bonds for sale: monetary value in the range of [0.0000, 100,000,000.0000] with four decimal resulution.
  - The selling price is represented in Mexican Pesos (MXN).
  - The API respond with an error when any consideration is not acomplished.

Buy orders:
- The user is able to list:
  - The published items and buy them.
  - The published items in mexican pesos (MXN) and US dollars (USD) based on Banxico exchage rates.
  - Its buy and sell orders.
  - Its completed sell orders.
- When a published item has been bought:
  - The API indacates an error as invalid operation.
- The system must assign a unique id based on the buyer id
- The API respond with an error when any consideration is not acomplished.

Users:
- The registered users must be unique
- The sell and buy operations, only registered users can complete them.

### Problem modeling

Based on the requirements the problem is modeled with two models:

- User
  - id
  - email
  - username
  - fullname
  - password 

- Bonds
  - id
  - bond_name
  - bond_no
  - bond_price
  - seller
  - buyer

Now for user operations the next endpoints have been created:

- [Register](http://127.0.0.1:8000/api/users/resgister/)
- [Login](http://127.0.0.1:8000/api/users/login/)
- [Refresh token](http://127.0.0.1:8000/api/users/login/refresh/)
- [User list](http://127.0.0.1:8000/api/users/list/)
- [User details](http://127.0.0.1:8000/api/users/1/)
- [List own user bonds](http://127.0.0.1:8000/api/bonds/user/own/)
- [List own user bonds for sale](http://127.0.0.1:8000/api/bonds/user/sale/)
- [List bought user bonds](http://127.0.0.1:8000/api/bonds/user/buy/)
- [Create a new sell order](http://127.0.0.1:8000/api/bonds/create/)
- [List sell orders](http://127.0.0.1:8000/api/bonds/sale/) (in MXN currency)
- [List sell orders](http://127.0.0.1:8000/api/bonds/sale/usd/) (in USD currency)
- [Make a buy order](http://127.0.0.1:8000/api/bonds/buy/1)
- [Dollar value](http://127.0.0.1:8000/api/bonds/sale/usdinfo)

For more information about endpoints, refer to [Local Documentation](http://localhost:8000/swagger/)


## Instructions

- Create and activate the virtual environment
    ```
    virtualenv env
    env\Scripts\activate
    ```
  
- Install python dependencies:
    ```
    pip install -r requirements.txt
    ```

- Change to the project folder broker
    ```
    cd broker
    ```

- Run django project
    ```
    python manage.py migrate
    python manage.py runserver
    ```

## Accomplishments

- [x] Develop an API:
  - [x] Incorporate user authentication.
  - [x] Limit the calls rate to 1000 calls/min.
- [x] Integrate external APIs.
- [x] Model the problem.
- [x] Handle errors.
- [x] Employ Git tool.
- [x] Document the project.
- [ ] Incorporate unit tests.
- [ ] Create a container in Docker.