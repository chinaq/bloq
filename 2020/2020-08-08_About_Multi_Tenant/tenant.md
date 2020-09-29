# IdentityServer4 Multi-tenant 多租户系列

- [IdentityServer4 Multi-tenant 多租户系列](#identityserver4-multi-tenant-多租户系列)
  - [问题](#问题)
  - [预期内容](#预期内容)
  - [项目](#项目)
    - [多域名](#多域名)
    - [多租户](#多租户)
    - [Finbuckle](#finbuckle)

## 问题
- 某天老王告诉我，我们当前提供给客户的程序啊，都是要一给一，每次新客户需要服务了，我们就部署一个新的站点给客户，代码什么的基本都是再复制一份，这都是什么鬼啊。你懂不懂点软件工程啊。“你行你来，来来来”。话虽如此，当然知错要能改，但基本也就是虚心接受屡教不改。
- 面临这样的问题，第一考虑，也基本是唯一考虑，就是使用多租户系统来解决。由于当前系统使用的微服务的架构，那么需要两者的结合。
- 当前我们关且仅关心，验证和授权部分。所以祭出的终极方案是，在 IdentityServer4 中实现多租户。

## 预期内容
- 多域名
    - 第一步，其他什么都不管，只是让 SPA 可以支持多个域名
- 多租户
    - API 识别出请求的用户和租户
- Finbuckle
    - API 利用 Finbuckle 框架处理数据

## 项目
- 地址 - [IdentityThings](https://github.com/chinaq/IdentityThings)

### 多域名
- 直接使用 IdentityServer4 的例子，将其改为多域名支持
- 基本只需要将不同 URL 指向同一 IP 即可
- 然后，在 IdentityServer4 中支持多个 CORS 请求即可

### 多租户
- 上接多域名项目
- 直接 IdentityServer4 中，修改 ProfileService 增加 tenant

### Finbuckle
- 上接多租户项目
- 在 API 中使用 Finbuckle
