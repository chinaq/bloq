# Tcp Application Problems

## 项目：
Tcp 服务端接收软件，在高峰时会连接超时，客户端在 10 秒内接收不到响应会断开。

## 设施
- iot 设备 2k台
- 接收服务器 - linux
    - 性能监控
        - netdata
    - 接收软件日志
        - logdashboard 网页显示
        - hangfire 定期清理
- 数据库服务器 - windows
    - 性能监控
        - Grafana
        - Prometheus

## 排错流程
- 问题一：MySql 读写慢，原因未知
    - 推测：建立大量 sql 连接，导致超时
    - 措施：切换至 MariaDb 后一切正常
- 问题二：仍有少量的超时错误，推测接收服务器负载问题
    - 观测：使用 netdata 监控，发现硬盘负载较高，
    - 推测：和日志有关，因最初使用 logdashboar 配合 serilog 的 txt 方式并无该现象，后续改为 nlog 的 sqlite 出现该问题，是否被写日志阻塞？
- 后续：尝试使用 serilog 的 mysql 改进
    - 见 [Concen with MariaDb](../2022-12-14_Concen_with_MariaDb/mariadb.md)
