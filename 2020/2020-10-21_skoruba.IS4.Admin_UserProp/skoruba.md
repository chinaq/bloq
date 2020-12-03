# Adding a tenant property for user in skoruba.is4.admin

## what

- 情况
  - 项目中使用 skoruba.is4.admin 作为 is4 的管理，当前需要支持多租户，最简法为添加一个 tenant 字段。
- 步骤
  - 添加字段
  - 使用 skoruba 的 ps1 脚本 add migration 
    - [IdentityServer4.Admin/build/add-migrations.ps1](https://github.com/skoruba/IdentityServer4.Admin/blob/master/build/add-migrations.ps1)
  - 项目中使用了大量的 IdentityUser 需要改为 UserIdentity
    - IdentityUser 是 IdentityUser 库的默认 User，不可修改属性
    - UserIdentity 是 skoruba 中定义的 User，可修改属性


## ref
- [Question about users enabled property - github](https://github.com/skoruba/IdentityServer4.Admin/issues/606)
- [Design-time DbContext Creation](https://docs.microsoft.com/en-us/ef/core/miscellaneous/cli/dbcontext-creation)
- [Using a Separate Migrations Project](https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/projects?tabs=dotnet-core-cli)