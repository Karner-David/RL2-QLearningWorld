import matplotlib.pyplot as plt
import numpy as np

def plot_rewards(rewards):
    """TODO: Smooth and plot reward per episode"""
    rewards = np.array(rewards)

    smoothed = np.convolve(rewards, np.ones(10)/10, mode='valid')

    plt.figure(figsize=(10,5))
    plt.plot(smoothed, label=f'Moving Avg (window=10)', color='blue')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('Total Reward per Episode (Smoothed)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
