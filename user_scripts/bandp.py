import math


"""
Brain waves

Delta wave – (0.1 – 3 Hz)
Theta wave – (4 – 7 Hz)
Alpha wave – (8 – 15 Hz)
Mu wave – (7.5 – 12.5 Hz)
SMR wave – (12.5 – 15.5 Hz)
Beta wave – (16 – 31 Hz)
Gamma wave – (32 – 100 Hz)
"""

# lowcut = 0 hz
# highcut = 150hz


GpdB = 10  # Gain

wp = 10 #pass band freq - area where freq is allowed

GsdB = 50 # Gain 

ws = 50 #stop band freq - area where frequency dies off
        # cut off freq - exact point where frequency starts to decline

# n = 0 #compute this filter order N


##### another try
# n = (1/2) * (  (math.log(((1/0.6)-1) / ((1/0.8)-1)))  /  math.log(ws/wp) )
# print('new try, n = ', n)
########



a = math.log(10)

n = ( a * ( ((10 ** (-GsdB/10)) - 1)/((10 ** (GpdB/10))-1)))/ (2 * a * (ws/wp))

print(n)

n = math.ceil(n)

print('n filter order = ', n)


#cut off frequency
wc = (wp / ((10 ** (-GpdB/10)) - 1)** (1/2*n))

print('cut off = ', wc)






