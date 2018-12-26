# API Key要保护吗

1. 使用服务端代理，可以防止在客户端显示 api key
2. 但服务端仍是暴露的
3. 要保护服务端又成了递归保护 api
4. 如果不使用用户登录验证的，还是混淆较易
5. 混淆只能是尽力而为
6. 没有银弹

## 引用

- [Securing API Keys in a JavaScript Single Page App](http://billpatrianakos.me/blog/2016/02/15/securing-api-keys-in-a-javascript-single-page-app/)
- [PRACTICAL API PROTECTION WALKTHROUGH](https://www.approov.io/blog/practical-api-protection-walkthrough-part-1.html)
 