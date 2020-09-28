# How to Implement Tenant Selection In Identity Server 4 For Multi Tenant Application

Lalita
May 3, 2020

In this tutorial I am going to show you how to implement tenant selection in Identity Server 4, in a multi tenant application. In many cases such tenant selection is necessary, especially in an Enterprise application. There are many ways to do multi tenancy in Identity Server 4. Here I am allowing the user to select the tenant. This could also be done in many other ways like, the tenant could be determined by the domain or subdomain name. Or the user could enter their tenant ID during login. The amount of variation you can get depends on your requirement. I will give you the scenario of this example. Suppose, you have an application where user the client can login to your application. The client then may have multiple companies under them, and after login the client may choose their company. Each company may have their own databases, so the client must choose which database they have access to. For this application we will be using .Net Core 3.1 and Identity Server 4.

First we need to implement an “AddAuthorizeInteractionResponseGenerator” which will allow extra interaction after the login is successful. For this create a helper class as follows.

``` cs
 public class AccountChooserResponseGenerator : AuthorizeInteractionResponseGenerator
    {
        public AccountChooserResponseGenerator(ISystemClock clock,
            ILogger<AuthorizeInteractionResponseGenerator> logger,
            IConsentService consent, IProfileService profile)
            : base(clock, logger, consent, profile)
        {
        }

        public override async Task<InteractionResponse> ProcessInteractionAsync(ValidatedAuthorizeRequest request, ConsentResponse consent = null)
        {
            {
                var response = await base.ProcessInteractionAsync(request, consent);
                if (response.IsConsent || response.IsLogin || response.IsError)
                    return response;

                if (!request.Subject.HasClaim(c => c.Type == "TenantId" && c.Value != "0"))
                    return new InteractionResponse
                    {
                        RedirectUrl = "/TenantSelection"
                    };

                return new InteractionResponse();

            }
        }
    }
```

In the above code after the login is successful we check if the Token has TokenId claims in it. If it doesn’t have TokenId in the claim then we redirect to “TenantSelection” page. You will also need to configure services. For this add the following code in the ConfigureServices method in Startup.cs

``` cs
// not recommended for production - you need to store your key material somewhere secure
builder
    .AddDeveloperSigningCredential()
    .AddAuthorizeInteractionResponseGenerator<AccountChooserResponseGenerator>();
```

We will also need cookies to store login state before the Tenant selection and add TenantId as scope. For this add the following code to Startup.cs.

``` cs
 services.AddAuthentication(options =>
            {
                options.DefaultScheme = "Cookies";
                options.DefaultChallengeScheme = "oidc";
            })
            .AddCookie("Cookies")
            .AddOpenIdConnect("oidc", options =>
                {
                    options.Authority = "http://localhost:5000";
                    options.RequireHttpsMetadata = false;
                    options.GetClaimsFromUserInfoEndpoint = true;

                    options.ClientId = "js";
                    options.SaveTokens = true;
                    options.Scope.Add("openid");
                    options.Scope.Add("profile");
                    options.Scope.Add("TenantId");
                });
```

You don’t need to actually add the OpenId part, so you can omit that if you want to. Now you need to implement ProfileService so you can add extra claims to your token. For this create a helper class as follows.

``` cs
 public class ProfileService : IProfileService
    {
        private readonly IUserClaimsPrincipalFactory<ApplicationUser> _claimsFactory;
        private readonly UserManager<ApplicationUser> _userManager;

        public ProfileService(UserManager<ApplicationUser> userManager, IUserClaimsPrincipalFactory<ApplicationUser> claimsFactory)
        {
            _userManager = userManager;
            _claimsFactory = claimsFactory;
        }

        public async Task GetProfileDataAsync(ProfileDataRequestContext context)
        {
            var sub = context.Subject.GetSubjectId();
            var user = await _userManager.FindByIdAsync(sub);
            var principal = await _claimsFactory.CreateAsync(user);
           
           //Get all the claims from the cookies
            var claims = principal.Claims.ToList();
           
          // Get the roles from the cookie
            var roles = claims.FindAll(c => c.Type == "role");

            claims = claims.Where(claim => context.RequestedClaimTypes.Contains(claim.Type)).ToList();

            // Add custom claims in token here based on user properties or any other source
            claims.Add(context.Subject.Claims.First(c => c.Type == "TenantId"));

           //Add roles if required
            claims.AddRange(roles);

            context.IssuedClaims = claims;
        }

        public async Task IsActiveAsync(IsActiveContext context)
        {
            var sub = context.Subject.GetSubjectId();
            var user = await _userManager.FindByIdAsync(sub);
            context.IsActive = user != null;
        }

    }
```

Now you need to register the ProfileService in the ConfigureServices method in Startup.cs. Add the following code there.

``` cs
  services.AddTransient<IProfileService, ProfileService>();
```

Lets create a simple view, where the user can select their Tenant. This will be the TenantSelection page. Create a Razor page view named TenantSelecton.

``` cs
@{
    ViewData["Title"] = "Index";
}

<h2>Index</h2>

<form method="post" action="/TenantSelection">
    
    <input type="Text"
           id="Tenant" name="Tenant" value=""><br>
 
    <button type="submit">Submit</button>
   
</form>
```

The above page is simple. We just create a input where we can type in the Tenant and submit the form. Then the Token will be generated with the Tenant name included. But in real project you will use get a list of Tenants from the database and then submit the chosen value. You can use the claims in the cookie generated after the successful login to authenticate the user and get the Tenant list from the database. Anyways we now need to create a controller where will post the Tenant info. For this create a controller called TenantSelectionController and create a TenantSelection POST method there as follows.

``` cs
 public class TenantSelectionController: Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Select(TenantModel model)
        {

            Uri uri = new Uri(Request.Headers["Referer"].ToString());
            string ReturnUrl = System.Web.HttpUtility.ParseQueryString(uri.Query)["returnUrl"];

            await HttpContext.SignInAsync(User.Claims.Single(r => r.Type == "sub").Value,
               new System.Security.Claims.Claim("TenantId", model.Tenant.ToString()));

            return Redirect(ReturnUrl);
        }
    }
```

In the above controller we sign in the user and add TenantId to the claims and redirect the user using the ReturnUrl. The Token thus generated will have the TenantId claim in it.

This is it we are done we have implemented tenant selection in Identity Server 4, we can now use the Tenant information to choose appropriate database if needed.

Thank you for reading. Good luck.

Lalita