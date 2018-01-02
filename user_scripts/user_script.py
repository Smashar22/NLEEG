

#self.plot_arr = []   # contains all plots
#self.lines = []   # contains all lines

# User algorithm example

self.figure2.clear()
ax = self.figure2.add_subplot(1,1,1)
x_axis_data = np.arange(0.0, 2.0, 0.01)   #time
y_axis_data = 1 + np.sin(2*np.pi*T)       #sine values
ax.plot(T, Q)
plt.title('Simple User Algorithm Example')
self.canvas2.draw()


