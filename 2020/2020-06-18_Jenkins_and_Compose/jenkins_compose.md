# Jenkins with docker-compose

- run Jenkins in Docker via offical doc
  - run docker in docker to support docker command in Jenkins docker container
  - run Jenkins in docker
  - post install Jenkins
- next - how to support the docker-compose command
    - make a new Dockerfile wrapped Jenkins with docker-compose from [clutteredcode/dind-compose](https://hub.docker.com/r/clutteredcode/dind-compose/dockerfile)
    - this dockerfile is to wrapped dind with compose, please renew it to wrap the Jenkins

``` Dockerfile
FROM docker:stable-dind

LABEL maintainer "David Clutter <cluttered.code@gmail.com>"

RUN apk update &&\
    apk upgrade --no-cache &&\
    apk add --no-cache python libffi openssl &&\
    apk add --no-cache --virtual .build-deps python-dev py-pip libffi-dev openssl-dev gcc libc-dev make &&\
    pip install --no-cache-dir docker-compose &&\
    apk del .build-deps
```
