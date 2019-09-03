# Deploy production of create-react-app on Docker Compose

- Because
    - **[The environment variables are embedded during the build time. ](https://create-react-app.dev/docs/adding-custom-environment-variables)**
- Please
    - [Understanding Docker Build Args, Environment Variables and Docker Compose Variables](https://vsupalov.com/docker-env-vars/)

``` yml
# docker-compose.yml

......
services:
  web-react-prod:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        REACT_APP_API_ADDRESS: "http://localhost:5001"
    image: web-react-prod
......
```

``` Dockerfile
# Dockerfile

......
ARG REACT_APP_API_ADDRESS
ENV REACT_APP_API=$REACT_APP_API_ADDRESS
RUN npm run build
......
```