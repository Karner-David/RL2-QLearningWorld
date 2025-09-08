# Q-Learning in Gridworld 🧠➡️🏁

This project implements a simple **Q-learning agent** that learns to navigate a **5×5 Gridworld** with obstacles. The goal is to reach the terminal state while minimizing penalties for extra moves.

---

## 🚀 Project Overview

- **Environment:**  
  A 5×5 grid with:
  - A fixed **start state** `(0, 0)`
  - A **goal state** `(4, 4)`
  - Several **obstacles** the agent cannot move into
  - Step penalty (`-0.1`) and goal reward (`+100`)

- **Agent:**  
  A tabular **Q-learning agent** that:
  - Maintains a Q-table mapping `(state, action)` → value
  - Chooses actions using an **ε-greedy policy**
  - Updates values with the standard Q-learning rule

- **Training:**  
  - Runs multiple episodes
  - Resets the environment each episode
  - Learns optimal paths by trial and error
  - Converges to ~99 reward (shortest path with step costs)

---

## 🧮 What I learned

- Q-learning is good for environments that have a small amount of discrete states and actions, making the table not too expensive. It also works pretty well with e-greedy policy as it will enable the agent to learn different paths while still exploiting high Q paths.

- Shaping penalties and rewards to influence the agent's behavior

- It's better to explore a lot in the beginning to eventually find the best path, then focus on exploiting in the later episodes.

---

## 📊 Results

Reward Curve

After training, the agent consistently achieves ~99.2 reward per episode, which corresponds to a near-optimal 8-step path. The following chart showcases the total reward per episode and shows the beginning exploration into exploitation once the optimal path is found.

![Result Curve](/result.png)
