import numpy as np
import random

class QLearningAgent:
    def __init__(self, state_space, action_space, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.state_space = state_space
        self.action_space = action_space
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = {}

        self.reset()

    def reset(self):
        """TODO: Initialize Q-table with zeros"""
        pass

    def select_action(self, state):
        """TODO: ε-greedy policy"""
        pass

    def update(self, state, action, reward, next_state, done):
        """TODO: Q-learning update"""
        pass
