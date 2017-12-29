#This is a script template for implementation of your Algorithm

 #Apply your algorithm to the variables marked below
 #Click Plot and NLEEG will take care of the rest


#self.plot_arr = []   # contains all plots

#self.lines = []   # contains all lines

#data[] is a dictionary containing all variables

self.figure2.clear() 			 #clears window for new plot
ax = self.figure2.add_subplot(1,1,1) 			 #adds plot
T = np.arange(0.0, 2.0, 0.01)
Q = 1 + np.sin(2*np.pi*T)
ax.plot(T, Q) 			 #plots variables T and Q
self.canvas2.draw() 			 #redraws the canvas

#<--- Remove the hash marks at the front to uncomment code

#Have Fun Plotting!
