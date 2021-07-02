# 关于 ABP 中的 Unit Of Work 的问题

## abp 中的 uow 简介
- [Unit of Work](https://docs.abp.io/en/abp/latest/Unit-Of-Work)
- 原则
  - 以下方法，当方法未指定 uow 时，将自动启动
    - asp.net controller actions
    - applicaion service methods
    - repo methods
  - 当需要指定新 uow 时
    - 继承 IUnitOfWorkEnabled 或使用 `[UnitOfWork]` 属性
    - 大多情况需要 virtual 方法
  - 手动指定的 uow 属性的运行情况
    - 当没有 uow 时，将新建
    - 当在 uow 环境中时，将使用现有 uow
  - 另可使用 IUnitOfWorkManager 手动新建 uow 的 Scope

## 问题一：丢失 DbContext
- 情况
  - 当调用 `repo.WithDetailsAsync()` 等方法时会出现如下的情况
- 错误
  ```
  Error Message:

  System.ObjectDisposedException : Cannot access a disposed context instance. A common cause of this error is disposing a context instance that was resolved from dependency injection and then later trying to use the same context instance elsewhere in your application. This may occur if you are calling 'Dispose' on the context instance, or wrapping it in a using statement. If you are using dependency injection, you should let the dependency injection container take care of disposing context instances.

  Object name: 'XyzDbContext'.
  ```
- 猜测
  - uow 基于同一 DbContext
  - repo 的默认方法，会自动使用 uow，便可获取到 DbContext
  - 但 WithDetailsAsync 之类的方法，并没有使用 uow，便无法得到 uow
- 解决
  - 使当前的调用包含在 uow 中
    - 添加 `[UnitOfWork]` 属性
    - 或
    - 包含在 `_unitOfWorkManager.Begin()` 中

## 问题二：未 Update 子属性
- 情况
  - 当使用 repo.UpdateAsync 时，并没有升级子属性表
- 分析
  - 当 select repo 和 update repo 不在同一 uow 时，单个 repo 的 update 仅追踪当前的 entity 而忽略 children entity
- 解决
  - 使其包含在同一 uow
