# 强化学习 Monte Carlo Methods



- [强化学习 Monte Carlo Methods](#monte-carlo-methods)
    - [支持方法](#)
        - [MC Prediction: State Values](#mc-prediction--state-values)
        - [MC Prediction: Action Values](#mc-prediction--action-values)
        - [Generalized Policy Iteration](#generalized-policy-iteration)
        - [MC Control: Incremental Mean](#mc-control--incremental-mean)
        - [MC Control: Policy Evaluation](#mc-control--policy-evaluation)
        - [MC Control: Policy Improvement](#mc-control--policy-improvement)
    - [完整计算](#)
        - [Exploration vs. Exploitation](#exploration-vs-exploitation)
        - [MC Control: Constant-alpha](#mc-control--constant-alpha)
    - [reference](#reference)

![](./img/result.png)

## 支持方法

### MC Prediction: State Values
- policy_now -> state-value

![](./img/mc-pred-state.png)


### MC Prediction: Action Values
- policy_now -> action-value

![](./img/mc-pred-action.png)

### Generalized Policy Iteration
- 本课程中学到的策略生成法都可视为GPI

### MC Control: Incremental Mean
- 使用平均数计算 value

### MC Control: Policy Evaluation
- 每个 episode 后，更新 value

### MC Control: Policy Improvement
- 使用 ϵ-greedy 更新 policy



## 完整计算

### Exploration vs. Exploitation
- 在探索和利用间平衡
- Greedy in the Limit with Infinite Exploration (GLIE)

![](./img/mc-control-glie.png)

### MC Control: Constant-alpha
- 使用 constant-α 设置最新数据的效用
- 相比原始 GLIE 可以更有效的利用新回馈数据

![](./img/mc-control-constant-a.png)



## reference
- [Monte Carlo Methods - Explore BlackjackEnv](./ref/Monte_Carlo_Solution.html)
- [Monte_Carlo_Methods_summary](./ref/monte_carlo_methods_summary.png)



