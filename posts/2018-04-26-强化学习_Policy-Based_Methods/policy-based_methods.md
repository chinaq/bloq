# 强化学习 Policy-Based Methods



- [强化学习 Policy-Based Methods](#policy-based-methods)
    - [Why Policy-Based Methods](#why-policy-based-methods)
    - [Policy Function Approximation](#policy-function-approximation)
        - [Linear Function with Softmax policy](#linear-function-with-softmax-policy)
        - [Linear Function with Gaussian policy](#linear-function-with-gaussian-policy)




## Why Policy-Based Methods
![](./img/why_policy-based_methods.png)

## Policy Function Approximation

### Linear Function with Softmax policy
![](./img/linear_function_with_softmax_policy.png)


### Linear Function with Gaussian policy
![](./img/linear_function_with_gaussian_policy.png)

- -> a gaussian distribution of action
- for Approximation, when action is right, set mu closer to action 

![](./img/gaussian_density.jpg)  
ref: Reinforcement Learning: An Introduction Second edition - 13.7 Policy Parameterization for Continuous Actions

![](./img/pg.png)  
ref: [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/)  
ref: [《强化学习》第七讲 策略梯度 - 高斯策略](https://zhuanlan.zhihu.com/p/28348110)
