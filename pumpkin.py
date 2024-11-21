import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Pumpkin body
pumpkin = patches.Ellipse((0, 0), 3, 1.5, color='orange')
ax.add_patch(pumpkin)
pumpkin_bump = patches.Ellipse(( 0.25, 0.70), 0.3, 0.2, color='orange')
ax.add_patch(pumpkin_bump)
pumpkin_bump = patches.Ellipse(( 0.50, 0.68), 0.3, 0.2, color='orange')
ax.add_patch(pumpkin_bump)
pumpkin_bump = patches.Ellipse(( 0.75, 0.64), 0.3, 0.2, color='orange')
ax.add_patch(pumpkin_bump)
pumpkin_bump = patches.Ellipse((-0.25, 0.70), 0.3, 0.2, color='orange')
ax.add_patch(pumpkin_bump)
pumpkin_bump = patches.Ellipse((-0.50, 0.68), 0.3, 0.2, color='orange')
ax.add_patch(pumpkin_bump)
pumpkin_bump = patches.Ellipse((-0.75, 0.64), 0.3, 0.2, color='orange')
ax.add_patch(pumpkin_bump)

# Eyes
left_eye = patches.Ellipse((-0.5, 0.2), 0.2, 0.3, color='white')
right_eye = patches.Ellipse((0.5, 0.2), 0.2, 0.3, color='white')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Nose
nose = patches.Polygon([(-0.1, 0), (0.1, 0), (0, -0.2)], color='white')
ax.add_patch(nose)

# Mouth
mouth = patches.Arc((0, -0.4), 1, 0.5, theta1=180, theta2=360, color='white')
ax.add_patch(mouth)
mouth = patches.Arc((0, -0.3), 1, 0.5, theta1=180, theta2=360, color='white')
ax.add_patch(mouth)

# Stem
stem = patches.Rectangle((-0.1, 0.75), 0.2, 0.2, color='green')
ax.add_patch(stem)

# Set axis limits and remove ticks
ax.set_xlim(-1.75, 1.75)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Pumpkin')

# save to file if desired
# =============================================================================
# True  - displays and saves the plot to file;
# False - only displays the plot
save_plot_to_file = True
filename = 'pumpkin.png'
# =============================================================================
if (save_plot_to_file):
    import os
    current_directory = os.getcwd()
    print("Current directory:", current_directory)
    plt.savefig(filename, dpi=300, edgecolor='none')
plt.show()
