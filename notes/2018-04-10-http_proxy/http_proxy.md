# http_proxy

## windows 中的系统代理

- 大多 GUI 软件，或默认使用系统代理，或可单独配置
- command line 大多不使用系统代理
    - PowerShell: 默认使用
    - cmd: 不使用
    - git bash: 不使用
    - 可以使用 `curl google.com` 测试
- 由于 command line 应用，大多使用 `set http_proxy=http://127.0.0.1:1080` 环境变量进行代理，可按此设置
- git bash 配置快捷如下:

``` bash
alias proxy-on='export http_proxy=http://127.0.0.1:1080 https_proxy=https://127.0.0.1:1080'
alias proxy-off='unset http_proxy https_proxy'
alias proxy-show='printenv | grep proxy'
```

- 参考
    - [http_proxy 了解](http://www.cnblogs.com/yi88/articles/6567517.html)
    - [Command Line Tutorials – Curl](https://quickleft.com/blog/command-line-tutorials-curl/)
    - [set HTTP_PROXY doesnt' work in PowerShell](https://sites.google.com/site/softwaretechforge/Downhome/Programminglanguage/sethttpproxydoesntworkinpowershell)
    - cmd 本可使用 doskey，但是 win10 有问题，就算了
        - [doskey in Windows is just like alias in Linux](https://www.jamescoyle.net/how-to/1100-doskey-in-windows-is-just-like-alias-in-linux)
        - [gist - bashrc.bat](https://gist.github.com/zhiguangwang/c15f944f590cafd7232bca61d2b4642b)

## mac 

- 不同点， ss软件只有 socks5 代理，所以使用 `export ALL_PROXY=socks5://127.0.0.1:1080` 进行设置
- 参考
    - [让 Homebrew 走代理更新](https://www.logcg.com/archives/1617.html)