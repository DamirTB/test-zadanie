# Commands for launching in development

use the following command, to launch the application in development

```
docker-compose up --build
```

## Global commands for docker
```
docker system prune -a
docker volume prune
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```

# one-time commands for docker-containers

```
docker-compose run --rm app python3 manage.py migrate
docker-compose run --rm app python3 manage.py makemigrations
docker-compose run --rm app python3 manage.py createsuperuser
docker-compose run --rm app python3 manage.py collectstatic
docker-compose run --rm app flake8
docker-compose run --rm app python3 manage.py loaddata main/fixtures/fixtures.json
docker-compose run --rm app python3 manage.py dumpdata main --indent 4 > main/fixtures/fixtures.json
```

# commands for prod server

## for troubleshooting

```
sudo tail -F /var/log/nginx/error.log
sudo journalctl -u gunicorn.socket
sudo systemctl status gunicorn
```

## for restarting

```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

# Endpoints and what they do

## Main tasks APIs

| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `GET`    | `/en-us/api/main/tasks`                             | Retrieve all tasks.                      |
| `POST`   | `/en-us/api/main/tasks`                             | Create a new task.                       |
| `PATCH`  | `/en-us/api/main/tasks/{id}`                          | Partial update a single task with specific id.                 |
| `DELETE` | `/en-us/api/main/tasks/{id}`  | Delete a single task with specific id.                    |
| `PUT`    | `/en-us/api/main/tasks/{id}` | Full update a single task with specific id |
| `GET` | `/en-us/api/main/tasks/?priority={value}&status={value}` | Retrieve tasks with filter | 

Example of how a single task json might look like 

```
{
        "id": 1,
        "name": "Homework",
        "text": "Finish the homework",
        "priority": 1,
        "status": 0,
        "finished": null,
        "created": "2024-12-04T19:25:49.619000+05:00"
}
```



## User APIs 

| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `POST`    | `/en-us/api/auth/login`                             | Login user & receive JWT token.                      |
| `POST`   | `/en-us/api/auth/registration`                             | Create a new user. email is optional field                      |
| `POST`  | `/en-us/api/auth/logout`                          | End user session                 |
| `GET`  | `/en-us/api/auth/user`                          | Receive current logged in user info                 |
