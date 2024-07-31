# NIQ

## BEFORE ALL

> All the comands must be run in the root of the project

### DOTENV FILES

As you can see all the comands must be run with a parameter pointing to a envfile, for consistency pls leave your env files in the folder called envs, there is a template that holds the env variables but you neet to change its names to `api.env` and `psql.env` 

## DEVELOPMENT

For development just run 

```bash
python app/main.py
```


## JUST DOCKERFILES

For deploying using just plain docker containers you need to do this steps

```bash
#Create the volume for postgres
docker volume create postgres_data

#Create a network for our containers
docker network create niq-net

#First create the postgres container
docker run --name some_postgres --env-file psql.env -d --net niq-net -v postgres_data:/var/lib/postgresql/data postgres:16


#Build the image of our app
docker build -t niq-api:1.0 -f docker/Dockerfile .
#run the api image
docker run --name flask-api --net niq-net --env-file app/.env -p 8080:8080 test-flask-api

```



## DOCKERCOMPOSE

Here it will initialize all the services by itself

```bash
docker compose -f ./docker/docker-compose.yml --env-file envs/api.env --env-file envs/psql.env  up --build
```

