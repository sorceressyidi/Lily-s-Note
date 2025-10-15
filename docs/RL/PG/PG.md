# An Exposition of Policy Gradient Methods: From REINFORCE to PPO



## 1\. The Foundation: REINFORCE and the Policy Gradient Theorem

Policy Gradient (PG) methods directly parameterize the policy $\pi_\theta(a|s)$ and optimize the policy parameters $\theta$ by performing gradient ascent on an objective function $J(\theta)$.

### 1.1. The Objective Function

The objective is to maximize the expected cumulative discounted reward, defined as the value of the initial state $s_0$:

$$J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)] = \mathbb{E}_{\tau \sim \pi_\theta}\left[\sum_{t=0}^T \gamma^t R(s_t, a_t)\right]$$

where $\tau = (s_0, a_0, s_1, a_1, \dots)$ is a trajectory sampled by following the policy $\pi_\theta$.

### 1.2. The Policy Gradient Theorem and its Derivation

The central challenge is to compute the gradient $\nabla_\theta J(\theta)$, as the expectation is taken over a distribution that itself depends on $\theta$. This is resolved by the Policy Gradient Theorem.

**Theorem**: The gradient of the objective function $J(\theta)$ is given by:

$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\left[\left(\sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t|s_t)\right) R(\tau)\right]$$

**Derivation**:

1.  **Definition of Expectation**: The expectation is an integral (or sum) over the space of all trajectories, weighted by their probabilities $P(\tau|\theta)$.

    $$\nabla_\theta J(\theta) = \nabla_\theta \int P(\tau|\theta) R(\tau) d\tau = \int \nabla_\theta P(\tau|\theta) R(\tau) d\tau$$

2.  **Log-Derivative Identity**: We apply the identity $\nabla_x f(x) = f(x) \nabla_x \log f(x)$.

    $$\int P(\tau|\theta) \nabla_\theta \log P(\tau|\theta) R(\tau) d\tau$$

3.  **Return to Expectation Form**: The integral is recognized again as an expectation.

    $$\mathbb{E}*{\tau \sim \pi*\theta}[\nabla_\theta \log P(\tau|\theta) R(\tau)]$$

4.  **Decomposition of Trajectory Probability**: The probability of a trajectory $P(\tau|\theta)$ is a product of the initial state probability $p(s_0)$ and the transition probabilities, which are composed of the policy and the environment dynamics.

    $$P(\tau|\theta) = p(s_0) \prod_{t=0}^{T-1} \pi_\theta(a_t|s_t) p(s_{t+1}|s_t, a_t)$$
    
    Taking the log gradient, the environment dynamics term $p(s_{t+1}|s_t, a_t)$ and initial state distribution $p(s_0)$ are constant with respect to $\theta$ and thus vanish.

    $$\nabla_\theta \log P(\tau|\theta) = \nabla_\theta \left[ \log p(s_0) + \sum_{t=0}^{T-1} \left(\log \pi_\theta(a_t|s_t) + \log p(s_{t+1}|s_t, a_t)\right) \right] = \sum_{t=0}^{T-1} \nabla_\theta \log \pi_\theta(a_t|s_t)$$

    This simplification yields a **model-free** algorithm, as the gradient does not depend on the environment's transition dynamics.

### 1.3. The REINFORCE Algorithm

The theorem provides an expectation that can be approximated with Monte Carlo sampling. A common refinement is to note that actions at time $t'$ cannot influence rewards received before $t'$ (causality). Thus, we can replace the total trajectory reward $R(\tau)$ with the **return-from-time-t**, $G_t = \sum_{k=t}^T \gamma^{k-t} R_k$. The practical gradient estimator for a batch of $N$ trajectories is:

$$\hat{g}_{\text{REINFORCE}} = \frac{1}{N} \sum_{i=1}^N \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t^{(i)}|s_t^{(i)}) G_t^{(i)}$$

**Limitation**: The Monte Carlo estimator $G_t$ for the expected return $Q^{\pi}(s_t, a_t)$ is unbiased but suffers from **high variance**. A single stochastic trajectory can yield a highly variable return, leading to noisy gradient estimates and unstable convergence.

-----

## 2\. Variance Reduction via Actor-Critic Methods

Actor-Critic methods mitigate the high variance of REINFORCE by introducing a learned value function approximator (the Critic) to provide a more stable signal to the policy (the Actor).

### 2.1. The Actor and The Critic

  * **Actor (Policy $\pi_\theta(a|s)$)**: A parameterized function that maps states to action distributions.
  * **Critic (Value Function $V_\phi(s)$)**: A parameterized function that estimates the expected return from a state $s$, i.e., $V_\phi(s) \approx V^\pi(s) = \mathbb{E}_{\tau \sim \pi_\theta}\left[\sum_{k=t}^\infty \gamma^{k-t} R_k | s_t = s\right]$.

### 2.2. The Advantage Function and Baseline Subtraction

