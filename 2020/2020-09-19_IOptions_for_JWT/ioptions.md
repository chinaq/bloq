# IOptions 在 JwtBearOptions 中的应用

- [IOptions 在 JwtBearOptions 中的应用](#ioptions-在-jwtbearoptions-中的应用)
  - [目标](#目标)
  - [默认实现](#默认实现)
    - [调用链](#调用链)
    - [加载链](#加载链)
  - [实现说明](#实现说明)
    - [两个个关键点](#两个个关键点)
    - [默认加载](#默认加载)
  - [文章中的修改](#文章中的修改)

## 目标
- 我们需要在 token 中检测到 Tenant


## 默认实现

### 调用链
``` cs
AuthenticationMiddleware
    -> JwtBearerHandler
        -> IOptionsMonitor
            -> IOptionsFactory
                -> IConfigureOptions
```

### 加载链
``` cs
[using Microsoft.Extensions.DependencyInjection - asp.net core]
AddJwtBear 
       [Microsoft.AspNetCore.Authentication - asp.net core]
    -> builder.AddScheme<JwtBearerOptions, JwtBearerHandler>(authenticationScheme, displayName, configureOptions);
           [using Microsoft.Extensions.DependencyInjection -  run time] 
        -> Services.Configure<AuthenticationOptions> 
               [using Microsoft.Extensions.DependencyInjection - run time]
            -> services.AddOptions();
               services.AddSingleton<IConfigureOptions<TOptions>>(new ConfigureNamedOptions<TOptions>(name, configureOptions)); 
```

## 实现说明
### 两个个关键点
- IConfigureOptions
    - 默认以 `new ConfigureNamedOptions<TOptions>(name, configureOptions)` 实现，每次调用会生成新 `TOptions` 即 `configureOptions` 即当前验证相关设定项。
- IOptionsMonitor
    - 默认 `OptionsMonitor<>` 实现，使用 `optionsFactory` 调用 `IConfigureOptions` 生成 `TOptions`，再放入缓存避免每次重新生成 `TOptions`

### 默认加载
- IConfigureOptions
``` cs
services.AddSingleton<IConfigureOptions<TOptions>>(new ConfigureNamedOptions<TOptions>(name, configureOptions)); 
```

- IOptionsMonitor
``` cs 
public static IServiceCollection AddOptions(this IServiceCollection services)
{
    if (services == null)
    {
        throw new ArgumentNullException(nameof(services));
    }

    services.TryAdd(ServiceDescriptor.Singleton(typeof(IOptions<>), typeof(OptionsManager<>)));
    services.TryAdd(ServiceDescriptor.Scoped(typeof(IOptionsSnapshot<>), typeof(OptionsManager<>)));
    services.TryAdd(ServiceDescriptor.Singleton(typeof(IOptionsMonitor<>), typeof(OptionsMonitor<>)));
    services.TryAdd(ServiceDescriptor.Transient(typeof(IOptionsFactory<>), typeof(OptionsFactory<>)));
    services.TryAdd(ServiceDescriptor.Singleton(typeof(IOptionsMonitorCache<>), typeof(OptionsCache<>)));
    return services;
}
``` 

## 文章中的修改
- IConfigureOptions
  - 修改 TOptions 中的 Authority，确保 token 颁发者和 API 认定的 Authority 相同
- IOptionsMonitor
  - 缓存 TOptions 不再仅使用 SchemeName，而是以 SchemeName+Tenant 为Key，保存 TOptions，这样每个 Tenant 都会独立存储 Authority
