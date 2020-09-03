
# Something about IdenttiyServer4

- [Something about IdenttiyServer4](#something-about-identtiyserver4)
  - [user sign-in to IdentityServer via cookie on default](#user-sign-in-to-identityserver-via-cookie-on-default)
  - [Use Identity Server End Points](#use-identity-server-end-points)
  - [Authentication and authorization for SPAs](#authentication-and-authorization-for-spas)
  - [Path of Identity](#path-of-identity)
  - [重写租户登录](#重写租户登录)
  - [others](#others)

## user sign-in to IdentityServer via cookie on default

``` cs
// IdentityServerServiceCollectionExtensions.cs

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

        // ......
}
```

- the preceding [source code - `service.AddIdentityServer()`](https://github.com/IdentityServer/IdentityServer4/blob/18897890ce2cb020a71b836db030f3ed1ae57882/src/IdentityServer4/src/Configuration/DependencyInjection/IdentityServerServiceCollectionExtensions.cs#L29-L53)
- In IdentitiServer4 [Authentication is tracked with a cookie managed by the cookie authentication handler from ASP.NET Core.](https://identityserver4.readthedocs.io/en/latest/topics/signin.html#cookie-authentication)



## Use Identity Server End Points

``` cs
// Startup.cs

public void Configure(IApplicationBuilder app)
{
    // ......

    app.UseRouting();
    app.UseIdentityServer();
    app.UseAuthorization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapDefaultControllerRoute();
    });
}
```

- identity server 4 endpoints are independent of app.UserEndpoints which runs later

``` cs
// IdentityServerApplicationBuilderExtensions.cs

public static IApplicationBuilder UseIdentityServer(this IApplicationBuilder app, IdentityServerMiddlewareOptions options = null)
{
    // ......

    app.UseMiddleware<MutualTlsEndpointMiddleware>();
    app.UseMiddleware<IdentityServerMiddleware>();
    return app;
}
```

- [app.UseIdentityServer() source](https://github.com/IdentityServer/IdentityServer4/blob/18897890ce2cb020a71b836db030f3ed1ae57882/src/IdentityServer4/src/Configuration/IdentityServerApplicationBuilderExtensions.cs#L23-L49)



``` cs
// EndpointRouter.cs

public async Task Invoke(HttpContext context, IEndpointRouter router, IUserSession session, IEventService events, IBackChannelLogoutService backChannelLogoutService)
{
    // ......
        var endpoint = router.Find(context);
        // ......
            var result = await endpoint.ProcessAsync(context);
            // ......
                await result.ExecuteAsync(context);
    // ......
}
```
- [EndpointRouter source](https://github.com/IdentityServer/IdentityServer4/blob/18897890ce2cb020a71b836db030f3ed1ae57882/src/IdentityServer4/src/Hosting/EndpointRouter.cs#L27-L66)
- use is4 router to attach the endpoint of is4
- `IdentityServerMiddleware.Invoke -> EndPointRouter.FindEndPoint -> IEndPointHanlder.Process`



## Authentication and authorization for SPAs

[official doc](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity-api-authorization?view=aspnetcore-3.1)

- Inside the `Startup.ConfigureServices` method:
    - IdentityServer with an additional AddApiAuthorization helper method that sets up some default ASP.NET Core conventions on top of IdentityServer:

    ``` cs
    // Startup.cs

    services.AddIdentityServer()
        .AddApiAuthorization<ApplicationUser, ApplicationDbContext>();
    ```

    - details about [`AddApiAuthorization()`](https://github.com/dotnet/aspnetcore/blob/9a1810c1dbe432fc7bc7e8bc68fa22ab787c0452/src/Identity/ApiAuthorization.IdentityServer/src/IdentityServerBuilderConfigurationExtensions.cs#L43-L74)

    ``` cs
    // IdentityServerBuilderConfigurationExtensions.cs

    public static IIdentityServerBuilder AddApiAuthorization<TUser, TContext>(
        this IIdentityServerBuilder builder,
        Action<ApiAuthorizationOptions> configure)
            where TUser : class
            where TContext : DbContext, IPersistedGrantDbContext
    {
        // ......

        builder.AddAspNetIdentity<TUser>()
            .AddOperationalStore<TContext>()
            .ConfigureReplacedServices()
            .AddIdentityResources()
            .AddApiResources()
            .AddClients()
            .AddSigningCredentials();

        // ......
    }
    ```

    - Authentication with an additional AddIdentityServerJwt helper method that configures the app to validate JWT tokens produced by IdentityServer:

    ``` cs
    services.AddAuthentication()
        .AddIdentityServerJwt();
    ```

* Inside the `Startup.Configure` method:
  * The authentication middleware that is responsible for validating the request credentials and setting the user on the request context:

    ```csharp
    app.UseAuthentication();
    ```

  * The IdentityServer middleware that exposes the OpenID Connect endpoints:

    ```csharp
    app.UseIdentityServer();
    ```


- AddApiAuthorization
    - This helper method configures IdentityServer to use our supported configuration. ......
- AddIdentityServerJwt
    - This helper method configures a policy scheme for the app as the default authentication handler. The policy is configured to let Identity handle all requests routed to any subpath in the Identity URL space "/Identity". The `JwtBearerHandler` handles all other requests. ......
- WeatherForecastController
    - In the *Controllers\WeatherForecastController.cs* file, notice the `[Authorize]` attribute applied to the class that indicates that the user needs to be authorized based on the default policy to access the resource. The default authorization policy happens to be configured to use the default authentication scheme, which is set up by `AddIdentityServerJwt` to the policy scheme that was mentioned above, making the `JwtBearerHandler` configured by such helper method the default handler for requests to the app.

## Path of Identity

- It's on `/Identity/account/login` when adding default identity
    - `AddDefaultIdentity -> AddDefaultUI -> IdentityDefaultUIConfigureOptions -> “/Identity/account/login”`
- custome ui on `/account/login` when only adding identity
    - `AddIdentity -> "/account/login"`



## 重写租户登录
``` cs
// ProfileService
// auth 后 token 中包含响应 claims
:AuthorizeEndPoint -> :AuthorizeResponseGenerator -> :DefaultTokenService -> :DefaultClaimService -> :ProfileService

// AuthorizeResponseGenerator
// 作用之一：用户是不是需要登录或授权等
:AuthorizeEndPoint -> :AuthorizeResponseGenerator
```

## others
- [Use Cookie in MVC Client - Interactive Applications with ASP.NET Core](http://docs.identityserver.io/en/latest/quickstarts/2_interactive_aspnetcore.html#creating-an-mvc-client)
- [[JWT] TokenValidationParameters RoleClaimType Not Fully Respected](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet/issues/1214)
- [Simplify clearing the JWT claims type mappings](https://github.com/dotnet/aspnetcore/issues/4660)
- [理解 OpenID Connect Hybrid 模式](http://www.ngbeijing.cn/2019/07/02/2019-07-02_openid_connect_hybrid_flow/)
- [RS256 JWT签名 - 非对称加密](https://zhuanlan.zhihu.com/p/70275218)
- [IdentityServer4源码解析_1_项目结构](https://holdengong.com/identityserver4%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90_1_%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84/)
- [Scaffold Identity in ASP.NET Core projects](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/scaffold-identity?view=aspnetcore-3.1)
- [How to Implement Tenant Selection In Identity Server 4 For Multi Tenant Application](https://lalitacode.com/how-to-implement-tenant-selection-in-identity-server-4-application/)
- [Implement Domain Or Subdomain Based Multi Tenancy In Identity Server](https://lalitacode.com/implement-domain-or-subdomain-based-multi-tenancy-in-identity-server/)
