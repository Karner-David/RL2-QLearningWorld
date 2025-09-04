import numpy as np

class GridworldEnv:
    def __init__(self, width, height, start, goal, obstacles, penalty=-1, reward=10):
        self.width = width
        self.height = height
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.penalty = penalty
        self.reward = reward
        self.reset()

    def reset(self):
        self.agent_pos = self.start
        return self.agent_pos

    def step(self, action):
        """TODO: Move the agent, return next_state, reward, done"""
        pass

    def is_terminal(self, state):
        """TODO: Return whether state is terminal"""
        pass

    def get_state_space(self):
        return [(x, y) for x in range(self.width) for y in range(self.height) if (x, y) not in self.obstacles]

    def get_action_space(self):
        return [0, 1, 2, 3]  # up, down, left, right

    def render(self):
        """Optional: print the grid for visualization"""
        pass
