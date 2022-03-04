# 自签名证书与自制 CA 证书


## mkcert vs dotnet-dev-certs
- mkcert 生成的证书 nodejs-https-request 可以通过，而 dotnet-dev-certs 生成的证书却不行
    - mkcert 先生成 CA certificate 再生成 server certificate
    - dotnet-dev-certs 直接生成 server certificate

## 本机注册的 certs
- mkcert 注册了 CA certificate
- dotnet-dev-certs 直接注册了 server certificate，但也添加了完全信任

## nodejs-https-request
- 由于 nodejs 不使用本机 CA，必须注册 CA 才可 https-request

## ref
- [Monkey patching tls in node.js to support self-signed certificates with custom root certificate authorities](https://medium.com/trabe/monkey-patching-tls-in-node-js-to-support-self-signed-certificates-with-custom-root-cas-25c7396dfd2a)
- [Create Your Own SSL Certificate Authority for Local HTTPS Development](https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/)
- [Creating a Self-Signed Certificate With OpenSSL](https://www.baeldung.com/openssl-self-signed-cert)
- [asp.net web api 使用自签名SSL证书](https://cloud.tencent.com/developer/article/1054686)
- [How to extract the private key, public key and CA cert from PFX](https://opentechtips.com/how-to-extract-the-private-key-public-key-and-ca-cert-from-pfx/)
