# Implement Domain Or Subdomain Based Multi Tenancy In Identity Server

Lalita
May 20, 2020

In this tutorial we saw how to implement tenant selection page in Identity Server 4. There I told you that there are other ways to do multi tenancy. Instead of tenant selection page where the user can select the tenant we can also determine tenant using domain or subdomain name. So, this is our topic for today. In this tutorial I am going to show you how to implement domain or subdomain based multi tenancy in Identity Server 4. Like the previous tutorial I have used .Net Core 3.1, SQL Server and Angular as our client app. The example implements Authorization Code Flow with PKCE but you can implement any OIDC flow you want. I am not going to create a Identity Server application from the beginning as it would be out of scope of this tutorial. So, before you begin have your Identity Server application up and running. Let’s begin.

The architecture of our application is going to be like this. We will have multiple tenants in our application. Each tenant will access our application through their own subdomains, For Eg, tenant1.lalita.com, tenant2.lalita.com etc. Each of these tenants are going to have their corresponding Authorization Server (Identity Server 4) running on tenant1.lalitaauth.com, tenant2.lalitaauth.com. Similarly we will have API’s running on tenant1.lalitaapi.com, tenant2.lalitaapi.com and so on. For simplicity I have used just “lalita.com” as our base domain name, because it is easy to develop that way. This can be changed according to your liking during deployment.

So, lets create a multi tenant application in Identity Server 4. In your Identity Server project create a user service class. I have named it ProfileService in this example. The code is as follows :

``` cs
public class ProfileService : IProfileService
    {
        private readonly IUserClaimsPrincipalFactory<ApplicationUser> _claimsFactory;
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly IHttpContextAccessor _context;

        public ProfileService(IHttpContextAccessor context,UserManager<ApplicationUser> userManager, IUserClaimsPrincipalFactory<ApplicationUser> claimsFactory)
        {
            _context = context;
            _userManager = userManager;
            _claimsFactory = claimsFactory;
        }

        public async Task GetProfileDataAsync(ProfileDataRequestContext context)
        {
            var sub = context.Subject.GetSubjectId();
            var user = await _userManager.FindByIdAsync(sub);
            var principal = await _claimsFactory.CreateAsync(user);

            var claims = principal.Claims.ToList();
            claims = claims.Where(claim => context.RequestedClaimTypes.Contains(claim.Type)).ToList();

            // Add custom claims in token here based on user properties or any other source
          string.Empty));
            claims.Add(new Claim("TenantId", user.TenantId ?? string.Empty));

            context.IssuedClaims = claims;
        }
        
        public async Task IsActiveAsync(IsActiveContext context)
        {
           
           

            //var tokenId = _interaction.
            var sub = context.Subject.GetSubjectId();
            var user = await _userManager.FindByIdAsync(sub);

            if (context.Caller == "AuthorizeEndpoint")
            {
                var tenantId = _context.HttpContext.Request.Query["acr_values"].ToString().Replace("tenant:", "");
                if (user != null && tenantId == user.TenantId)
                {
                    context.IsActive = true;
                }
                else
                {
                    context.IsActive = false;
                }
            }
            else
            {
                context.IsActive = user != null;
            }       
        }

    }
```

I will explain some of the important part of the code above. Above we have create a ProfileService class which extends IProfileService. Here we have simply implented GetProfileDataAsync method where we add a new claim to the token called “TenantId”. This method is called after the user successfully logins. In this same class we have implemented another method called IsActiveAsync. This is a very important method as this is called everytime during the Authorization flow, so this is good place to implement custom logic if needed. Here, we will get the acr_values which the client sends to the Authorization Server during authorization requests. The acr_value will be same as the subdomain name. This will be also be our Tenant Id. If acr_value matches the TenantId in our token we authorized the request. If not then we set IsActive to false which will cause an unauthorized result. You can also resolve the TenantId of the request using redirect_uri or client_uri but I think acr_values is a better way to do it.

Register the ProfileService and IHttpContextAccessor in ConfigureService which we have made use of method of StartUp.cs.

``` cs
services.AddSingleton<IHttpContextAccessor, HttpContextAccessor>();
services.AddScoped<IProfileService, ProfileService>();
```

Also don’t forget to enable CORS as follows. Create a variable for your CORS settings in Startup.cs.

``` cs
private readonly string MyAllowSpecificOrigins = “_myAllowSpecificOrigins”;
```

Now in ConfigureServices method add the CORS settings. This settings will be different according to your development or deployement configurations.

``` cs
 options.AddPolicy(MyAllowSpecificOrigins, builder =>
                {
                    builder.WithOrigins("https://localhost:4200", 
                        "http://localhost:4200", 
                        "https://tenant1.lalita.com:4200",
                        "https://tenant2.lalita.com:4200",
                        "http://tenant1.lalita.com:4200",
                        "http://tenant2.lalita.com:4200");
                    builder.WithHeaders("Authorization");
                    builder.WithHeaders("content-type");

                });
```

