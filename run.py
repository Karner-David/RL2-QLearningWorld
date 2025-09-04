from gridworld import GridworldEnv
from q_learning_agent import QLearningAgent
from plots import plot_rewards

def train(env, agent, episodes):
    """TODO: Implement the training loop
    - Reset the environment each episode
    - For each time step:
        - Select an action using the agent
        - Step the environment to get next_state, reward, done
        - Update the Q-table
        - Accumulate total reward
    - Return a list of total rewards per episode
    """
    pass


def main():
    env = GridworldEnv(
        width=5,
        height=5,
        start=(0, 0),
        goal=(4, 4),
        obstacles=[(1, 1), (2, 2), (3, 3)],
        penalty=-1,
        reward=10
    )
    agent = QLearningAgent(env.get_state_space(), env.get_action_space())
    rewards = train(env, agent, episodes=500)

    # Plot reward curve
    plot_rewards(rewards)

if __name__ == "__main__":
    main()
