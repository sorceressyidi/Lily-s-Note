"""
Q-Learning Visualizer - Static Image Version for Notebook

Generates a static visualization showing Q-learning step by step.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============== CONFIG ==============
maze = np.array([
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 2]   # 2 = goal
])

n_rows, n_cols = maze.shape
start = (0, 0)
goal = (3, 3)

actions = ["UP", "DOWN", "LEFT", "RIGHT"]
action_delta = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

alpha = 0.5
gamma = 0.9


def step(state, action, maze_arr):
    """Take action; return (next_state, reward, done)."""
    dr, dc = action_delta[action]
    next_state = (state[0] + dr, state[1] + dc)

    if (next_state[0] < 0 or next_state[0] >= n_rows or
            next_state[1] < 0 or next_state[1] >= n_cols or
            maze_arr[next_state] == 1):
        return state, -0.5, False
    if next_state == goal:
        return next_state, 10.0, True
    return next_state, -0.1, False


def create_q_learning_visualization():
    """Create a multi-panel visualization of Q-learning."""
    
    # Run Q-learning and collect history
    Q = np.zeros((n_rows, n_cols, 4))
    np.random.seed(42)
    
    history = []
    episodes = 3
    
    for ep in range(episodes):
        state = start
        done = False
        step_count = 0
        while not done and step_count < 20:
            # epsilon-greedy
            if np.random.rand() < 0.3:
                action = np.random.randint(4)
            else:
                action = np.argmax(Q[state])
            
            next_state, reward, done = step(state, action, maze)
            
            old_q = Q[state][action]
            max_future_q = np.max(Q[next_state])
            new_q = old_q + alpha * (reward + gamma * max_future_q - old_q)
            Q[state][action] = new_q
            
            history.append({
                'episode': ep,
                'state': state,
                'action': action,
                'next_state': next_state,
                'reward': reward,
                'old_q': old_q,
                'new_q': new_q,
                'max_future_q': max_future_q,
                'Q': Q.copy()
            })
            
            state = next_state
            step_count += 1
    
    # Create visualization
    fig = plt.figure(figsize=(16, 12))
    fig.patch.set_facecolor('#1a1a2e')
    
    # Create grid
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3,
                         left=0.05, right=0.95, top=0.92, bottom=0.08)
    
    # === Panel 1: Maze with Q-values ===
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor('#0f0f1e')
    
    # Draw maze
    for i in range(n_rows):
        for j in range(n_cols):
            if maze[i, j] == 1:
                color = '#4a4a4a'
            elif maze[i, j] == 2:
                color = '#00ff88'
            else:
                color = '#2a2a4a'
            rect = plt.Rectangle((j-0.5, n_rows-1-i-0.5), 1, 1, 
                                 facecolor=color, edgecolor='white', linewidth=2)
            ax1.add_patch(rect)
    
    # Mark start
    ax1.plot(0, n_rows-1, 'o', markersize=20, color='#ff6b6b', 
             markeredgecolor='white', markeredgewidth=2)
    ax1.text(0, n_rows-1, 'S', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')
    
    # Mark goal
    ax1.plot(3, 0, '*', markersize=30, color='#00ff88')
    ax1.text(3, 0, 'G', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')
    
    ax1.set_xlim(-0.6, n_cols-0.4)
    ax1.set_ylim(-0.6, n_rows-0.4)
    ax1.set_aspect('equal')
    ax1.set_title('🗺️ Maze Environment', fontsize=14, fontweight='bold', 
                 color='white', pad=10)
    ax1.axis('off')
    
    # === Panel 2: Q-table heatmap ===
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor('#0f0f1e')
    
    # Show max Q-value for each state
    max_Q = np.max(Q, axis=2)
    im = ax2.imshow(max_Q, cmap='RdYlGn', aspect='auto')
    
    for i in range(n_rows):
        for j in range(n_cols):
            if maze[i, j] != 1:
                ax2.text(j, i, f'{max_Q[i,j]:.1f}', ha='center', va='center',
                        fontsize=11, fontweight='bold', color='white')
            else:
                ax2.text(j, i, '█', ha='center', va='center',
                        fontsize=20, color='#4a4a4a')
    
    ax2.set_title('📊 Max Q-Values per State', fontsize=14, fontweight='bold',
                 color='white', pad=10)
    ax2.set_xticks(range(n_cols))
    ax2.set_yticks(range(n_rows))
    ax2.tick_params(colors='white')
    plt.colorbar(im, ax=ax2, shrink=0.8)
    
    # === Panel 3: Q-values for start state ===
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_facecolor('#0f0f1e')
    
    q_start = Q[start]
    colors = ['#ff6b6b', '#4ecdc4', '#ffe66d', '#95e1d3']
    bars = ax3.bar(actions, q_start, color=colors, edgecolor='white', linewidth=2)
    
    for bar, v in zip(bars, q_start):
        ax3.text(bar.get_x() + bar.get_width()/2, v + 0.1, f'{v:.2f}',
                ha='center', fontsize=11, fontweight='bold', color='white')
    
    ax3.set_title(f'🎯 Q-values at Start {start}', fontsize=14, fontweight='bold',
                 color='white', pad=10)
    ax3.set_ylabel('Q(s, a)', fontsize=12, color='white')
    ax3.tick_params(colors='white')
    ax3.grid(True, alpha=0.2, color='#4a4a6a')
    
    # === Panel 4: Learning curve ===
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.set_facecolor('#0f0f1e')
    
    # Calculate cumulative max Q over time
    max_q_over_time = [h['Q'].max() for h in history]
    ax4.plot(max_q_over_time, color='#00ff88', linewidth=3, marker='o', 
            markersize=4, markerfacecolor='white')
    ax4.fill_between(range(len(max_q_over_time)), max_q_over_time, 
                    alpha=0.3, color='#00ff88')
    
    ax4.set_title('📈 Max Q-Value Over Time', fontsize=14, fontweight='bold',
                 color='white', pad=10)
    ax4.set_xlabel('Step', fontsize=12, color='white')
    ax4.set_ylabel('Max Q', fontsize=12, color='white')
    ax4.tick_params(colors='white')
    ax4.grid(True, alpha=0.2, color='#4a4a6a')
    
    # === Panel 5: Sample update ===
    ax5 = fig.add_subplot(gs[1, 1:])
    ax5.set_facecolor('#0f0f1e')
    ax5.axis('off')
    
    # Show a sample update step
    sample = history[5]  # Pick a representative step
    
    title_text = "⚡ Q-Learning Update Example"
    ax5.text(0.5, 0.95, title_text, ha='center', va='top', fontsize=16,
            fontweight='bold', color='white', transform=ax5.transAxes)
    
    state_text = f"State: {sample['state']} → Action: {actions[sample['action']]} → Next: {sample['next_state']}"
    ax5.text(0.5, 0.80, state_text, ha='center', va='top', fontsize=13,
            color='#4ecdc4', transform=ax5.transAxes,
            bbox=dict(boxstyle='round', facecolor='#2a2a4a', edgecolor='#4ecdc4', linewidth=2))
    
    reward_text = f"Reward: {sample['reward']:.2f}"
    ax5.text(0.5, 0.65, reward_text, ha='center', va='top', fontsize=13,
            color='#ffe66d', transform=ax5.transAxes)
    
    formula_text = f"""