Now in Configure method the same class enable CORS as follows :

``` cs
 app.UseCors(MyAllowSpecificOrigins);
```
Now you need to add the TenantId field to out Identity user model.

``` cs
 public class ApplicationUser : IdentityUser
    {

        public string TenantId { get; set; }
    }
```

Run the migrations and update the database as follows :

``` sh
add-migration 'Tenant Migration" -context IdentityDbContext
update-database -context IdentityDbContext
```

In the above code IdentityDbContext is your Db Context for your Identities. After this process you will have TenantId column in your AspNetUsers table.

AspNetUsers Table
AspNetUsers Table with TenantId Column
You need to make some changes to Login method of Identity Server Account controller. This is the same method you use to do the login. Just make simple changes to the code where we now check if TenantId of our user in database is same as the value we have received through acr_values. Add the following code just before this code:

``` cs
  if (user != null && context.Tenant.ToString() == user.TenantId.ToString())
{
 var result = await _signInManager.PasswordSignInAsync(model.Username, model.Password,
                        model.RememberLogin, lockoutOnFailure: true);
```

This code should be there is you are using Identity Server 4 QuickStarts. Whole login method will be as follows :

``` cs
public async Task<IActionResult> Login(LoginInputModel model, string button)
        {
            // check if we are in the context of an authorization request
            var context = await _interaction.GetAuthorizationContextAsync(model.ReturnUrl);

            // the user clicked the "cancel" button
            if (button != "login")
            {
                if (context != null)
                {
                    // if the user cancels, send a result back into IdentityServer as if they 
                    // denied the consent (even if this client does not require consent).
                    // this will send back an access denied OIDC error response to the client.
                    await _interaction.GrantConsentAsync(context, ConsentResponse.Denied);

                    // we can trust model.ReturnUrl since GetAuthorizationContextAsync returned non-null
                    if (await _clientStore.IsPkceClientAsync(context.ClientId))
                    {
                        // if the client is PKCE then we assume it's native, so this change in how to
                        // return the response is for better UX for the end user.
                        return View("Redirect", new RedirectViewModel { RedirectUrl = model.ReturnUrl });
                    }

                    return Redirect(model.ReturnUrl);
                }
                else
                {
                    // since we don't have a valid context, then we just go back to the home page
                    return Redirect("~/");
                }
            }

            if (ModelState.IsValid)
            {
                var user = await _userManager.FindByNameAsync(model.Username);
                if (user != null && context.Tenant.ToString() == user.TenantId.ToString())
                {
                    var result = await _signInManager.PasswordSignInAsync(model.Username, model.Password,
                        model.RememberLogin, lockoutOnFailure: true);
                    if (result.Succeeded)
                    {
                        await _events.RaiseAsync(new UserLoginSuccessEvent(user.UserName, user.Id, user.UserName));

                        if (context != null)
                        {
                            if (await _clientStore.IsPkceClientAsync(context.ClientId))
                            {
                                // if the client is PKCE then we assume it's native, so this change in how to
                                // return the response is for better UX for the end user.
                                return View("Redirect", new RedirectViewModel { RedirectUrl = model.ReturnUrl });
                            }

                            // we can trust model.ReturnUrl since GetAuthorizationContextAsync returned non-null
                            return Redirect(model.ReturnUrl);
                        }

                        // request for a local page
                        if (Url.IsLocalUrl(model.ReturnUrl))
                        {
                            return Redirect(model.ReturnUrl);
                        }
                        else if (string.IsNullOrEmpty(model.ReturnUrl))
                        {
                            return Redirect("~/");
                        }
                        else
                        {
                            // user might have clicked on a malicious link - should be logged
                            throw new Exception("invalid return URL");
                        }
                    }
                }

                await _events.RaiseAsync(new UserLoginFailureEvent(model.Username, "invalid credentials"));
                ModelState.AddModelError(string.Empty, AccountOptions.InvalidCredentialsErrorMessage);
            }

            // something went wrong, show form with error
            var vm = await BuildLoginViewModelAsync(model);
            return View(vm);
        }
```

For every Tenant you will have to add their respective redirect_uris in the client settings of Identity Server.

Redirect Uris
Redirect Uris for our client
This is all the setup needed in our Authorization Server (Identity Server 4). In our Angular 9 client we will have to set the Authorization Server and Redirect Uris according to the respective tenant. This is a sample client settings in Angular 9 client.

