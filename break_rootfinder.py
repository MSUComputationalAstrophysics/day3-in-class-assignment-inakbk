#in-class 3

from pylab import *
from scipy import interpolate


def breaking_function(x):


#interval
a = 
b = 

x = linspace(a, b, 1000)


#pre-class code:

#scipy methods:
y_sci_lin = interpolate.interp1d(ip.all_x, ip.all_f_of_x, kind='linear')
y_sci_nearest = interpolate.interp1d(ip.all_x, ip.all_f_of_x, kind='nearest')
y_sci_cubic = interpolate.interp1d(ip.all_x, ip.all_f_of_x, kind='cubic')

figure(1)
plot(x, y_sci_lin(x), 'm--') #scipy lin
plot(x, y_sci_nearest(x), 'k-') #scipy nearest (zero'th order)
plot(x, y_sci_cubic(x), 'y--') #scipy lin

plot(ip.all_x, ip.all_f_of_x, 'rx') #data
plot(x, ip.analytic_func(x), 'g') #analytical

legend(['scipy linear ip', 'scipy nearest ip', 'scipy cubic ip', 'given data points', 'analytical function'])
xlabel('x')
ylabel('y')
title('Interpolation')
show()