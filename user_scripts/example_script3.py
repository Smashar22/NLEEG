# Example user script - 3
# This script template shows the Hilbert Transform being Implemented

# When the Hilbert Transform is applied 
# To a Cos(signal), it makes a Sine(signal)
# Paste the following example into the user script window and see.


self.figure2.clear()                  #clears window for new plot
ax = self.figure2.add_subplot(1,1,1)  #adds plot
T = np.arange(0.0, 2.0, 0.01)         #x axis ticks
Q = np.cos(2*np.pi*T)                 #use a cosine wave as data

an_sig = hilbert(Q)
hilby_imag = an_sig.imag

ax.plot(T, Q, label="Real Signal (Cosine)")               #plot variables
ax.plot(T, hilby_imag, label="Hilbert Transform (Sine) ") #plot variables
ax.legend(loc='best')
self.canvas2.draw()                   #redraws the canvas


# Save Script will save to the "user_scripts" folder

# Have Fun Plotting!







