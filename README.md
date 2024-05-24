# Furum Django webapp
Forum for pet enthusiasts

## Setup
clone repo:
```sh
$ git clone https://github.com/SiimAllik/Furum.git
$ cd Furum
```
Build docker container from Dockerfile

```sh
$ docker build . -t docker-furum
```

Run the container on port 8000

```sh
$ docker run --name furum-container -p 8000:8000 docker-furum
```
## Additional commands

### Testing the project

```sh
$  docker exec -ti furum-container /bin/bash
$  python manage.py test
```
exit the container bash by pressing CTRL+d

### Stopping container:

```sh
$ docker stop furum-container
```
