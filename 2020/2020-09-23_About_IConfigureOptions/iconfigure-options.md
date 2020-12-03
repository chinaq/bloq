# IOptions 和 IConfigureOptions

## 加载
- `services.AddOptions()` 做了什么
    - 加载了一堆 `IOptions` 的实现
    - 我们只关注 `IOptionsMonitor<TOptions>`，默认使用了 `OptionsMonitor<TOptions>`的实现
- `service.AddOptions().Configure<TOptions>` 做了什么
    - 加载了 `IConfigureNamedOptions<TOptions>` 的默认实现 `ConfigureNamedOptions<TOptions>`

## 调用
![ioptions](./img/ioptions.jpeg)
