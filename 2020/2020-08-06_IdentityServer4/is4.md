
# Something about IdenttiyServer4

- [Something about IdenttiyServer4](#something-about-identtiyserver4)
  - [user sign-in to IdentityServer via cookie on default](#user-sign-in-to-identityserver-via-cookie-on-default)
  - [Use Identity Server End Points](#use-identity-server-end-points)
  - [others](#others)

## user sign-in to IdentityServer via cookie on default

``` cs
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



## Use Identity Server End Points

``` cs
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
public static IApplicationBuilder UseIdentityServer(this IApplicationBuilder app, IdentityServerMiddlewareOptions options = null)
{
    // ......

    // it seems ok if we have UseAuthentication more than once in the pipeline --
    // this will just re-run the various callback handlers and the default authN 
    // handler, which just re-assigns the user on the context. claims transformation
    // will run twice, since that's not cached (whereas the authN handler result is)
    // related: https://github.com/aspnet/Security/issues/1399
    if (options == null) options = new IdentityServerMiddlewareOptions();
    options.AuthenticationMiddleware(app);

    app.UseMiddleware<MutualTlsEndpointMiddleware>();
    app.UseMiddleware<IdentityServerMiddleware>();
    return app;
}
```

- [source](https://github.com/IdentityServer/IdentityServer4/blob/18897890ce2cb020a71b836db030f3ed1ae57882/src/IdentityServer4/src/Configuration/IdentityServerApplicationBuilderExtensions.cs#L23-L49)



``` cs
public async Task Invoke(HttpContext context, IEndpointRouter router, IUserSession session, IEventService events, IBackChannelLogoutService backChannelLogoutService)
{
    // this will check the authentication session and from it emit the check session
    // cookie needed from JS-based signout clients.
    await session.EnsureSessionIdCookieAsync();

    context.Response.OnStarting(async () =>
    {
        if (context.GetSignOutCalled())
        {
          // .....
        }
    });

    try
    {
        var endpoint = router.Find(context);
        if (endpoint != null)
        {
            _logger.LogInformation("Invoking IdentityServer endpoint: {endpointType} for {url}", endpoint.GetType().FullName, context.Request.Path.ToString());

            var result = await endpoint.ProcessAsync(context);
            if (result != null)
            {
                _logger.LogTrace("Invoking result: {type}", result.GetType().FullName);
                await result.ExecuteAsync(context);
            }

            return;
        }
    }
    catch (Exception ex)
    {
      // ......
    }

    await _next(context);
}
```
- [source](https://github.com/IdentityServer/IdentityServer4/blob/18897890ce2cb020a71b836db030f3ed1ae57882/src/IdentityServer4/src/Hosting/EndpointRouter.cs#L27-L66)
- use is4 router to attach the endpoint of is4
- `IdentityServerMiddleware.Invoke -> EndPointRouter.FindEndPoint -> IEndPointHanlder.Process`



## others
- [Use Cookie in MVC Client - Interactive Applications with ASP.NET Core](http://docs.identityserver.io/en/latest/quickstarts/2_interactive_aspnetcore.html#creating-an-mvc-client)
- [[JWT] TokenValidationParameters RoleClaimType Not Fully Respected](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet/issues/1214)
- [Simplify clearing the JWT claims type mappings](https://github.com/dotnet/aspnetcore/issues/4660)
- [理解 OpenID Connect Hybrid 模式](http://www.ngbeijing.cn/2019/07/02/2019-07-02_openid_connect_hybrid_flow/)
- [RS256 JWT签名 - 非对称加密](https://zhuanlan.zhihu.com/p/70275218)
- [IdentityServer4源码解析_1_项目结构](https://holdengong.com/identityserver4%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90_1_%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84/)