``` js
let sts: string  = 'http://'+window.location.hostname+':5000';

    return () =>
        oidcConfigService.withConfig({
            stsServer: sts,
            redirectUrl: window.location.origin,
            postLogoutRedirectUri:window.location.origin,
            clientId: 'js',
            scope: 'openid profile web_api',
            responseType: 'code',
            silentRenew: true,
            silentRenewUrl: `${window.location.origin}/silent-renew.html`,
            customParams:{acr_values:'tenant:'+window.location.host.split('.')[0]+''}
        });
```

In the above code I have set the Authorization Server (stsServer) according to the tenant. So, if the user access our service through tenant1.lalita.com, the acr_values (tenant), sts_server(Authorization/Identity Server) is going to be set accordingly.

Now we will move on to the API. For this just create a simple .Net Core API project in Visual Studio. All our work in this tutorial. is going to be in this project, from now onward. There are some complications here as we need to set dynamic authority for our JWT Bearer Middleware, and .net Core doesn’t make it simple for us. Anyways lets proceed.

First create a TenantProvider class which we will use to resolve the tenant.

``` cs
  public class TenantProvider
    {
        private readonly IHttpContextAccessor _httpContextAccessor;

        public TenantProvider(IHttpContextAccessor httpContextAccessor)
            => _httpContextAccessor = httpContextAccessor;

        public string GetCurrentTenant()
        {
           
            string requestUrl = $"{this._httpContextAccessor.HttpContext.Request.Host}";
            var tenantId = requestUrl.Split('.')[0];
            string authorityDomain = "lalita.com:5000";
            //string authorityScheme = this._httpContextAccessor.HttpContext.Request.Scheme;
            string authorityScheme = "http";
            string authorityUrl = $"{authorityScheme}://{tenantId}.{authorityDomain}";
            return  authorityUrl;
           
        }
    }
```

Its a simple class where we get the tenant from the Http Request. For this we have injected IHttpContextAccessor using DI. So, if the client access our api like tenant1.lalitaapi.com, the tenant is going to be resolved as “tenant1”. Once again don’t forget to register IHttpContextAccessor and TenantProvider in Configure Service method of Startup.cs.

``` cs
services.AddSingleton<IHttpContextAccessor, HttpContextAccessor>();
services.AddSingleton<TenantProvider>();
``` 

Now that we are working on Startup.cs, lets also add JWT Bearer settings in ConfigureServices method as follows:

``` cs
services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
          .AddJwtBearer(options =>
          {
               options.RequireHttpsMetadata = false;
               // base-address of your identityserver
               options.Authority = "http://lalita.com:5000";

               // name of the API resource
               options.Audience = "web_api";          

              //options.Events = new JwtBearerEvents()
              //{
              //    OnMessageReceived = async context =>
              //    {
                     
              //    }

              //};
          });
```

You can just put the base address of our Authorization Server for now as this is going to be dynamic and set according to the tenant. Once again don’t forget to add CORS settings, which is same as above for our Identity Server project.

Also add authorization in Configure method of Startup.cs.

``` cs
 app.UseAuthorization();
```

Make sure the above code is below app.UseRouting().

To create dynamic JwtBearerOptions we need to implement two more class. First class is JwtOptionsInitializer which is given below.

``` cs
public class JwtOptionsInitializer : IConfigureNamedOptions<JwtBearerOptions>
    {
        private readonly TenantProvider _tenantProvider;

        public JwtOptionsInitializer(
            TenantProvider tenantProvider)
        {

            _tenantProvider = tenantProvider;
        }

        public void Configure(string name, JwtBearerOptions options)
        {
          

            var authority = _tenantProvider.GetCurrentTenant();

            options.Authority = authority;
        }

        public void Configure(JwtBearerOptions options)
            => Debug.Fail("This infrastructure method shouldn't be called.");
    }
```

In the above code we set configrue JwtBearerOptions and set our authority based on the tenant.

Now we will implement the second class required which we need to monitor and fetch changes in JwtBearerOptions.

``` cs
 public class JweBearerOptionsProvider : IOptionsMonitor<JwtBearerOptions>
    {
        private readonly ConcurrentDictionary<(string name, string tenant), Lazy<JwtBearerOptions>> _cache;
        private readonly IOptionsFactory<JwtBearerOptions> _optionsFactory;
        private readonly TenantProvider _tenantProvider;

        public JweBearerOptionsProvider(
            IOptionsFactory<JwtBearerOptions> optionsFactory,
            TenantProvider tenantProvider)
        {
            _cache = new ConcurrentDictionary<(string, string), Lazy<JwtBearerOptions>>();
            _optionsFactory = optionsFactory;
            _tenantProvider = tenantProvider;

            
        }

        public JwtBearerOptions CurrentValue => Get(Options.DefaultName);

        public JwtBearerOptions Get(string name)
        {
            var tenant = _tenantProvider.GetCurrentTenant();

            Lazy<JwtBearerOptions> Create() => new Lazy<JwtBearerOptions>(() => _optionsFactory.Create(name));
            return _cache.GetOrAdd((name, tenant), _ => Create()).Value;
        }

        public IDisposable OnChange(Action<JwtBearerOptions, string> listener) => null;
    }
```

