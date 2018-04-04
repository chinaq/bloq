---

layout:            post  
title:             "Hyperparameter Optimization"  
date:              2017-08-29 18:25:00 +0300  
tags:              ML
category:          Tech  
author:            Qiang  

---

## 缘起
- 郑尹杰：[Udacity-DLND-从第一个项目谈BP算法的超参数调整](https://zhuanlan.zhihu.com/p/28847218
)
- [使用Hyperopt自动选择超参数](https://mp.weixin.qq.com/s/-n-5Cp_hgkvdmsHGWEIpWw)
- 手动调参太累，让程序自己尝试



## 针对 DLND p2 图片分类

### 搜索的参数
- Batch size (64, 128, 256, 512, 1024)
- conv layers (1, 2, 3)
- conv thick (32, 256)
- full layer (1, 2, 3)
- full thick (32, 256)
- keep prob (0.3-0.9)
- 追加 learning rate (0.001-0.00001)

### 尝试的动作
- 手动设定 layers, thicks
- 随机选取 thicks
- 随机选取 layers, thicks
- 随机选取 layers，固定2倍 thicks
- 追加 随机选取 learning rate (以为最重要，结果无明显提升)

### 结果
- 基本都保持在 68-72
- 缺点：似乎无论怎么调都不会提升识别率
- 优点：自动选参保证了识别率不会过低

### 还有哪些参数没有尝试
- learning rate delay policy
- Batch Normalization type
- Pooling type
- Pooling window size
- conv striders size
- stimulate function type(relu, ...)



## 思考 - 接着该如何提高
- 初始化 weights，标准偏差采用 1/√n ，其中 n 为某一层输入单元数(input units) 
- cs231n 二次选取最优
- 读论文 Who is the best in CIFAR-10 ?



## cs231n 神经网络笔记3 内容列表：
- 梯度检查
- 合理性（Sanity）检查
- 检查学习过程
    - 损失函数
    - 训练与验证准确率
    - 权重：更新比例
    - 每层的激活数据与梯度分布
    - 可视化
- 参数更新
    - 一阶（随机梯度下降）方法，动量方法，Nesterov动量方法
    - 学习率退火
    - 二阶方法
    - 逐参数适应学习率方法（Adagrad，RMSProp）
- 超参数调优
- 评估
    - 模型集成
- 总结
- 拓展引用



## cs231n 神经网络笔记3 泛读

### 检查整个学习过程
- 以周期（epochs）为单位进行观测

#### 损失函数
- loss 体现出了 learning rate 的大小
- learning rate: the most important hyperpara `*****`
- ![](img/loss_and_learning_rate.png)

#### 训练集和验证集准确率
- 差距过大：过拟合，增大正则化强度（更强的L2权重惩罚，更多的随机失活等）或收集更多的数据
- 差距过小：模型容量还不够大，应该通过增加参数数量让模型容量更大些
- ![](img/accuracy.jpg)

#### 权重更新比例
- 对每个参数集的更新比例进行单独的计算和跟踪。
- 一个经验性的结论是这个比例应该在1e-3左右。
  - 如果更低，说明学习率可能太小
  - 如果更高，说明学习率可能太高

#### 每层的激活数据及梯度分布
- 对于使用tanh的神经元，我们应该看到激活数据的值在整个[-1,1]区间中都有分布。
- 如果看到神经元的输出全部是0，或者全都饱和了往-1和1上跑，那肯定就是有问题了

##### 第一层可视化
- 左图中的特征充满了噪音，这暗示了网络可能出现了问题：网络没有收敛，学习率设置不恰当，正则化惩罚的权重过低。
- 右图的特征不错，平滑，干净而且种类繁多，说明训练过程进行良好。
- ![](img/first_layer.png)

### 超参数调优
- 最常用的设置有：
    - 初始学习率
    - 学习率衰减方式（例如一个衰减常量）
    - 正则化强度（L2惩罚，随机失活强度）
- 实现：主程序调用仆程序，训练多个随机值
- 比起交叉验证最好使用一个验证集
- 超参数范围
    - 在对数尺度上进行超参数搜索。例如，一个典型的学习率应该看起来是这样：learning_rate = 10 ** uniform(-6, 1)
    - 但是有一些参数（比如随机失活）还是在原始尺度上进行搜索（例如：dropout=uniform(0,1)）
- 随机搜索优于网格搜索
    - ![](img/radom_search.png)
- 对于边界上的最优值要小心
    - 假设我们使用learning_rate = 10 ** uniform(-6,1)来进行搜索。一旦我们得到一个比较好的值，一定要确认你的值不是出于这个范围的边界上，不然你可能错过更好的其他搜索范围
- 从粗到细地分阶段搜索
    - 先进行初略范围（比如10 ** [-6, 1]）搜索，然后根据好的结果出现的地方，缩小范围进行搜索。进行粗搜索的时候，让模型训练一个周期就可以了
    - 第二个阶段就是对一个更小的范围进行搜索，这时可以让模型运行5个周期
    - 而最后一个阶段就在最终的范围内进行仔细搜索，运行很多次周期。
    - 贝叶斯超参数最优化
- 评估
    - 模型集成
        - 同一个模型，不同的初始化
        - 在交叉验证中发现最好的模型
        - 一个模型设置多个记录点
        - 在最终平滑区，平均最后几次的 weights
            - 这个“平滑”过的版本的权重总是能得到更少的误差。直观的理解就是目标函数是一个碗状的，你的网络在这个周围跳跃，所以对它们平均一下，就更可能跳到中心去。





## 参考
- [Udacity-DLND-从第一个项目谈BP算法的超参数调整](https://zhuanlan.zhihu.com/p/28847218
)
- [使用Hyperopt自动选择超参数](https://mp.weixin.qq.com/s/-n-5Cp_hgkvdmsHGWEIpWw)
- [Neural networks for algorithmic trading. Hyperparameters optimization（同上英文版）](https://medium.com/@alexrachnog/neural-networks-for-algorithmic-trading-hyperparameters-optimization-cb2b4a29b8ee)
- [Hyperopt](https://github.com/hyperopt/hyperopt/wiki/FMin)
- [Introduction to Hyperopt for Optimizing Neural Networks](https://github.com/Vooban/Hyperopt-Keras-CNN-CIFAR-100/blob/master/IntroductionToHyperopt.ipynb)
- [Hyperopt for solving CIFAR-100 with a convolutional neural network (CNN) built with Keras and TensorFlow, GPU backend]( https://github.com/Vooban/Hyperopt-Keras-CNN-CIFAR-100)
- [Who is the best in CIFAR-10 ?](http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html#43494641522d3130)
- [cs231n - Hyperparameter optimization 小节（random search）](http://cs231n.github.io/neural-networks-3/)
