# AuthenticateAsClient

- [X509Chain Validation with my own self signed CA - github](https://github.com/dotnet/runtime/issues/39283#issuecomment-658280486)

``` cs
    // self-signed certification

    chain.ChainPolicy.RevocationMode = X509RevocationMode.NoCheck;
    chain.ChainPolicy.VerificationFlags = X509VerificationFlags.AllowUnknownCertificateAuthority;
    chain.ChainPolicy.RevocationFlag = X509RevocationFlag.EndCertificateOnly;
    chain.ChainPolicy.TrustMode = X509ChainTrustMode.CustomRootTrust;
    chain.ChainPolicy.CustomTrustStore.Add((X509Certificate2)caCert);
```

- 这玩意在 Mac 上是如下这般运行的

``` cs

// 客户端证书验证

// SslStream
SslStream.AuthenticateAsClient
    // SslStream.IO
    -> SslStream.ProcessAuthenticationAsync
        -> SslStream.ForceAuthenticationAsync
            -> SslStream.CompleteHandshake
                // SslStream.Protocal
                -> SslStream.VerifyRemoteCertificate
                    // 从此处起与原生系统挂钩
                    // CertificateValidationPal.OSX
                    -> CertificateValidationPal.VerifyCertificateProperties

                        // 检查证书链
                        -> X509Chain.Build
                            // ChainPal.Apple
                            -> ChainPal.BuildChain
                                -> SecTrustChainPal.Excute
                                    -> Interop.AppleCrypto.X509ChainGetTrustResults
                                        // al_x509chain.c
                                        -> AppleCryptoNative_X509ChainGetTrustResults

                        // 检查证书名，又不止于此
                        -> Interop.AppleCrypto.SslCheckHostnameMatch
                            // pal_ssl.c
                            -> AppleCryptoNative_SslIsHostnameMatch
```

