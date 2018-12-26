# 小米 IoT 的 ios-rn-sdk 坑

## Create

    进入 MiHomePluginSDK 所在目录，运行 createPlugin 脚本创建一个新的本地扩展程序包：

    ./createPlugin plugin_name

    其中 plugin_name 即为之前申请创建的扩展程序包名 com.aaa.bbb.ios

这里小坑，`./createPlugin` 是 python2 代码

## Run

    进入 MiHomePluginSDK 所在目录，启动 node 服务器：

    npm start --reset-cache

此坑为，运行前本机需安装 [`watchman`](http://facebook.github.io/watchman/)，否则报错。（为毛用 `watchman` ，不用的话 windows 都可以跑了，何必 mac 呢。不过无论怎样，mi 的文档比 ali 好多了，后者能折磨死你）

---

## 附带写个 [expo](https://expo.io/) 坑
- 参考
    - [愚蠢的Expo / CRNA不会挑选合适的网络](https://segmentfault.com/a/1190000013108816)