A key technique for variance reduction is subtracting a state-dependent **baseline**, $b(s)$, from the return. A well-chosen baseline can significantly reduce variance without introducing bias.

**Proof of Unbiasedness**: We show that the expectation of the baseline term is zero.

$$\mathbb{E}_{(s,a) \sim \pi_\theta}[\nabla_\theta \log \pi_\theta(a|s) b(s)] = \int_s p(s) \sum_a \pi_\theta(a|s) \nabla_\theta \log \pi_\theta(a|s) b(s) da$$

$$= \int_s p(s) b(s) \sum_a \nabla_\theta \pi_\theta(a|s) da = \int_s p(s) b(s) \nabla_\theta \left(\sum_a \pi_\theta(a|s)\right) da$$

Since $\sum_a \pi_\theta(a|s) = 1$, its gradient is $\nabla_\theta(1) = 0$. Thus, the expectation is zero.

The optimal baseline is the state-value function, $V^\pi(s)$. Subtracting this from the action-value function, $Q^\pi(s,a)$, yields the **Advantage Function**:

$$A^\pi(s,a) = Q^\pi(s,a) - V^\pi(s)$$

The advantage captures whether an action is better or worse than the policy's average behavior in that state.

### 2.3. Actor-Critic Derivations

In practice, we use the Critic, $V_\phi(s)$, to estimate the advantage.

1.  **Advantage Estimation**: We can use the one-step **TD (Temporal Difference) error** as a low-variance, biased estimate of the advantage:

    $$A(s_t, a_t) \approx (R_t + \gamma V_\phi(s_{t+1})) - V_\phi(s_t)$$

2.  **Actor (Policy) Gradient**: The policy gradient is updated using this advantage estimate.

    $$\hat{g}*{\text{Actor}} = \mathbb{E}*t[\nabla*\theta \log \pi*\theta(a_t|s_t) A(s_t, a_t)]$$
    
    The Actor's parameters are updated via gradient ascent: $\theta \leftarrow \theta + \alpha \hat{g}_{\text{Actor}}$.

3.  **Critic (Value) Loss**: The Critic is updated by minimizing the Mean Squared Error between its predictions and the TD Target.

    $$L(\phi) = \mathbb{E}*t\left[(R_t + \gamma V*\phi(s_{t+1}) - V_\phi(s_t))^2\right]$$
    
    The Critic's parameters are updated via gradient descent: $\phi \leftarrow \phi - \beta \nabla_\phi L(\phi)$.

This formulation is often called **Advantage Actor-Critic (A2C)**.

-----

## 3\. Proximal Policy Optimization (PPO)

While A2C reduces variance, its on-policy nature is sample-inefficient, and it remains sensitive to step size, which can lead to catastrophic policy updates. PPO addresses both issues by enabling multi-epoch updates on sampled data in a constrained, stable manner.

### 3.1. The Core Problem and PPO's Objective

The goal is to maximize a "surrogate" objective function that encourages policy improvement, but penalizes large changes from the policy $\pi_{\theta_{old}}$ that was used to collect the data. This allows for multiple gradient steps on the same batch of data.

1.  **Probability Ratio**: The change in policy is measured by the ratio:

    $$r_t(\theta) = \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_{old}}(a_t | s_t)}$$

2.  **The Clipped Surrogate Objective**: This is PPO's central innovation. It takes the minimum of the normal objective and a "clipped" version that prevents the ratio $r_t(\theta)$ from moving too far from 1.0.

    $$L^{CLIP}(\theta) = \mathbb{E}_t \left[ \min \left( r_t(\theta) A_t, \quad \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t \right) \right]$$

    where `clip` constrains $r_t(\theta)$ to the interval $[1-\epsilon, 1+\epsilon]$. The `min` operator ensures that the update is conservative: it creates a pessimistic bound on the improvement, removing the incentive for the policy ratio to move outside the trusted interval.

### 3.2. PPO Algorithm and Objective Function

The full PPO objective function often includes two additional terms: a value function loss and an entropy bonus to encourage exploration.

$$L^{PPO}(\theta, \phi) = \mathbb{E}_t \left[ L^{CLIP}(\theta) - c_1 L^{VF}(\phi) + c_2 S[\pi_\theta](s_t) \right]$$

  * **$L^{CLIP}(\theta)$**: The policy objective defined above.
  * **$L^{VF}(\phi)$**: The Critic's value function loss, which is the squared error $(V_\phi(s_t) - G_t)^2$.
  * **$S[\pi_\theta](s_t)$**: An entropy bonus to encourage exploration and prevent premature convergence to a suboptimal policy.
  * $c_1, c_2$: Hyperparameters that weight these loss components.

The algorithm proceeds by collecting a batch of data with $\pi_{\theta_{old}}$, and then performing several epochs of stochastic gradient ascent on this combined objective function $L^{PPO}$ over mini-batches of the collected data. This multi-epoch update scheme dramatically improves sample efficiency.