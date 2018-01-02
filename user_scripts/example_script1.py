# Basic user script - 1 
# This script shows the basic variables


N = data["num_samples"]                     #this is your eeg data x-axis (time)

self.figure2.clear()                        #this clears the previous plot

ax = self.figure2.add_subplot(1,1,1)        #this adds the plot to the NLEEG window

x_axis_data = np.linspace(0.0, N, N)        #this sets the x axis time length

y_axis_data = self.lines[(3)]               #this is your eeg data on channel 4

ax.plot(x_axis_data, y_axis_data)           #this plots your data

plt.title('Simple User Algorithm Example')

self.canvas2.draw()                         #this draws everything onto the window


