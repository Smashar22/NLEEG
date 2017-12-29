
# User algorithm example

self.figure2.clear()
ax = self.figure2.add_subplot(1,1,1)
T = np.arange(0.0, 2.0, 0.01)
Q = 1 + np.sin(2*np.pi*T)
ax.plot(T, Q)
plt.title('Simple User Algorithm Example')
self.canvas2.draw()


