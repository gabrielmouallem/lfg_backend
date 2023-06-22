# LFG - Loan For Goods Project

## 1. Install Docker

Install docker following the link: https://docs.docker.com/get-docker/

- Make sure to run docker on windows 10 after installation

## 2. Running Celery Redis Broker

```bash
docker-compose exec web celery -A lfg_backend worker -l info
``` 

## 3. Make the docker compose up

```bash
docker-compose up --build
``` 

## 4. Create a django superuser inside the docker container

```bash
docker-compose run web python manage.py createsuperuser
``` 

To create a superuser for the admin page with the preferred username and password.

## 5. Make the migrations if necessary

```bash
docker-compose run web python manage.py makemigrations
``` 

and then:

```bash
docker-compose run web python manage.py migrate
``` 

## 6. You can access the app on

http://localhost:8000/

## 7. You can access the admin page on

http://localhost:8000/admin


## [IMPORTANT]

If for any reason the django backend starts before the postgres database is ready just change any line on the django project and hit save, with that the hot reload will restart the server and then connect to the database properly since the database will be ready then.