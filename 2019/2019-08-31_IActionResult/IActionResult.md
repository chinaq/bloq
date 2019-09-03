# `ActionResult<T>`

- `ActionResult<T>` offers the following benefits over the IActionResult type:
  - The `[ProducesResponseType]` attribute's Type property can be excluded. For example, `[ProducesResponseType(200, Type = typeof(Product))]` is simplified to `[ProducesResponseType(200)]`. The action's expected return type is instead inferred from the `T` in `ActionResult<T>`.
  - Implicit cast operators support the conversion of both `T` and `ActionResult` to `ActionResult<T>`. `T` converts to `ObjectResult`, which means return new `ObjectResult(T)`; is simplified to return `T`;.

- ref
  - [Controller action return types in ASP.NET Core Web API](https://docs.microsoft.com/en-us/aspnet/core/web-api/action-return-types?view=aspnetcore-2.2#actionresultt-type)
  - [IActionResult and ActionResult](https://exceptionnotfound.net/asp-net-core-demystified-action-results/)