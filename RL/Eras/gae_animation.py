"""
GAE 动画 - 保存为 GIF 版本
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, FancyArrowPatch
import matplotlib

# 设置后端
matplotlib.use('Agg')

class GAEAnimationGIF:
    def __init__(self):
        self.timesteps = 10
        self.rewards = np.array([1.5, 2.0, 2.5, 3.0, 3.2, 3.5, 3.8, 3.0, 2.0, -15.0])
        self.values = np.array([80, 95, 115, 135, 155, 175, 185, 175, 150, 100])
        self.positions_x = np.cumsum(np.array([0, 1.5, 2.0, 2.5, 3.0, 3.2, 3.5, 3.8, 3.0, 2.0, -1.0]))
        self.positions_y = np.array([0.5, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.75, 0.6, 0.3, -0.2])
        
        self.gamma = 0.99
        self.gae_lambda = 0.95
        self.next_value = 0
        
        self.deltas = np.zeros(self.timesteps)
        self.advantages = np.zeros(self.timesteps)
        self.compute_gae()
    
    def compute_gae(self):
        last_gae = 0
        for i in reversed(range(self.timesteps)):
            if i == self.timesteps - 1:
                next_val = self.next_value
            else:
                next_val = self.values[i + 1]
            
            self.deltas[i] = self.rewards[i] + self.gamma * next_val - self.values[i]
            self.advantages[i] = last_gae = self.deltas[i] + self.gamma * self.gae_lambda * last_gae
    
    def create_animation(self, output_file):
        self.fig = plt.figure(figsize=(20, 12))
        self.fig.patch.set_facecolor('#1a1a2e')
        
        gs = self.fig.add_gridspec(3, 2, hspace=0.35, wspace=0.25,
                                   left=0.05, right=0.95, top=0.95, bottom=0.08)
        
        self.ax_trajectory = self.fig.add_subplot(gs[0, :])
        self.ax_trajectory.set_facecolor('#0f0f1e')
        
        self.ax_table = self.fig.add_subplot(gs[1, 0])
        self.ax_table.set_facecolor('#0f0f1e')
        
        self.ax_delta = self.fig.add_subplot(gs[1, 1])
        self.ax_delta.set_facecolor('#0f0f1e')
        
        self.ax_gae = self.fig.add_subplot(gs[2, :])
        self.ax_gae.set_facecolor('#0f0f1e')
        
        print("Creating animation...")
        anim = animation.FuncAnimation(
            self.fig, self.animate, 
            frames=self.timesteps + 2,
            interval=1000,
            repeat=True,
            blit=False
        )
        
        print(f"Saving to {output_file}...")
        writer = animation.PillowWriter(fps=1)
        anim.save(output_file, writer=writer, dpi=100)
        print(f"✓ Animation saved!")
    
    def animate(self, frame):
        if frame < self.timesteps:
            current_step = self.timesteps - 1 - frame
            self.update_all_plots(current_step)
        else:
            self.update_all_plots(0)
        return []
    
    def update_all_plots(self, calc_step):
        # 清空所有子图
        self.ax_trajectory.clear()
        self.ax_table.clear()
        self.ax_delta.clear()
        self.ax_gae.clear()
        
        # 设置背景色
        self.ax_trajectory.set_facecolor('#0f0f1e')
        self.ax_table.set_facecolor('#0f0f1e')
        self.ax_delta.set_facecolor('#0f0f1e')
        self.ax_gae.set_facecolor('#0f0f1e')
        
        # === 轨迹图 ===
        self.ax_trajectory.axhline(0, color='#4a4a4a', linewidth=3, alpha=0.5)
        self.ax_trajectory.fill_between([-2, max(self.positions_x)+2], -0.5, 0, 
                                       color='#2a2a2a', alpha=0.3)
        
        # 画淡色轨迹
        self.ax_trajectory.plot(self.positions_x, self.positions_y, 
                               color='#3a3a5a', linewidth=2, linestyle='--', alpha=0.3)
        
        # 画所有点（淡色）
        for i in range(self.timesteps):
            x, y = self.positions_x[i], self.positions_y[i]
            circle = Circle((x, y), 0.15, color='#4a4a6a', alpha=0.3, zorder=1)
            self.ax_trajectory.add_patch(circle)
            self.ax_trajectory.text(x, y-0.5, f't={i}', ha='center', 
                                   color='#6a6a8a', fontsize=9, alpha=0.5)
        
        # 高亮已计算的部分
        for i in range(calc_step, self.timesteps):
            x, y = self.positions_x[i], self.positions_y[i]
            color = '#00ff88' if self.advantages[i] > 0 else '#ff4444'
            circle = Circle((x, y), 0.2, color=color, alpha=0.9, zorder=10,
                          edgecolor='white', linewidth=2)
            self.ax_trajectory.add_patch(circle)
            self.ax_trajectory.text(x, y+0.4, f'A={self.advantages[i]:.0f}', 
                                   ha='center', fontsize=10, color=color, 
                                   fontweight='bold', zorder=11)
        
        # 画彩色轨迹线
        for i in range(calc_step, self.timesteps - 1):
            color = '#00ff88' if self.advantages[i] > 0 else '#ff4444'
            self.ax_trajectory.plot([self.positions_x[i], self.positions_x[i+1]],
                                   [self.positions_y[i], self.positions_y[i+1]],
                                   color=color, linewidth=4, alpha=0.8, zorder=5)
        
        # 当前计算点（紫色）
        x, y = self.positions_x[calc_step], self.positions_y[calc_step]
        circle = Circle((x, y), 0.35, color='#bb00ff', alpha=0.7, zorder=15,
                       edgecolor='white', linewidth=3)
        self.ax_trajectory.add_patch(circle)
        self.ax_trajectory.text(x, y-0.6, f'⬅ COMPUTING t={calc_step}', 
                               ha='center', fontsize=12, color='#bb00ff', 
                               fontweight='bold', zorder=16,
                               bbox=dict(boxstyle='round', facecolor='#1a1a2e', 
                                       edgecolor='#bb00ff', linewidth=2))
        
        # 递归箭头
        if calc_step < self.timesteps - 1:
            arrow = FancyArrowPatch(
                (self.positions_x[calc_step+1], self.positions_y[calc_step+1] + 0.3),
                (self.positions_x[calc_step], self.positions_y[calc_step] + 0.3),
                arrowstyle='->', mutation_scale=30, linewidth=3,
                color='#bb00ff', alpha=0.8, zorder=12
            )
            self.ax_trajectory.add_patch(arrow)
        
        self.ax_trajectory.set_xlim(-1, max(self.positions_x)+2)
        self.ax_trajectory.set_ylim(-1, 1.5)
        self.ax_trajectory.set_title('🏃 HalfCheetah Trajectory', 
                                    fontsize=16, fontweight='bold', color='white', pad=15)
        self.ax_trajectory.set_xlabel('Distance', fontsize=12, color='white')
        self.ax_trajectory.set_ylabel('Height', fontsize=12, color='white')
        self.ax_trajectory.grid(True, alpha=0.2, color='#4a4a6a')
        self.ax_trajectory.tick_params(colors='white')
        
        # === 数据表格 ===
        self.ax_table.axis('off')
        self.ax_table.set_title('📊 Episode Data', fontsize=14, fontweight='bold', 
                               color='white', pad=10)
        
        table_data = []
        headers = ['t', 'Reward', 'Value', 'δ', 'Advantage']
        for i in range(calc_step, min(calc_step + 5, self.timesteps)):
            row = [
                f'{i}',
                f'{self.rewards[i]:.1f}',
                f'{self.values[i]:.0f}',
                f'{self.deltas[i]:.1f}',
                f'{self.advantages[i]:.1f}'
            ]
            table_data.append(row)
        
        if table_data:
            table = self.ax_table.table(cellText=table_data, colLabels=headers,
                                        cellLoc='center', loc='center',
                                        bbox=[0, 0, 1, 1])
            table.auto_set_font_size(False)
            table.set_fontsize(11)
            
            for i in range(len(headers)):
                cell = table[(0, i)]
                cell.set_facecolor('#bb00ff')
                cell.set_text_props(weight='bold', color='white')
            
            for i in range(1, len(table_data) + 1):
                for j in range(len(headers)):
                    cell = table[(i, j)]
                    if i == 1:
                        cell.set_facecolor('#3a3a5a')
                    else:
                        cell.set_facecolor('#2a2a3a')
                    cell.set_text_props(color='white')
                    cell.set_edgecolor('#4a4a6a')
        
        # === TD Error ===
        self.ax_delta.set_title('⚡ TD Error Calculation', fontsize=14, 
                               fontweight='bold', color='white', pad=10)
        
        x = np.arange(self.timesteps)
        for i in range(self.timesteps):
            if i >= calc_step:
                color = '#00ff88' if self.deltas[i] > 0 else '#ff4444'
                alpha = 0.9
            else:
                color = '#4a4a6a'
                alpha = 0.3
            
            self.ax_delta.bar(i, self.deltas[i], color=color, alpha=alpha, 
                             edgecolor='white', linewidth=1.5)
        
        self.ax_delta.bar(calc_step, self.deltas[calc_step], color='#bb00ff', 
                         alpha=0.9, edgecolor='white', linewidth=3)
        
        if calc_step == self.timesteps - 1:
            next_v = self.next_value
        else:
            next_v = self.values[calc_step + 1]
        
        formula = f't={calc_step}: δ={self.rewards[calc_step]:.1f}+{self.gamma:.2f}×{next_v:.0f}-{self.values[calc_step]:.0f}={self.deltas[calc_step]:.1f}'
        self.ax_delta.text(0.5, 0.95, formula, transform=self.ax_delta.transAxes,
                          fontsize=10, ha='center', va='top', color='white',
                          bbox=dict(boxstyle='round', facecolor='#bb00ff', alpha=0.8))
        
        self.ax_delta.axhline(0, color='white', linewidth=1, alpha=0.5)
        self.ax_delta.grid(True, alpha=0.2, color='#4a4a6a')
        self.ax_delta.tick_params(colors='white')
        self.ax_delta.set_xlabel('Time Step', fontsize=11, color='white')
        self.ax_delta.set_ylabel('TD Error', fontsize=11, color='white')
        
        # === GAE ===
        self.ax_gae.set_title('🔄 GAE Calculation (Backward)', fontsize=14, 
                             fontweight='bold', color='white', pad=10)
        
        for i in range(self.timesteps):
            if i >= calc_step:
                color = '#00ff88' if self.advantages[i] > 0 else '#ff4444'
                alpha = 0.9
            else:
                color = '#4a4a6a'
                alpha = 0.3
            
            self.ax_gae.bar(i, self.advantages[i], color=color, alpha=alpha, 
                           edgecolor='white', linewidth=1.5)
        
        self.ax_gae.bar(calc_step, self.advantages[calc_step], color='#bb00ff', 
                       alpha=0.9, edgecolor='white', linewidth=3)
        
        if calc_step < self.timesteps - 1:
            arrow = FancyArrowPatch(
                (calc_step + 1, self.advantages[calc_step + 1]),
                (calc_step + 0.3, self.advantages[calc_step]),
                arrowstyle='->', mutation_scale=25, linewidth=3,
                color='#bb00ff', alpha=0.8, zorder=10
            )
            self.ax_gae.add_patch(arrow)
            formula = f't={calc_step}: A={self.deltas[calc_step]:.1f}+{self.gamma*self.gae_lambda:.3f}×({self.advantages[calc_step+1]:.1f})={self.advantages[calc_step]:.1f}'
        else:
            formula = f't={calc_step}: A={self.deltas[calc_step]:.1f}+0={self.advantages[calc_step]:.1f}'
        
        self.ax_gae.text(0.5, 0.95, formula, transform=self.ax_gae.transAxes,
                        fontsize=10, ha='center', va='top', color='white',
                        bbox=dict(boxstyle='round', facecolor='#bb00ff', alpha=0.8))
        
        progress = (self.timesteps - calc_step) / self.timesteps * 100
        self.ax_gae.text(0.98, 0.05, f'Progress: {progress:.0f}%', 
                        transform=self.ax_gae.transAxes,
                        fontsize=12, ha='right', va='bottom', color='#00ff88',
                        fontweight='bold')
        
        self.ax_gae.axhline(0, color='white', linewidth=1, alpha=0.5)
        self.ax_gae.grid(True, alpha=0.2, color='#4a4a6a')
        self.ax_gae.tick_params(colors='white')
        self.ax_gae.set_xlabel('Time Step', fontsize=11, color='white')
        self.ax_gae.set_ylabel('Advantage', fontsize=11, color='white')

def main():
    print("=" * 80)
    print("🎬 Creating GAE Animation GIF...")
    print("=" * 80)
    
    visualizer = GAEAnimationGIF()
    output_file = 'gae_animation.gif'
    visualizer.create_animation(output_file)
    
    print("\n✅ Done! GIF saved to:", output_file)
    print("\n📝 What the animation shows:")
    print("   • TOP: Robot trajectory (green=good, red=bad)")
    print("   • MIDDLE-LEFT: Data table")
    print("   • MIDDLE-RIGHT: TD Error (δ) bars")
    print("   • BOTTOM: GAE Advantage bars")
    print("   • Purple = Currently computing")
    print("   • Purple arrows = Backward recursion direction")
    print("=" * 80)

if __name__ == "__main__":
    main()
