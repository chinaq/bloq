# Abp Exceptions

- [Abp Exceptions](#abp-exceptions)
    - [问题 - Tenant not Found!](#问题---tenant-not-found)
    - [asp.net 的 exceptions 机制](#aspnet-的-exceptions-机制)
        - [ExceptionHandlerMiddleware](#exceptionhandlermiddleware)
        - [IAsyncExceptionFilter](#iasyncexceptionfilter)
    - [abp 的exceptions 机制](#abp-的exceptions-机制)
    - [Angular 端的处理](#angular-端的处理)

## 问题 - Tenant not Found!

## asp.net 的 exceptions 机制
### ExceptionHandlerMiddleware
- ExceptionHandlerMiddleware
    ```
    ExceptionHandlerMiddleware 
        -> (ExcepionHandlerOperion.ExceptionHandler ?? next)
    ```
    - 如果抓到 exception，修改 context 中的各状态参数，之后两种方案
        - 如果指定 ExcepionHandlerOperion.ExceptionHandler，则调用
        - 如果未指定，则继续 next
### IAsyncExceptionFilter
- 附属于 EndPointMiddleware，仅处理 Controller 的错误
- IAsyncExceptionFilter
    ```
    DefaultActionDescriptorCollectionProvider 
        -> ControllerActionDescriptorProvider
            -> 
    ```
    
    ```cs
    internal sealed class EndpointMiddleware {
        ......
        public Task Invoke(HttpContext httpContext) {
            var endpoint = httpContext.GetEndpoint();
            ......
            var requestTask = endpoint.RequestDelegate(httpContext);
            ......
        }
        ......
    }
    ```


    ``` cs
    public static class MvcCoreServiceCollectionExtensions {
        ......
        // To enable unit testing
        internal static void AddMvcCoreServices(IServiceCollection services)
        {
            ......
            services.TryAddEnumerable(ServiceDescriptor.Transient<IActionDescriptorProvider, ControllerActionDescriptorProvider>());
            services.TryAddSingleton<IActionDescriptorCollectionProvider, DefaultActionDescriptorCollectionProvider>();
            .....
        }
        ......
    }
    ```

## abp 的exceptions 机制
- 仅注入了 `IAsyncExceptionFilter` 的实现

## Angular 端的处理
- [Tenant Not Found Error (Http 500) #9417](https://github.com/abpframework/abp/issues/9417)