Bellman Update Formula:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q(s,a) ← Q(s,a) + α × [r + γ × max Q(s',a') - Q(s,a)]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step-by-step:
  • Old Q({sample['state']}, {actions[sample['action']]}): {sample['old_q']:.3f}
  • Target = r + γ × max Q(next) = {sample['reward']:.2f} + {gamma} × {sample['max_future_q']:.3f} = {sample['reward'] + gamma * sample['max_future_q']:.3f}
  • Error = Target - Old Q = {sample['reward'] + gamma * sample['max_future_q'] - sample['old_q']:.3f}
  • New Q = Old Q + α × Error = {sample['new_q']:.3f}
"""
    ax5.text(0.5, 0.55, formula_text, ha='center', va='top', fontsize=11,
            color='white', family='monospace', transform=ax5.transAxes,
            bbox=dict(boxstyle='round', facecolor='#1a1a3e', edgecolor='#bb00ff', 
                     linewidth=2, alpha=0.9))
    
    # Main title
    fig.suptitle('🧠 Q-Learning: From Bellman Equations to Action', 
                fontsize=20, fontweight='bold', color='white', y=0.98)
    
    plt.savefig('q_learning_visual.png', dpi=150, facecolor='#1a1a2e',
               edgecolor='none', bbox_inches='tight')
    print("✓ Saved q_learning_visual.png")
    plt.close()


def create_q_learning_gif():
    """Create an animated GIF showing Q-learning progression."""
    import matplotlib.animation as animation
    
    # Run Q-learning and collect history
    Q = np.zeros((n_rows, n_cols, 4))
    np.random.seed(42)
    
    history = []
    episodes = 2
    
    for ep in range(episodes):
        state = start
        done = False
        step_count = 0
        while not done and step_count < 15:
            if np.random.rand() < 0.3:
                action = np.random.randint(4)
            else:
                action = np.argmax(Q[state])
            
            next_state, reward, done = step(state, action, maze)
            
            old_q = Q[state][action]
            max_future_q = np.max(Q[next_state])
            new_q = old_q + alpha * (reward + gamma * max_future_q - old_q)
            Q[state][action] = new_q
            
            history.append({
                'episode': ep,
                'state': state,
                'action': action,
                'next_state': next_state,
                'reward': reward,
                'old_q': old_q,
                'new_q': new_q,
                'max_future_q': max_future_q,
                'Q': Q.copy()
            })
            
            state = next_state
            step_count += 1
    
    # Create animation
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor('#1a1a2e')
    
    def animate(frame_idx):
        for ax in axes:
            ax.clear()
            ax.set_facecolor('#0f0f1e')
        
        if frame_idx >= len(history):
            frame_idx = len(history) - 1
        
        h = history[frame_idx]
        
        # Left: Maze
        ax1 = axes[0]
        for i in range(n_rows):
            for j in range(n_cols):
                if maze[i, j] == 1:
                    color = '#4a4a4a'
                elif maze[i, j] == 2:
                    color = '#00ff88'
                else:
                    color = '#2a2a4a'
                rect = plt.Rectangle((j-0.5, n_rows-1-i-0.5), 1, 1, 
                                     facecolor=color, edgecolor='white', linewidth=2)
                ax1.add_patch(rect)
        
        # Current position
        s = h['state']
        ax1.plot(s[1], n_rows-1-s[0], 'o', markersize=25, color='#ff6b6b',
                markeredgecolor='white', markeredgewidth=3)
        
        # Next position
        ns = h['next_state']
        ax1.plot(ns[1], n_rows-1-ns[0], 's', markersize=20, color='#ffa500',
                markeredgecolor='white', markeredgewidth=2)
        
        # Goal
        ax1.plot(3, 0, '*', markersize=30, color='#00ff88')
        
        ax1.set_xlim(-0.6, n_cols-0.4)
        ax1.set_ylim(-0.6, n_rows-0.4)
        ax1.set_aspect('equal')
        ax1.set_title(f'Step {frame_idx+1}: {h["state"]} → {actions[h["action"]]} → {h["next_state"]}',
                     fontsize=12, fontweight='bold', color='white', pad=10)
        ax1.axis('off')
        
        # Right: Q-values bar chart
        ax2 = axes[1]
        q_vals = h['Q'][h['state']]
        colors = ['#ff6b6b', '#4ecdc4', '#ffe66d', '#95e1d3']
        colors[h['action']] = '#bb00ff'  # Highlight chosen action
        
        bars = ax2.bar(actions, q_vals, color=colors, edgecolor='white', linewidth=2)
        for bar, v in zip(bars, q_vals):
            ax2.text(bar.get_x() + bar.get_width()/2, v + 0.05, f'{v:.2f}',
                    ha='center', fontsize=10, fontweight='bold', color='white')
        
        ax2.set_title(f'Q({h["state"]}, ·)  |  r={h["reward"]:.1f}', 
                     fontsize=12, fontweight='bold', color='white', pad=10)
        ax2.set_ylabel('Q-value', fontsize=11, color='white')
        ax2.tick_params(colors='white')
        ax2.grid(True, alpha=0.2, color='#4a4a6a')
        ax2.set_ylim(-1, max(q_vals.max() + 0.5, 1))
        
        fig.suptitle('🧠 Q-Learning Step by Step', fontsize=16, 
                    fontweight='bold', color='white', y=0.98)
        
        return axes
    
    anim = animation.FuncAnimation(fig, animate, frames=len(history),
                                  interval=1500, repeat=True)
    
    writer = animation.PillowWriter(fps=1)
    anim.save('q_learning_animation.gif', writer=writer, dpi=100)
    print("✓ Saved q_learning_animation.gif")
    plt.close()


if __name__ == "__main__":
    print("=" * 60)
    print("🎬 Creating Q-Learning Visualizations...")
    print("=" * 60)
    
    create_q_learning_visualization()
    create_q_learning_gif()
    
    print("\n✅ Done!")
    print("   • q_learning_visual.png - Static overview")
    print("   • q_learning_animation.gif - Step-by-step animation")
    print("=" * 60)
