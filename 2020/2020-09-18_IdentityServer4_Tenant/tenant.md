# Options of JWT on ASP.NET

- [Options of JWT on ASP.NET](#options-of-jwt-on-aspnet)
  - [起因](#起因)
  - [备份](#备份)
  - [内容确认](#内容确认)
    - [验证](#验证)
    - [颁发](#颁发)
    - [关于 IdentityServer4](#关于-identityserver4)
    - [颁发 token 流程](#颁发-token-流程)
  - [开始动手](#开始动手)
    - [前提](#前提)
    - [重写 Identity Server](#重写-identity-server)
    - [两个主要点](#两个主要点)
    - [原 Profile Service](#原-profile-service)
      - [修改 Client](#修改-client)
      - [修改 API 端](#修改-api-端)

## 起因
因为需要为某一项目设置多租户，参考各类文章后，决定采用 xxx 一文，进行学习并设置。你肯定打不开连接。。。。。。这事够神奇的。几天前搜索了一下多租户的相关文章，目标希望和 IdentityServer4 相结合，确定了此篇为主要学习对象。之后去完成了手上的其他一些工作，等在回来后，404 了。。。。。。，更绝的是，除了文章本来还有配套的 github 库和 youtube 视频，全部消失了消失了消失了，也不知到是什么原因导致。所以当时只能再找出路，但 google 了半天没有满意的文章。灵感大王一道，为什么不用网页快照？瞬间回来了，除了图片没有缓存、CSS 消失外，内容基本都可以看清了，呼。接着是 github 库，直接 google 库名，可以找到缓存页，但这就没什么鸟用了，我要的是库，不是页面。再次感谢伟大的 github fork，居然有某位大神 fork 过之前的库，于是我 fork 再 fork。这下就只剩视频了，没办法只好放弃。基本是心满意足了。

## 备份
- 原文已备份在本文 ref 文件夹中
- repo
  - [IdentityServerTenantSelection](https://github.com/chinaq/IdentityServerTenantSelection)
  - [IdentityServerSubdomainMultiTenant](https://github.com/chinaq/IdentityServerSubdomainMultiTenant)

## 内容确认
### 验证
- Tenant 包含在如下几个部分中
  - 用户数据库
  - IS4 HOST 地址中包含的 Tenant
  - HTTP Request 中的 Tenant 字段
- 登录时
  - 需要用户数据库和 Request 中的 Tenant 一致
- AuthenticationEndPoint 
  - 需要确保用户存在，其 claim 和 Request 中的 Tenant 也一致
- HOST 地址似乎没有用到，但是 ISSUER 的值会指定为这个地址

### 颁发
- 颁发的 token 中包含 Tenant 即可

### 关于 IdentityServer4 
- 首先，确认 IdentityServer4 的模版结构
  - 注册部分
    - 添加 IdentityServer，这会注册一系列新的 EndPoints 用于授权 token
  - 使用部分
    - 使用 EndPoints 必然是在原routing 之前，因为他有自己的路由
    - 也在 Authentication 之前，因为到达 EndPoints 之后，会主动检验是否需要登录
  
### 颁发 token 流程
  - Client 导向 IdentityServer4 对 Auth End Points
    - 由于未登录，重定向
  - Account
    - 用户登录
  - AuthenticationEndpoint
    - 验证下用户是否有效
    - 颁发 claims 中包含 Tenant

## 开始动手

### 前提
- 以 Identity Server 4 的 example 为例子
- 简方案，只需重新实现这一接口即可完成对 claims 中的 Tenant 赋值。

### 重写 Identity Server
``` cs
// AuthorizeResponseGenerator
// 先确认用户是不是需要登录或授权等
:AuthorizeEndPoint -> :AuthorizeInteractionResponseGenerator

// ProfileService
// 通过授权后，响应 claims
:AuthorizeEndPoint -> :AuthorizeResponseGenerator -> :DefaultTokenService -> :DefaultClaimService -> :ProfileService
```

### 两个主要点
- IProfile 主要处理两件事
   - 确定当前用户是否已登录并验证通过
   - 为 IdentityServer4 服务颁发 claims 

- Login 页面也需要确认 Tenant 是否正确
  - AuthenticationRequest 将解析 acr_values


### 原 Profile Service
- 可以先看一下原 Profile 的内容
  - 确定 tenant 和用户记录的 tenant 相对应
  - 添加 tenant 到 claims

#### 修改 Client

- 确定 JS client 中的 acr_values 为对应 tenant 即可
  - acr_values 中指定tenant
  - authority 中指定 url 包含 tenant

#### 修改 API 端
- 最简
  - 去除对 Issuer (即 Authority）的验证
    - 因为默认情况下，生成 token 的 claims 时，指定 Issuer 为请求 Auth 的地址
  - 另，也要去除 aud 的验证，默认 API Scope 不生成 aud
- 进一步
  - 为每个 tenant 匹配相应 ISSUER
    - 修改 IConfigureNamedOptions，使 JwtBearedOptions 中的 Authority 动态生成



