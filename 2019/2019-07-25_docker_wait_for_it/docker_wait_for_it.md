# Docker wait-for-it

## waiting for ports
``` bash
#!/usr/bin/env bash

./wait-for-it $MYSQL_DB
if [[ $? -gt 0 ]]; then 
    exit 1 
fi

./wait-for-it $RABBITMQ
if [[ $? -gt 0 ]]; then
    exit 1
fi

dotnet NBIoT.API.dll
```

## ref
- [wait-for-it](https://github.com/vishnubob/wait-for-it)
- [Control startup and shutdown order in Compose](https://docs.docker.com/compose/startup-order/)
- [Include Files Outside Docker Build Context](https://www.jamestharpe.com/include-files-outside-docker-build-context/)