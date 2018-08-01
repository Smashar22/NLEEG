# Example user script - 2
# This script template shows the Faster Fourier Transform being Implemented


ch_num = 5  # change this to select a different channel

self.figure2.clear()
N = data["num_samples"]
samp = data["samp_rate"]
T = 1.0 / samp
N_fft = samp/5       
y = self.lines[(ch_num-1)]
m_rem = np.ones_like(y)*np.mean(y)        # mean adjusted
y = y - m_rem
yf = fft(y, n=N_fft)                      # Compute the fft
xf = np.arange(0,samp,samp/N_fft)
d = self.figure2.add_subplot(1,1,1)
d.set_xlim(xmin=0, xmax=100)
d.set_xticks(np.arange(0, 100, 10))
d.grid()
d.plot(xf,np.abs(yf), lw=2.0, c='b')      # plot variables
d.set_ylabel('FFT magnitude (power)')
d.set_xlabel('Frequency (Hz)')
self.canvas2.draw()

# Save Script will save to the "user_scripts" folder

# Have Fun Plotting!