Here we put JwtBearerOptions in a dictionary, for each tenant that accesses our API. Once again we need to register the above two classes in ConfigureServices method of Startup class. Add the just below the code where we registered our TenantProvider.

``` cs
  services.AddSingleton<IOptionsMonitor<JwtBearerOptions>, JweBearerOptionsProvider>();
            services.AddSingleton<IConfigureOptions<JwtBearerOptions>, JwtOptionsInitializer>();
```

Finally we will create a CustomAuthorize attribute.

``` cs
 public void OnAuthorization(AuthorizationFilterContext context)
        {

            var tenantId = context.HttpContext.User.Claims.Where(x => x.Type == "TenantId").FirstOrDefault().Value;
            var requestUrl = $"{context.HttpContext.Request.Host}";
            var requestTenantId = requestUrl.Split('.')[0];
            if (tenantId != requestTenantId)
            {
                context.Result = new UnauthorizedResult();
            }

            var issuer = context.HttpContext.User.FindFirst(x => x.Type == "iss").Value;
            var issuerTenant = new Uri(issuer).Host.Split('.')[0];
            if (issuerTenant != tenantId)
            {
                context.Result = new UnauthorizedResult();
            }
            return;

        }
```

During authorization we check if the TenantId is the same as the TenantId resolved from API Url. If they are not the same we return unauthorized. We also check the issuer to see if it matches with our respective tenant. We can also use this method to dynamically create a connection string to our database according to the tenant information. This can also be checked in JwtBearerEvents OnTokenValidated event.

Now you can decorate your Controller Actions with the custom authorization filter.

``` cs
[CustomAuthorize(AuthenticationSchemes = "Bearer")]
```

Instead of custom Authorization Filter we can also use policy based authorization. I will show you one example quickly. Create policy requirement and handlers as follows.

``` cs
 public class TenantRequirement : IAuthorizationRequirement
    {


        public TenantRequirement()
        {

        }
    }
public class TenantHandler : AuthorizationHandler<TenantRequirement>
    {

        private readonly IHttpContextAccessor _context;
        public TenantHandler(IHttpContextAccessor context)
        {

            _context=context;
        }
        protected override Task HandleRequirementAsync(AuthorizationHandlerContext context,
                                                    TenantRequirement requirement)
        {

            if (!context.User.HasClaim(c => c.Type == "TenantId")|| !context.User.HasClaim(c => c.Type == "iss"))
            {
                //TODO: Use the following if targeting a version of
                //.NET Framework older than 4.6:
                //      return Task.FromResult(0);
                return Task.CompletedTask;
            }


            var tenantId = context.User.Claims.Where(x => x.Type == "TenantId").FirstOrDefault().Value;
            var requestUrl = $"{_context.HttpContext.Request.Host}";
           
            var requestTenantId = requestUrl.Split('.')[0];
            if (tenantId != requestTenantId)
            {
                return Task.CompletedTask;
            }


            var issuer =  context.User.FindFirst(x => x.Type == "iss").Value;
            var issuerTenant = new Uri(issuer).Host.Split('.')[0];
            if(issuerTenant!=tenantId)
            {
                return Task.CompletedTask;
            }
            context.Succeed(requirement);
           

            //TODO: Use the following if targeting a version of
            //.NET Framework older than 4.6:
            //      return Task.FromResult(0);
            return Task.CompletedTask;
        }
    }
```

Now register the handler and policy based authorization is ConfigureServices method of Startup class.

``` cs
 services.AddAuthorization(options =>
            {
                options.AddPolicy("Tenant", policy =>
                    policy.Requirements.Add(new TenantRequirement()));
            });
services.AddSingleton<IAuthorizationHandler, TenantHandler>();
```

Now you can decorate your Controller Actions with policy based authorization filter as follows.

``` cs
 [Authorize(AuthenticationSchemes = "Bearer",Policy ="Tenant")]
```

You can see the code in this Github repository.

So, we have reached to the end of the tutorial. This is all you need to get domain or subdomain based multi tenancy going in Identity Server 4. So, its as easy as that to get Identity Server Multi Tenancy. Once, again there are other ways to get Identity Server Multi Tenancy, such as having user choose the tenant during login, or by resolving the tenant in back end login through user info in the token. There are simply many ways to get Identity Server Multi Tenancy and it all depends on your requirements. You can combine this with tenant selection page for even more fidelity. If you have any issues or problems please leave a comment below or you can contact me directly at info@lalitacode.com. Good, luck.

Lalita.