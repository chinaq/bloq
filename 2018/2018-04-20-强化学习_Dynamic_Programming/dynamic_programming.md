# 强化学习 Dynamic Programming



- [强化学习 Dynamic Programming](#dynamic-programming)
    - [支持方法](#)
        - [Iterative Policy Evaluation](#iterative-policy-evaluation)
        - [Estimation of Action Values](#estimation-of-action-values)
        - [Policy Improvement](#policy-improvement)
    - [完整计算](#)
        - [Policy Iteration](#policy-iteration)
        - [Truncated Policy Iteration](#truncated-policy-iteration)
        - [Value Iteration](#value-iteration)
    - [reference](#reference)



## 支持方法

### Iterative Policy Evaluation
- 迭代策略评估：policy_now -> state-value

![](./img/iterative_policy.png)

### Estimation of Action Values
- 动作值估算： state-value -> action-value

![](./img/action_value.png)

### Policy Improvement
- 策略改进：(state-value, action-value) -> policy_new

![](./img/policy_improvement.png)



## 完整计算

### Policy Iteration
- 策略迭代：（policy_evalution, policy_improvement) -> policy

![](./img/policy_iteration.png)

### Truncated Policy Iteration
- 截断策略迭代：（truncated_policy_evalution, policy_improvement) -> policy
- 相比 policy iteration 仅多次循环，无需完全收敛即可更新 policy

![](./img/truncated_policy.png)
![](./img/truncate_policy_it.png)

### Value Iteration
- 价值迭代：policy_improvement -> policy 
- state-value 和 action-value 计算方程合而为一，几乎只需更新 state-value 即可获取 policy
- 相比 truncated policy iteration 每扫一次 state 即可更新 state-value

![](./img/value_iteration.png)



## reference
- [rl cheatsheet](./ref/cheatsheet.pdf)
- [Dynamic Programming - Explore FrozenLakeEnv](./ref/Dynamic_Programming_Solution.html)
- [dynamic_programming_summary](./ref/dynamic_programming_summary.png)