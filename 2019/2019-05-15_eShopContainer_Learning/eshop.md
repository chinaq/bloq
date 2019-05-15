# eShopContainer Learning
### learning examples form micosoft

## set up
- if on mac, please set `IdentityUrl` in `docker-compose.override.yml`
``` yml
IdentityUrl=http://docker.for.mac.localhost:5105
# Local Mac: Use http://docker.for.mac.localhost:5105
# || Local Windows:  Use 10.0.75.1 in a "Docker for Windows" environment, if using "localhost" from browser.
# || Remote access: Use ${ESHOP_EXTERNAL_DNS_NAME_OR_IP} if using external IP or DNS name from browser.
```
- While `microsoft/mssql-server-linux` is not inited correctly after `docker-compose up`, please rm it and `docker-compose` again.