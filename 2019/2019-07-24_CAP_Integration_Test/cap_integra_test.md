# Cap Integration Test

![cap](img/cap.png)

## Use in Memory Queue in a memory start up file
``` cs
public void ConfigureServices(IServiceCollection services)
{
    services.AddCap(x =>
    {
        x.UseInMemoryStorage();
        x.UseInMemoryMessageQueue();
    });
}
```

## run publish from services in test
``` cs
    var capBus = factory
        .Server
        .Host
        .Services
        .GetService(typeof(ICapPublisher))
        as ICapPublisher;

    await capBus.PublishAsync(
        nameof(NBMeterDataArrivedIntegrationEvent),
        @event);
```

## ref
- [快速开始 - CAP](http://cap.dotnetcore.xyz/user-guide/zh/getting-started/quick-start/)
- [Integration tests in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-2.2)