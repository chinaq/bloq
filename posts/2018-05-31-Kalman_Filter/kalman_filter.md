# Kalman Filter



### measurement update
- 使用当前测到的位置 z 和 当前预估的位置 H*x' ，重新确认当前更可信的位置 x

### predict
- 使用当前更可信的位置 x，预估下一可能位置 x'_next

### equation

![](./img/equation.png)

![](./img/cal.png)

- 状态
    - X：均值
    - P：协方差
- 包含的协方差
    - P：状态协方差
    - Q：状态转换协方差
    - R：测量协方差


## compare
--- | single variable | multi varible
--- | --- | --- 
区别 | 方差 | 协方差
mean | ![](./img/mu_single.png) | ![](./img/mu_multi.png)
diviation | ![](./img/diviation_single.png) | ![](./img/diviation_multi.png)
k | ![](./img/k_single.png) | ![](./img/k_multi.png) 

## ref
- [我所理解的卡尔曼滤波](https://www.jianshu.com/p/d3b1c3d307e0)