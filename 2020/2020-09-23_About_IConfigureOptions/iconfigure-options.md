

Set all kinds of IOptions

Every IConfigureOptions Stayed in the List


## 最简
- 依照常规，从最简单的开始
- 第一

## 加载
- `services.AddOptions()` 做了什么
    - 加载了一堆 IOptions 的实现，我们只关注 `IOptionsMonitor<TOptions>`，默认使用了 `OptionsMonitor<TOptions>` 实现
- `service.AddOptions().Configure<TOptions>` 做了什么
    - 加载了 `IConfigureNamedOptions` 的默认实现 `ConfigureNamedOptions`

## 调用

![ioptions](./img/ioptions.jpeg)
