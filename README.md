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

- [Register](http://127.0.0.1:8000/api/users/register/), to create a new instance of user in the data base.
- [Login](http://127.0.0.1:8000/api/users/login/), to get the token authorization as registered user.
- [Refresh token](http://127.0.0.1:8000/api/users/login/refresh/), to refresh the token authorization if this 
- [User list](http://127.0.0.1:8000/api/users/list/), to list all registered users (only superuser can access)
- [User details](http://127.0.0.1:8000/api/users/1/), to edit, delete, or list a specific user (for now only superuser can access).
- [List own user bonds](http://127.0.0.1:8000/api/bonds/user/own/), to list the bonds that the logged user bought or create for sale.
- [List own user bonds for sale](http://127.0.0.1:8000/api/bonds/user/sale/), to list the bonds that logged user create for sale.
- [List bought user bonds](http://127.0.0.1:8000/api/bonds/user/buy/), to list the bonds that the logged user bought.
- [Create a new sell order](http://127.0.0.1:8000/api/bonds/create/), to create a new bond for sale.
- [List sell orders](http://127.0.0.1:8000/api/bonds/sale/) (in MXN currency), to list sell orders published by users, except by logged user.
- [List sell orders (USD)](http://127.0.0.1:8000/api/bonds/sale/usd/) (in USD currency), to list sell orders published by users, except by logged user in USD.
- [Make a buy order](http://127.0.0.1:8000/api/bonds/buy/1), to buy bonds.
- [Dollar value](http://127.0.0.1:8000/api/bonds/sale/usdinfo), to retrieve the dollar exchange information.

For more information about endpoints, refer to [Local Documentation](http://localhost:8000/swagger/)

## Usage instructions

- Create and activate the virtual environment:
    ```
    virtualenv env
    env\Scripts\activate
    ```
  Notice that the above activation of virtual environment is given for Windows OS.

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

- Test the API endpoints opening the [Local Documentation](http://localhost:8000/swagger/).
  
- Create two or more users in the Section Users in /users/register/
  ```
  - {
      "email": "cristian@example.com",
      "fullname": "Cristian",
      "username": "cristian",
      "password": "1234"
    }
    
  - {
      "email": "paulina@example.com",
      "fullname": "Paulina",
      "username": "paulina",
      "password": "1234"
    }
  - {
      "email": "pedro@example.com",
      "fullname": "Pedro",
      "username": "pedro",
      "password": "1234"
    }
  - {
      "email": "laura@example.com",
      "fullname": "Laura",
      "username": "laura",
      "password": "1234"
    }
  ```
- Login with a user account in Section users in /users/login/:
  ```
  - {
      "email": "cristian@example.com",
      "password": "1234"
    }
  - {
      "email": "paulina@example.com",
      "password": "1234"
    }
  - {
      "email": "pedro@example.com",
      "password": "1234"
    }
  - {
      "email": "laura@example.com",
      "password": "1234"
    }
  ```

- Copy the access key and get authorization.
  - Click on the "Authorize" button  
  - Write in the box:
  - Bearer <access key>
  - Click on authorize and close the pop-up box.
  - The user authorization is gotten.

- Create the next sell orders in Section bonds in /bonds/create/ with two different accounts:
  ```
  - {
      "bond_name": "cash",
      "bond_price": "1000",
      "bond_no": "10"
    }
  - {
      "bond_name": "money",
      "bond_price": "500",
      "bond_no": "100"
    }
  - {
      "bond_name": "gold",
      "bond_price": "500",
      "bond_no": "100"
    }
  - {
      "bond_name": "silver",
      "bond_price": "8000",
      "bond_no": "1000"
    }
  ```

  Notice, those sell orders accomplish the problem requirements.

- Try create the next bonds:
  - Creation of a sell order with a repeated name
    ```
    - {
        "bond_name": "money",
        "bond_price": "500",
        "bond_no": "100"
      }
    ```
  - Creation of a sell order with problem requirements violations:
    ```
    - {
        "bond_name": "mo",
        "bond_price": "0",
        "bond_no": "0"
      }
    - {
        "bond_name": "money money money money money money money money",
        "bond_price": "100000001.0000",
        "bond_no": "10001"
      }
    ```  
- List sell orders in Section Bonds in /bonds/sale/. The list only displays sell orders of different users than the logged user. Also, the bonds than have already been bought were not displayed. In a similar way, in in Section Bonds in /bonds/sale/usd, it is displayed the same list but in USD currency.

- Buy the desired bond introducing the id of bond. Only the logged user can buy other user bonds and those have not been bought yet.

- List user bonds:
  - Bonds that user already sell in Section Bonds in /bonds/user/sale/
  - Bonds that user bought in Section Bonds in /bonds/user/buy/
  - Bonds of user (bought and in sell bonds) in Section Bonds in /bonds/user/own/


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