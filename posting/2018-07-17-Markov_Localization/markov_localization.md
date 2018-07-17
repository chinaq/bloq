# Markov Localization


- [Markov Localization](#markov-localization)
    - [Localization Posterior](#localization-posterior)
        - [Tools](#tools)
        - [Bayes Rule](#bayes-rule)
        - [Variables](#variables)
        - [Apply Bayes Rule On Localization Posterior](#apply-bayes-rule-on-localization-posterior)
    - [To Simplify Motion Model](#to-simplify-motion-model)
        - [Total Probability for Motion Model](#total-probability-for-motion-model)
        - [Markov Assumption for Motion Model](#markov-assumption-for-motion-model)
        - [Recursive Structure of Motion Model](#recursive-structure-of-motion-model)
        - [Summary of Motion Model](#summary-of-motion-model)



## Localization Posterior
### Tools
- Bayes Rule 
- the Law of Total Probability
- the Markov Assumption

### Bayes Rule
- ![](./img/bayes_rule.png)
- ![](./img/bayes_rule_1.png)

### Variables
- ![](./img/variables.png)
- ![](./img/posterior_explanation.png)

### Apply Bayes Rule On Localization Posterior
- 定义后验方程
- Defination of Localization Posterior
    - ![](./img/def_posterior.png)
- Observation model & Motion model
    - ![](./img/models.png)
- Normalizer
    - ![](./img/normalizer.png)



## To Simplify Motion Model
### Total Probability for Motion Model
- 使得当前状态与上一状态相关
- ![](./img/total_probability.png)

### Markov Assumption for Motion Model
- 减少当前状态、上一状态的依赖项
- 目标
    - ![](./img/markov_target.png)
- 原理
    - ![](./img/markov_example.png)
- 结果
    - ![](./img/markov_result.png)

### Recursive Structure of Motion Model
- 使得当前状态几乎只于上一状态相关
- Simply bel(x(t-1))
    - ![](./img/simply_x_t-1.png)
- Recursive Structure
    - ![](./img/recursive_structure.png)
- Discrete Case
    - ![](./img/discrete_case.png)

### Summary of Motion Model
- ![](./img/sum_of_motion.png) 


