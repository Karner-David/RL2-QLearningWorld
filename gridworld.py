import numpy as np

class GridworldEnv:
    def __init__(self, width, height, start, goal, obstacles, penalty=-.1, reward=100):
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

    # 0 up | 1 down | 2 left | 3 right
    # returns the new position, reward or penalty if at goal, and whether it at goal or not
    def step(self, action):
        """TODO: Move the agent, return next_state, reward, done"""
        if (action == 0):
            new_pos = (self.agent_pos[0], max(0, self.agent_pos[1] - 1))
        elif (action == 1):
            new_pos = (self.agent_pos[0], min(self.height - 1, self.agent_pos[1] + 1))
        elif (action == 2):
            new_pos = (max(0, self.agent_pos[0] - 1), self.agent_pos[1])
        elif (action == 3):
            new_pos = (min(self.width - 1, self.agent_pos[0] + 1), self.agent_pos[1])

        if new_pos not in self.obstacles:
            self.agent_pos = new_pos

        return self.agent_pos, self.reward if self.agent_pos == self.goal else self.penalty, self.agent_pos == self.goal

    def is_terminal(self, state):
        """TODO: Return whether state is terminal"""
        return state == self.goal

    def get_state_space(self):
        return [(x, y) for x in range(self.width) for y in range(self.height) if (x, y) not in self.obstacles]

    def get_action_space(self):
        return [0, 1, 2, 3]  # up, down, left, right

    def render(self):
        """Optional: print the grid for visualization"""
        pass
