import numpy as np
import random

class QLearningAgent:
    def __init__(self, state_space, action_space, alpha=0.1, gamma=0.8, epsilon=0.08):
        self.state_space = state_space
        self.action_space = action_space
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = {}
        self.reset()

    def reset(self):
        """TODO: Initialize Q-table with zeros"""
        self.Q = {(state, action): 0.0 for state in self.state_space for action in self.action_space}
        # print(self.Q)

    def select_action(self, state):
        """TODO: ε-greedy policy"""

        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.action_space)
        else:
            q_vals = [self.Q[(state, a)] for a in self.action_space]
            max_q = max(q_vals)
            max_as = [a for a in self.action_space if self.Q[(state, a)] == max_q]
            action = np.random.choice(max_as)

        return action

    def update(self, state, action, reward, next_state, done):
        """TODO: Q-learning update"""
        target = reward + self.gamma * max(self.Q[(next_state, a)] for a in self.action_space) * (not done)
        self.Q[(state, action)] += self.alpha * (target - self.Q[(state, action)])

