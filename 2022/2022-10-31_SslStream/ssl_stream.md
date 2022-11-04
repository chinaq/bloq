# SslStream in dotnet

## 问题
- 加载证书
    - dotnet 的 `SslStream` 只能加载单一证书
        - 即便使用 collection，也只会加载第一个符合的，如果需要加载验证对方的 root CA 只能使用 store 加载至系统证书库中再使用
            - [Verifying the chain of a self-signed certificate when using SslStream](https://stackoverflow.com/questions/57619863/verifying-the-chain-of-a-self-signed-certificate-when-using-sslstream)
        - dotnet 只能忽略相关验证
            - [sslStream and RemoteCertificateChainErrors](https://social.msdn.microsoft.com/Forums/en-US/8aeadd67-16ba-40e0-b9d6-262e6e7f5a94/sslstream-and-remotecertificatechainerrors?forum=netfxnetcom)
        - 以上内容不正确，请参见后续 [`AuthenticateAsClient`](../2022-11-04_AuthenticateAsClient/auth.md)
    - go 可直接加载 CA - [Https单向认证和双向认证](https://wiki.wgpsec.org/knowledge/base/network-https.html)
    - 其他示例 - [HTTPS双向认证（Mutual TLS authentication)](https://help.aliyun.com/document_detail/160093.html)
        - 注：集中客户端忽略了 CA 检验
        - `SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.`
- mac ssl 错误 - `Interop+AppleCrypto+SslException`
    - 使用 debug 模式可正常运行 - [dotnet core 3.0 SSL works in debug mode but not with `dotnet run`](https://stackoverflow.com/questions/58799673/dotnet-core-3-0-ssl-works-in-debug-mode-but-not-with-dotnet-run)
    - 更奇怪的是，强制 rebuild 也可执行 `dotnet build --no-incremental &&  dotnet run`


# 其他
- 以后可尝试的库 - [SuperSimpleTcp](https://github.com/jchristn/SuperSimpleTcp)
    - SuperSimpleTcp provides simple methods for creating your own TCP-based sockets application, enabling easy integration of connection management, sending, and receiving data.
- 好用的 ssl 数据发送软件 - [PacketSender](https://github.com/dannagle/PacketSender)
    - Packet Sender is an open source utility to allow sending and receiving TCP, UDP, and SSL (encrypted TCP) packets as well as HTTP/HTTPS requests and panel generation. 
