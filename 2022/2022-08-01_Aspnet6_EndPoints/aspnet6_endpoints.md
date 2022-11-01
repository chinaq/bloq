# Asp.Net 6 Endpoints

- WebApplication 继承了 IEndpointRouteBuilder，则 `ICollection<EndpointDataSource> DataSources` 包含在内
- 下一段中的 `// reset route builder if it existed, this is needed for StartupFilters` 是意味着某些 `StartFilter` 会在内部调用 `UseRouting()` 吗？
  ``` cs
    // WebApplicationBuilder.cs

    private void ConfigureApplication(WebHostBuilderContext context, IApplicationBuilder app)
    {
        Debug.Assert(_builtApplication is not null);

        // UseRouting called before WebApplication such as in a StartupFilter
        // lets remove the property and reset it at the end so we don't mess with the routes in the filter
        if (app.Properties.TryGetValue(EndpointRouteBuilderKey, out var priorRouteBuilder))
        {
            app.Properties.Remove(EndpointRouteBuilderKey);
        }

        if (context.HostingEnvironment.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }

        // Wrap the entire destination pipeline in UseRouting() and UseEndpoints(), essentially:
        // destination.UseRouting()
        // destination.Run(source)
        // destination.UseEndpoints()

        // Set the route builder so that UseRouting will use the WebApplication as the IEndpointRouteBuilder for route matching
        app.Properties.Add(WebApplication.GlobalEndpointRouteBuilderKey, _builtApplication);

        // Only call UseRouting() if there are endpoints configured and UseRouting() wasn't called on the global route builder already
        if (_builtApplication.DataSources.Count > 0)
        {
            // If this is set, someone called UseRouting() when a global route builder was already set
            if (!_builtApplication.Properties.TryGetValue(EndpointRouteBuilderKey, out var localRouteBuilder))
            {
                app.UseRouting();
            }
            else
            {
                // UseEndpoints will be looking for the RouteBuilder so make sure it's set
                app.Properties[EndpointRouteBuilderKey] = localRouteBuilder;
            }
        }

        // Wire the source pipeline to run in the destination pipeline
        app.Use(next =>
        {
            _builtApplication.Run(next);
            return _builtApplication.BuildRequestDelegate();
        });

        if (_builtApplication.DataSources.Count > 0)
        {
            // We don't know if user code called UseEndpoints(), so we will call it just in case, UseEndpoints() will ignore duplicate DataSources
            app.UseEndpoints(_ => { });
        }

        // Copy the properties to the destination app builder
        foreach (var item in _builtApplication.Properties)
        {
            app.Properties[item.Key] = item.Value;
        }

        // Remove the route builder to clean up the properties, we're done adding routes to the pipeline
        app.Properties.Remove(WebApplication.GlobalEndpointRouteBuilderKey);

        // reset route builder if it existed, this is needed for StartupFilters
        if (priorRouteBuilder is not null)
        {
            app.Properties[EndpointRouteBuilderKey] = priorRouteBuilder;
        }
    }
  ```
