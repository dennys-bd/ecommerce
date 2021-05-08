# ecommerce

Ecommerce service/api to save favorite products of clients

## Runing

1. Create .env file from .env.example and fill the missing variables `cp .env.exanple .env`
2. Choose between docker or Local instance to run the application

### Docker
#### Requirements

* Docker Compose

#### Running the application

1. Start the application `docker-compose up backend`
2. Migrate the database `docker-compose exec backend ./manage.py migrate`


### Local instance
#### Requirements

* Docker or PostgresQl instance running
* Make
* Python => 3.9.2
* Pip

#### Setup and run the application

1. Install virtualenv `pip install virtualenv`
2. Create your virtualenv `{PATH/TO/YOUR/PYTHON3.9} -m venv venv` (don't change the env name)
3. Activate your venv `source venv/bin/activate`
4. Run postgresql `make prepare` if you are using docker, else just adjust .env accordly
5. Setup your venv `make setupvenv`
6. Run tests `make test`
7. Run server `make start`

## Acessing the application
--- 
**IMPORTANT**

This api is made to run under a microservice architecture, wouldn't be nice to have endpoints to create a user (client), or to login the user.
since is expected to the user to exists on other services already.
With this in mind your user will be altomaticly created on your first access a token (that would be created by another service)
To test everything setup your evironment and run `./manage.py create_token YOUR_EMAIL` you will receive a token that mush be on headers in each request.

---

Every action has a render (Django Rest Framework), but is configurated to on production return only json responses already, oppitionally you can force receieving json response including `?format=json` at the end like `/api/clients/?format=json`


You can check the documentation to [Clients Endpoint](docs/api/clients.md) or [Products Endpoint](docs/api/products.md)

To more informations in how to make requests to the api check postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/c87bb77b702e705740c7)
