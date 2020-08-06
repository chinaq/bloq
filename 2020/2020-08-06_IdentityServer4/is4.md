
# Something about IdenttiyServer4

- [Something about IdenttiyServer4](#something-about-identtiyserver4)
  - [user sign-in to IdentityServer via cookie on default](#user-sign-in-to-identityserver-via-cookie-on-default)
  - [others](#others)

## user sign-in to IdentityServer via cookie on default

``` cs
/// <summary>
/// Adds IdentityServer.
/// </summary>
/// <param name="services">The services.</param>
/// <returns></returns>
public static IIdentityServerBuilder AddIdentityServer(this IServiceCollection services)
{
    var builder = services.AddIdentityServerBuilder();

    builder
        .AddRequiredPlatformServices()
        .AddCookieAuthentication()
        .AddCoreServices()
        .AddDefaultEndpoints()
        .AddPluggableServices()
        .AddValidators()
        .AddResponseGenerators()
        .AddDefaultSecretParsers()
        .AddDefaultSecretValidators();

    // provide default in-memory implementation, not suitable for most production scenarios
    builder.AddInMemoryPersistedGrants();

    return builder;
}
```

- the preceding [source code - `service.AddIdentityServer()`](https://github.com/IdentityServer/IdentityServer4/blob/18897890ce2cb020a71b836db030f3ed1ae57882/src/IdentityServer4/src/Configuration/DependencyInjection/IdentityServerServiceCollectionExtensions.cs#L29-L53)
- In IdentitiServer4 [Authentication is tracked with a cookie managed by the cookie authentication handler from ASP.NET Core.](https://identityserver4.readthedocs.io/en/latest/topics/signin.html#cookie-authentication)


## others
- [Use Cookie in MVC Client - Interactive Applications with ASP.NET Core](http://docs.identityserver.io/en/latest/quickstarts/2_interactive_aspnetcore.html#creating-an-mvc-client)
- [[JWT] TokenValidationParameters RoleClaimType Not Fully Respected](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet/issues/1214)
- [Simplify clearing the JWT claims type mappings](https://github.com/dotnet/aspnetcore/issues/4660)
- [理解 OpenID Connect Hybrid 模式](http://www.ngbeijing.cn/2019/07/02/2019-07-02_openid_connect_hybrid_flow/)
- [RS256 JWT签名 - 非对称加密](https://zhuanlan.zhihu.com/p/70275218)
