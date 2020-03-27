# OAuth on React

## JS
- IdentityServer4 Example

## React
- react-oidc
- 使用 [`react-oidc-redux`](https://github.com/AxaGuilDEv/react-oidc/tree/master/packages/redux#readme) 主要问题是，各个包之间的依赖库问题，当前经多次尝试后，如下依赖可运行。

```
"dependencies": {
    ......
    "@axa-fr/react-oidc-redux": "^3.0.8",
    "@axa-fr/react-oidc-redux-fetch": "^3.0.8",
    "connected-react-router": "^5.0.1",
    "oidc-client": "1.8.2",
    "react": "16.8.6",
    "react-redux": "^5.0.7",
    "react-router": "^5.0.1",
    "redux": "^4.0.4",
    "redux-oidc": "^3.1.4",
    ......
  },
  "devDependencies": {
    ......
    "react-scripts": "~3.2.0",
    ......
  },
```

## V2
- 最终放弃了使用 react-oidc 主要是包冲突太严重了

### V2 的问题
- `docker` 内部局域网连接
  - 改用 [`host.docker.internal`](https://docs.docker.com/docker-for-mac/networking/)
  - 如果本主机也要同时连该地址，请在 host 中将 `host.docker.internal` DNS 为 `127.0.0.1`
- `oidc-client-js` 自动跳出登录
  - 在 `oidc-client-js` 的 `config` 中增加 `monitorSession: false`
    - [User signs out in Chrome after a few seconds](https://github.com/maxmantz/redux-oidc/issues/52#issuecomment-603308436)
  - 大概是因为 `monitorSession` 需要用到 `iframe`，当 `iframe` 被禁用时，无法会话便自动 `logout` 了
    - [JS认证和WebAPI - 灭蒙鸟](https://www.jianshu.com/p/fde63052a3a5)
- chrome 中登录后依然停留在了登录界面
  - cookie 跨域问题，因为 chrome 升级后，SameSite 设置为 none 时，必须基于 https 
  - 请设置 `app.UseCookiePolicy(new CookiePolicyOptions { MinimumSameSitePolicy = SameSiteMode.Lax });` 
    - [Identity server is keep showing “Showing login: User is not authenticated” in /connect/authorize/callback](https://stackoverflow.com/questions/51912757/identity-server-is-keep-showing-showing-login-user-is-not-authenticated-in-c)
    - [The Chromium Projects - SameSite Updates - Adding `SameSite=None; Secure` to your cookies?](https://www.chromium.org/updates/same-site)
