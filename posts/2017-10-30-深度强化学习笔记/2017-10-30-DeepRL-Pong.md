---

layout:            post  
title:             "Deep Reinforcement Learning: Pong from Pixels Note"  
tags:              ML
category:          Tech  
author:            Qiang  

---

<!-- TOC -->

- [1. Pong from pixels（基于像素的乒乓）](#1-pong-from-pixels基于像素的乒乓)
    - [1.1. Policy network （策略网络）](#11-policy-network-策略网络)
    - [1.2. It sounds kind of impossible.（不现实?）](#12-it-sounds-kind-of-impossible不现实)
    - [1.3. Supervised Learning.（监督学习）](#13-supervised-learning监督学习)
    - [1.4. Policy Gradients.（策略梯度）](#14-policy-gradients策略梯度)
    - [1.5. Training protocol. （训练准则）](#15-training-protocol-训练准则)
    - [1.6. alternative view. （另一种视角）](#16-alternative-view-另一种视角)
    - [1.7. More general advantage functions.(回报)](#17-more-general-advantage-functions回报)
    - [1.8. Deriving Policy Gradients.（策略梯度推导）](#18-deriving-policy-gradients策略梯度推导)
    - [1.9. Learning.（真正的学习代码）](#19-learning真正的学习代码)
    - [1.10. Learned weights. （权重都学了什么）](#110-learned-weights-权重都学了什么)
- [2. What isn't happening （发生了什么）](#2-what-isnt-happening-发生了什么)
- [3. Non-differentiable computation in Neural Networks （不可微计算)](#3-non-differentiable-computation-in-neural-networks-不可微计算)
- [4. Conclustions （结论）](#4-conclustions-结论)
- [5. 参考](#5-参考)

<!-- /TOC -->

# 1. Pong from pixels（基于像素的乒乓）
img -> action  
![pong](img/pong.png)

## 1.1. Policy network （策略网络）
![policy](img/policy.png)  
一个2层神经网络，输入为游戏像素(`210*160*3`)，输出为“上移”动作概率。  
`X1*W1 -> X2*W2 -> sigmoid -> Logistic Loss`

## 1.2. It sounds kind of impossible.（不现实?）
困难在哪里，如果一局赢了，那么你怎么知道哪一步好，哪一步差？

## 1.3. Supervised Learning.（监督学习）
![sl](img/sl.png)  
目标为向上，即输出 1。当前输出为 0.3，对数概率(log probabilities)为 -1.2=ln(0.3), -0.36=ln(0.7)

## 1.4. Policy Gradients.（策略梯度）
![rl](img/rl.png)  
在强化学习中我们并没有正确的标签信息，没关系，我们可以等着瞧!比如在乒乓游戏中，我们可以等到游戏结束，获得游戏的回报(胜：+1;负：-1)，再对我们所执行过的动作赋予梯度(DOWN)(Monte Carlo Search)。

## 1.5. Training protocol. （训练准则）
![](img/episodes.png)  
**训练过程**:假设每一次游戏包含200帧画面，那么我们一共作了20,000次UP/DOWN的决策。假设我们赢了12局，输了88局，那么我们将对于那些胜局中200\*12=2400个决策进行正向更新(positive update，为相应的动作赋予+1.0的梯度，并反向传播，更新参数);而对败局中200*88=17600个决策进行负向更新。于是，我们可以使用改进之后的策略网络再玩100局，循环往复。  
**解决不知哪一步好**：如果你考虑上百万次游戏过程，一个正确的动作给你带来胜利的概率仍然是更大的，也就意味着你将会观察到更多的正向更新，从而使得你的策略依然会朝着正确的方向改进。

## 1.6. alternative view. （另一种视角）
Policy Gradients 与监督学习是相通的，只有两个小小的修改

- 使用了假标签 y（依据最终的回报给予 1 或 -1）
- 使用最终的回报修正 损失函数（例如：当正向回报非常大时，说明往该方向行动是正确的，那么倍增损失，使用权重以更大的步伐往该方向调整）

## 1.7. More general advantage functions.(回报)
回报可使用 discount 因子

## 1.8. Deriving Policy Gradients.（策略梯度推导）
梯度策略的推导，看不懂

## 1.9. Learning.（真正的学习代码）
最后的学习代码 130 行而已。

``` python
""" Trains an agent with (stochastic) Policy Gradients on Pong. Uses OpenAI Gym. """
import numpy as np
import cPickle as pickle
import gym

# 超参
H = 200 # 神经元数
batch_size = 10 # 每个 batch 运行多少轮游戏
learning_rate = 1e-4
gamma = 0.99 
decay_rate = 0.99 # decay factor for RMSProp leaky sum of grad^2
resume = False # 继续之前的记录
render = False

# 初始化
D = 80 * 80 # input dimensionality: 80x80 grid
if resume:
  model = pickle.load(open('save.p', 'rb'))
else:
  model = {}
  model['W1'] = np.random.randn(H,D) / np.sqrt(D) # "Xavier" initialization
  model['W2'] = np.random.randn(H) / np.sqrt(H)

# update buffers that add up gradients over a batch
grad_buffer = { k : np.zeros_like(v) for k,v in model.iteritems() }
# rmsprop memory
rmsprop_cache = { k : np.zeros_like(v) for k,v in model.iteritems() }

def sigmoid(x): 
  return 1.0 / (1.0 + np.exp(-x)) # sigmoid "squashing" function to interval [0,1]

# 预处理图像
def prepro(I):
  """ prepro 210x160x3 uint8 frame into 6400 (80x80) 1D float vector """
  I = I[35:195] # crop
  I = I[::2,::2,0] # downsample by factor of 2
  I[I == 144] = 0 # erase background (background type 1)
  I[I == 109] = 0 # erase background (background type 2)
  I[I != 0] = 1 # everything else (paddles, ball) just set to 1
  return I.astype(np.float).ravel()

# 计算 discount 后的 rewards
def discount_rewards(r):
  """ take 1D float array of rewards and compute discounted reward """
  discounted_r = np.zeros_like(r)
  running_add = 0
  for t in reversed(xrange(0, r.size)):
    # reset the sum, since this was a game boundary (pong specific!)
    if r[t] != 0: running_add = 0
    running_add = running_add * gamma + r[t]
    discounted_r[t] = running_add
  return discounted_r

# 前向传播
def policy_forward(x):
  h = np.dot(model['W1'], x)
  h[h<0] = 0 # ReLU nonlinearity
  logp = np.dot(model['W2'], h)
  p = sigmoid(logp)
  return p, h # return probability of taking action 2, and hidden state

# 反向传播, eph: 隐藏单元值，epdlogp: policy gradient
def policy_backward(eph, epdlogp):
  """ backward pass. (eph is array of intermediate hidden states) """
  dW2 = np.dot(eph.T, epdlogp).ravel() # dw2 = 最终误差 * 隐藏单元值
  dh = np.outer(epdlogp, model['W2'])
  dh[eph <= 0] = 0 # backpro prelu
  dW1 = np.dot(dh.T, epx)
  return {'W1':dW1, 'W2':dW2}

# 预备开始
env = gym.make("Pong-v0")
observation = env.reset()
prev_x = None # used in computing the difference frame
xs,hs,dlogps,drs = [],[],[],[]  # xs图像，hs隐藏层，dlogs代价导数，drs单次动作回报
running_reward = None
reward_sum = 0
episode_number = 0
while True:
  if render: env.render()

  # 预处理输入图像，使用图像差
  cur_x = prepro(observation)
  x = cur_x - prev_x if prev_x is not None else np.zeros(D)
  prev_x = cur_x

  # 前向传播
  aprob, h = policy_forward(x)
  action = 2 if np.random.uniform() < aprob else 3 # roll the dice!

  # 记录中间状态
  xs.append(x) # observation
  hs.append(h) # hidden state
  y = 1 if action == 2 else 0 # a "fake label"
  # 使用的 对数损失函数(logarithmic loss function)，即交叉熵
  # grad that encourages the action that was taken to be taken
  # (see http://cs231n.github.io/neural-networks-2/#losses if confused)
  dlogps.append(y - aprob) 

  # 动一下
  observation, reward, done, info = env.step(action)
  reward_sum += reward
  # record reward 
  # (has to be done after we call step() to get reward for previous action)
  drs.append(reward)

  # 完成一次 episode
  if done:
    episode_number += 1

    # stack 所有中间状态
    epx = np.vstack(xs)  # inputs
    eph = np.vstack(hs)  # hidden states
    epdlogp = np.vstack(dlogps)  # action gradients
    epr = np.vstack(drs)  # rewards
    xs,hs,dlogps,drs = [],[],[],[] # reset array memory

    # 计算 discount 后的 rewards
    discounted_epr = discount_rewards(epr)
    # 正则化 rewards
    discounted_epr -= np.mean(discounted_epr)
    discounted_epr /= np.std(discounted_epr)

    # 使用回报，缩放梯度，policy gradient之美
    # modulate the gradient with advantage (PG magic happens right here.)
    epdlogp *= discounted_epr
    grad = policy_backward(eph, epdlogp)
    for k in model: grad_buffer[k] += grad[k] # 单个 batch 上的 gradient和

    # 使用 rmsprop法 修正权重
    if episode_number % batch_size == 0:
      for k,v in model.iteritems():
        g = grad_buffer[k] # gradient
        rmsprop_cache[k] = decay_rate * rmsprop_cache[k] + (1 - decay_rate) * g**2
        model[k] += learning_rate * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)
        grad_buffer[k] = np.zeros_like(v) # reset batch gradient buffer

    # 保存好参数
    if running_reward is None:
      running_reward = reward_sum
    else:
      running_reward = running_reward * 0.99 + reward_sum * 0.01
    print 'resetting env. episode reward total was %f. running mean: %f'\
      % (reward_sum, running_reward)
    if episode_number % 100 == 0: pickle.dump(model, open('save.p', 'wb'))
    reward_sum = 0
    observation = env.reset() # reset env
    prev_x = None

  # 一轮结束否
  if reward != 0: # Pong has either +1 or -1 reward exactly when game ends.
    print ('ep %d: game finished, reward: %f'\
      % (episode_number, reward)) + ('' if reward == -1 else ' !!!!!!!!')
```

## 1.10. Learned weights. （权重都学了什么）
权重 W1 的可视化  
![weights](img/weights.png)

# 2. What isn't happening （发生了什么）
- 策略梯度算法是一种 guess-and-check 模式  
- 很多方面和人类的学习方法不同，请看原文

# 3. Non-differentiable computation in Neural Networks （不可微计算)
看不懂

# 4. Conclustions （结论）
总之，还有很多问题

# 5. 参考
- [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/)
- [深度强化学习：基于像素的乒乓游戏](http://blog.csdn.net/lishuandao/article/details/52694770)
- [http://cs231n.github.io/neural-networks-2/#losses](http://cs231n.github.io/neural-networks-2/#losses)
- [CS231n课程笔记翻译：神经网络笔记 2](https://zhuanlan.zhihu.com/p/21560667?refer=intelligentunit)
- [用人话解释机器学习中的Logistic Regression（逻辑回归）](https://www.codelast.com/%E5%8E%9F%E5%88%9B-%E7%94%A8%E4%BA%BA%E8%AF%9D%E8%A7%A3%E9%87%8A%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%B8%AD%E7%9A%84logistic-regression%EF%BC%88%E9%80%BB%E8%BE%91%E5%9B%9E%E5%BD%92%EF%BC%89/)
- [斯坦福机器学习笔记-逻辑回归](https://yoyoyohamapi.gitbooks.io/mit-ml/content/%E9%80%BB%E8%BE%91%E5%9B%9E%E5%BD%92/articles/%E9%80%BB%E8%BE%91%E5%9B%9E%E5%BD%92.html)
- [logistic回归详解(二）：损失函数（cost function）详解](http://blog.csdn.net/bitcarmanlee/article/details/51165444)
- [Softmax函数与交叉熵](http://blog.csdn.net/behamcheung/article/details/71911133)
