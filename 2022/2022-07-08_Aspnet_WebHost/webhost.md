# Asp.Net 的 WebHost

- [Asp.Net 的 WebHost](#aspnet-的-webhost)
    - [从 host 到 services](#从-host-到-services)
    - [asp.net 3.x/5 的 Host](#aspnet-3x5-的-host)
    - [asp.net 6 的 WebApplication](#aspnet-6-的-webapplication)


## 从 host 到 services
- 构建 Web Host
    - ![build_run_host](./img/build_run_host.jpg)
- 从 Connection Delegate 到 HttpConnection MiddleWare
    - ![connection_delegate](./img/connection_delegate.jpg)
- 从 Connection Context 到 Http Context
    - ![connection context to http context](img/ConnectionContext_to_HttpContext.jpg)
- AppServices & RequestServices
    - ![services](./img/AppServices_and_RequestServices.jpg)


## asp.net 3.x/5 的 Host
- Host & Builder
    - ![host builder](./img/host_1_2.jpg)
- Host Run
    - ![host run](./img/host_3.jpg)
- GenericWebHostBuilder
    - ![generic webhost builder](./img/generic_webhost_builder.jpg)
- Create & Use Middleware
    - ![middleware](img/middeware.jpg)

## asp.net 6 的 WebApplication
- WebApplication
    - ![web application](img/webapplication.jpg)
- TcpApplciation
    - ![tcp application](img/tcpapplication.jpg)
