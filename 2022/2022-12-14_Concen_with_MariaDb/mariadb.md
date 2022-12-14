# Concen with MariaDb

- [Concen with MariaDb](#concen-with-mariadb)
    - [origin](#origin)
    - [app server - log async](#app-server---log-async)
    - [mariadb server - innodb\_log\_file\_size up](#mariadb-server---innodb_log_file_size-up)
    - [mariadb server - thread\_pool\_size, thread\_pool\_min\_threads up](#mariadb-server---thread_pool_size-thread_pool_min_threads-up)
    - [ref](#ref)

## origin
![origin](img/origin.png)
- 原始设置，尚未优化
- 大量数据超过 1s，部分超过 20s


## app server - log async
![log async](img/log-async.png)
- 将软件日志的写入，改为 async
- 规律性长时间响应


## mariadb server - innodb_log_file_size up
![log size up](img/log-size-up.png)
- 将数据库的 innodb_log_file_size 增大，保证不会发生 sync write
- 长时间响应间隔增大


## mariadb server - thread_pool_size, thread_pool_min_threads up
![thread pool up](img/thread-pool-up.png)
- 将数据库的的 thread_pool_size(unix), thread_pool_min_threads(windows) 增大
- 仅出现 4 次长时间响应，原因如下
    - new connections
    - new thread pools
    - write c disk
    - new thread pools


## ref
- [Thread Pool in MariaDB](https://mariadb.com/kb/en/thread-pool-in-mariadb/)
- [InnoDB Flushing: Theory and solutions](https://www.percona.com/blog/2011/04/04/innodb-flushing-theory-and-solutions/)
- [A graph a day, keeps the doctor away ! – MySQL Checkpoint Age](https://lefred.be/content/a-graph-a-day-keeps-the-doctor-away-mysql-checkpoint-age/)
- [Poorman’s MySQL monitoring/trending](https://lefred.be/content/poormans-mysql-monitoring-trending/)
- [MySQL Server Exporter](https://grafana.com/oss/prometheus/exporters/mysql-exporter/?tab=installation)
- [在Windows 如何安裝 mysql_exporter](https://opensource.dwins.com/?p=458)
