"""
Unit 2 - Example 1: Q-Learning Algorithm
الوحدة 2 - مثال 1: خوارزمية Q-Learning

This example demonstrates:
1. Q-learning algorithm
2. Q-table initialization
3. Q-value updates
4. Policy extraction
"""

import numpy as np

print("=" * 60)
print("Example 1: Q-Learning Algorithm")
print("مثال 1: خوارزمية Q-Learning")
print("=" * 60)

# Simple Grid World Environment
# بيئة شبكة بسيطة
# States: 0, 1, 2, 3, 4 (4 is goal)
# Actions: 0=left, 1=right

class SimpleGridWorld:
    """
    Simple grid world for Q-learning demonstration.
    شبكة بسيطة لعرض Q-learning.
    """
    def __init__(self):
        self.states = 5
        self.actions = 2  # left, right
        self.goal_state = 4
        
    def get_reward(self, state, action, next_state):
        """Get reward for transition."""
        if next_state == self.goal_state:
            return 10.0  # Goal reward
        return -0.1  # Small negative reward for each step
    
    def get_next_state(self, state, action):
        """Get next state after action."""
        if action == 0:  # left
            return max(0, state - 1)
        else:  # right
            return min(self.states - 1, state + 1)

# Initialize Q-table
# تهيئة جدول Q
env = SimpleGridWorld()
Q = np.zeros((env.states, env.actions))

print("\nInitial Q-table:")
print("جدول Q الأولي:")
print(Q)

# Q-Learning parameters
# معاملات Q-Learning
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

print("\n" + "=" * 60)
print("Q-Learning Training")
print("تدريب Q-Learning")
print("=" * 60)

# Training loop
# حلقة التدريب
num_episodes = 100

for episode in range(num_episodes):
    state = 0  # Start state
    
    while state != env.goal_state:
        # Epsilon-greedy action selection
        # اختيار الإجراء باستخدام epsilon-greedy
        if np.random.random() < epsilon:
            action = np.random.randint(env.actions)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit
        
        # Take action
        next_state = env.get_next_state(state, action)
        reward = env.get_reward(state, action, next_state)
        
        # Q-learning update
        # تحديث Q-learning
        Q[state, action] = Q[state, action] + alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )
        
        state = next_state

print("\nTrained Q-table:")
print("جدول Q المدرب:")
print(Q)

# Extract policy
# استخراج السياسة
print("\n" + "=" * 60)
print("Extracted Policy")
print("السياسة المستخرجة")
print("=" * 60)

policy = {}
for state in range(env.states):
    best_action = np.argmax(Q[state])
    action_name = "left" if best_action == 0 else "right"
    policy[state] = action_name
    print(f"State {state}: {action_name}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

