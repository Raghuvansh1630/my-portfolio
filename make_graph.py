import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Data (Simulating a signal)
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                # Calculate the sine wave

# 2. Setup the Plot (Dark theme to match your site)
plt.style.use('dark_background')
plt.figure(figsize=(8, 4))

# 3. Draw the line
plt.plot(x, y, color='#00ffcc', linewidth=3, label='Signal')

# 4. Add labels
plt.title("My First Data Science Visualization")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3) # Faint grid lines

# 5. Save the image
plt.savefig("project_chart.png", transparent=True)
print("Success! Graph saved as 'project_chart.png'")