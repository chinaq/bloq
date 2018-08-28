---

layout:            post  
title:             "Softmax & Cross Entrophy Loss"  
date:              2017-09-03 18:25:00 +0300  
tags:              ML
category:          Tech  
author:            Qiang  

---

## softmax
- 非线性极大化最大值 
- 用于最后一层分类
- 非局部性，任一值改变，改变所有值比例
- 可搭配 log-likelihood 代价函数，或交叉熵代价函数
- 偏导后没有梯度下降减小的问题（未仔细研究偏导值）

## cross entrophy loss
- 衡量真实值的「出乎意料」程度
- 偏导为凸函数
- 如果最后一层激活函数为 sigmoid，交叉熵求导后，可以消除 sigmoid' ，此层梯度下降减小问题被大幅削弱了。

## 思考
- 以上两函数，必有缺点，待研究

## 参考
- [分类模型的 Loss 为什么使用 cross entropy](https://zhuanlan.zhihu.com/p/26268559)
- [改进神经网络的学习方式](https://hit-scir.gitbooks.io/neural-networks-and-deep-learning-zh_cn/content/chap3/c3s0.html)