# 便利化aws

- [便利化aws](#%E4%BE%BF%E5%88%A9%E5%8C%96aws)
    - [启停](#%E5%90%AF%E5%81%9C)
    - [tmux](#tmux)
    - [vs code 结合 rmate](#vs-code-%E7%BB%93%E5%90%88-rmate)



## 启停
- 使用 fastai 提供的 [script](https://github.com/fastai/courses/blob/master/setup/aws-alias.sh)（基于 [aws-cli](https://amazonaws-china.com/cn/cli/)）可快速启停 aws

## tmux
- 利用 tmux 可以快速恢复 command line 窗口
- 参考
    - [Linux下终端利器tmux](http://kumu-linux.github.io/blog/2013/08/06/tmux/)

## vs code 结合 rmate
- 使用 `Remote VSCode` 插件可在本地编辑远程文件
- 设置方法：
    - 本地安装 `Remote VSCode` 插件
    - 确保本地 `vs code` 中 `Remote: Start Server` 已自动运行
    - 在服务端安装 `rmate`，首推 `pip install rmate`
- 运行
    - `vs code` 中的 `command line` 运行 `ssh -R 52698:127.0.0.1:52698 user@example.org`，连接到服务端
    - 服务端运行 `rmate -p 52698 file`，本地 `vs code` 中显示文件

- 参考
    - [Remote VSCode](https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode)
    - [Remote Editing using VS Code](https://blog.technologee.co.uk/remote-editing-using-vs-code/)