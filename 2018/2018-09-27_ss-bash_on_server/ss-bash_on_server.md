# ss-bash on server

```
用法：
    显示版本：
        ssadmin.sh -v|v|version
    显示帮助：
        ssadmin.sh [-h|h|help]
    启动ss:
        ssadmin.sh start
    停止ss：
        ssadmin.sh stop
    查看ss状态：
        ssadmin.sh status
    重启ss：
        ssadmin.sh restart
    软重启ss：
        ssadmin.sh soft_restart
        在不影响现有连接的情况下重启ss服务。用于ss服务参数修改，
        和手动直接修改配置文件后，重启ss服务。
    添加用户：
        ssadmin.sh add port passwd limit
            port：端口号, 0<port<=65535
            passwd：密码, 不能有空格，引号等字符
            limit：流量限制，可以用K/M/G/T、KB/MB/GB/TB等（不区
                   分大小写）。支持小数。比如10.5G、10.5GB等。
                   1KB=1024 bytes，以此类推。
        示例： ssadmin.sh add 3333 abcde 10.5G

    ......
```

- install 
    - apt install python python-pip
    - git clone [ss-bash](https://github.com/hellofwy/ss-bash)
- run
    - ss-bash create users
    - ./ssadmin start 
- cron
    - clean data monthly
        - [请问怎么设置每月自动重置流量信息？](https://github.com/hellofwy/ss-bash/issues/42)
        - [crontab 定时任务]( https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)
- problem on ubuntu 18
    - [Kali2.0 update到最新版本后安装shadowsocks服务报错问题](https://blog.csdn.net/blackfrog_unique/article/details/60320737)

## 补充
- 在 `crontab` 中设置自动重置流量的一些问题
  - 由于 `crontab` 运行时不与 `shell`发生关系，不会加载 `.bashrc` 之类的文件，导致无法获取 `PATH` ，便无法启动 `ssserver`
  - 尝试直接引入 `. ~/.bashrc ` 失败，因为文件中使用了 `sh` 中的命令 `shopt`
  - 所以直接加载环境变量 `export PATH=/usr/local/bin:$PATH` ，可行