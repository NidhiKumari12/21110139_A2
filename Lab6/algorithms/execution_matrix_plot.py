import matplotlib.pyplot as plt

# Data
worker_counts = [1, 2, 4, 16]
speedup_load = [0.813, 0.9484, 0.7755, 0.8]
speedup_no = [0.9784, 0.9235, 0.856, 0.69]

# Plot
plt.plot(worker_counts, speedup_load, marker='o', linestyle='-', label='Speedup (With Load)')
plt.plot(worker_counts, speedup_no, marker='s', linestyle='--', label='Speedup (With No)')

# Labels and Title
plt.xlabel('Worker Count')
plt.ylabel('Speedup')
plt.title('Worker Count vs Speedup')
plt.legend()
plt.grid(True)

# Save Plot as Image
plt.savefig('execution_matrix_plot.png')

print("Plot saved as 'execution_matrix_plot.png'")

