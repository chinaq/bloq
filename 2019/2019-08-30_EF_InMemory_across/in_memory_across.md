# InMemoryDatabase Across

- [In-memory database not persisted across service providers](https://github.com/aspnet/EntityFrameworkCore/issues/9613#issuecomment-430722420)
- Note for others finding this issue. There are two ways to resolve this:
    - Either pass a `InMemoryDatabaseRoot` object to `UseInMemoryDatabase` --see below
    - Or ensure the context instance is created the same way in each place so that the same internal service provider is used everywhere

``` cs
// setting
public static readonly InMemoryDatabaseRoot InMemoryDatabaseRoot = new InMemoryDatabaseRoot();
```

``` cs
// using
var options = new DbContextOptionsBuilder<MeterContext>()
    .UseInMemoryDatabase(databaseName: "test", InMemoryDatabaseRoot)
    .Options;
var context = new MeterContext(options);
```
