import matplotlib.pyplot as plt
import numpy as np

# Create the data for the bar plot
designs = ['TVM_VTA original', 'Optimized', 'Berkeley-hardfloat original', 'optimized']
time = [190, 92, 191, 109]

# Define the width of the bars
bar_width = 0.35

# Plot the bar plot
fig, ax = plt.subplots()
bar1 = ax.bar(designs[:2], time[:2], color=(0.2, 0.4, 0.6, 0.6), width=bar_width)
bar2 = ax.bar(designs[2:], time[2:], color='orange', width=bar_width)

# Add labels and title
ax.set_xlabel('Benchmark', fontsize=28)
ax.set_ylabel('Time Consumption', fontsize=28)
# ax.set_title('FPGA Resource Usage Comparison', fontsize=20)

# Add a legend
ax.legend((bar1, bar2), ('TVM-VTA', 'Berkeley-hardfloat'), fontsize=25)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: '{:d}m {:d}s'.format(int(x//60), int(x%60))))
plt.gca().tick_params(axis='both', labelsize=20)

# Show the plot
plt.show()