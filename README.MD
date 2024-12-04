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
docker-compose run --rm app flake8
docker-compose run --rm app python3 manage.py loaddata main/fixtures/fixtures.json
docker-compose run --rm app python3 manage.py dumpdata main --indent 4 > main/fixtures/fixtures.json
```

# commands for prod server

for troubleshooting

```
sudo tail -F /var/log/nginx/error.log
sudo journalctl -u gunicorn.socket
```
