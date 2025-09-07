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
    rewards_list = []
    for i in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        steps = 0
        while not done and steps < 100:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
            steps += 1

        rewards_list.append(total_reward)
        if (i + 1) > 2000:
            if (i + 1) % 50 == 0:
                agent.epsilon = agent.epsilon * 0.99
        if (i + 1) % 100 == 0:
            print(f"Episode {i+1}/{episodes}, Reward: {total_reward:.2f}, Epsilon: {agent.epsilon:.3f}")


    return rewards_list


def main():
    env = GridworldEnv(
        width=5,
        height=5,
        start=(0, 0),
        goal=(4, 4),
        obstacles=[(1, 1), (2, 2), (3, 3)],
        penalty=-0.1,
        reward=100
    )
    agent = QLearningAgent(env.get_state_space(), env.get_action_space())
    rewards = train(env, agent, episodes=5000)

    # Plot reward curve
    plot_rewards(rewards)

if __name__ == "__main__":
    main()
