# Authentication

- [Authentication](#authentication)
  - [Use cookie authentication without ASP.NET Core Identity](#use-cookie-authentication-without-aspnet-core-identity)
    - [The Doc](#the-doc)
    - [ConfigureServices](#configureservices)
    - [Configure](#configure)
    - [Controller](#controller)
      - [Sign in](#sign-in)
      - [Sign out](#sign-out)
    - [Keys](#keys)
  - [用最简单的方式在ASP.NET Core应用中实现认证、登录和注销 - 大内老A](#用最简单的方式在aspnet-core应用中实现认证登录和注销---大内老a)

## Use cookie authentication without ASP.NET Core Identity

###  [The Doc](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/cookie?view=aspnetcore-3.1)

### ConfigureServices
``` cs
services
    .AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie();
```

> Specifying the default scheme results in the `HttpContext.User` property being set to that identity. If that behavior isn't desired, disable it by invoking the parameterless form of `AddAuthentication()`.

-- from [Authorize with a specific scheme in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-3.1)

### Configure
``` cs
app.UseAuthentication();
app.UseAuthorization();

app.UseEndpoints(endpoints =>
{
    endpoints.MapControllers();
    endpoints.MapRazorPages();
});
```

### Controller
#### Sign in
``` cs
var claims = new List<Claim>
{
    new Claim(ClaimTypes.Name, user.Email),
    new Claim("FullName", user.FullName),
    new Claim(ClaimTypes.Role, "Administrator"),
};

var claimsIdentity = new ClaimsIdentity(
    claims, CookieAuthenticationDefaults.AuthenticationScheme);

var authProperties = new AuthenticationProperties
{
    //AllowRefresh = <bool>,
    //ExpiresUtc = DateTimeOffset.UtcNow.AddMinutes(10),
    //IsPersistent = true,
    //IssuedUtc = <DateTimeOffset>,
    //RedirectUri = <string>
};

await HttpContext.SignInAsync(
    CookieAuthenticationDefaults.AuthenticationScheme, 
    new ClaimsPrincipal(claimsIdentity), 
    authProperties);
```

#### Sign out
``` cs
await HttpContext.SignOutAsync(
    CookieAuthenticationDefaults.AuthenticationScheme);
```

### Keys
- SignIn `ClaimsPrincipal` by `HttpContext.SignInAsync`, while Identity SignIn by `UserManager.SignAsync` which based on `HttpContext.SignInAsync` in depth.


## [用最简单的方式在ASP.NET Core应用中实现认证、登录和注销](https://www.cnblogs.com/artech/p/authentication-sign-in-out.html) - 大内老A