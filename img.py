import matplotlib.pyplot as plt
import numpy as np

# Create the data for the bar plot
designs = ['Original Design', 'Optimized Design']
ALMs = [20331, 2597]

# Plot the bar plot
plt.bar(designs, ALMs, color=[(0.19, 0.46, 0), (0.19, 0.46, 0.58)])

# Add labels and title
plt.xlabel('Benchmarks', fontsize=25)
plt.ylabel('ALMs', fontsize=25)
# plt.title('FPGA Resource Usage Comparison')

plt.gca().tick_params(axis='both', labelsize=20)

# Show the plot
plt.show()