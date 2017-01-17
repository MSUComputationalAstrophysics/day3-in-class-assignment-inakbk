#in-class 3

from pylab import *
from scipy import optimize

def breaking_function1(x):
	return sin(x)*x**6

#interval
a = -10
b = 10
#guess
x0 = 1

x = linspace(a, b, 1000)
f = breaking_function1
plot(x, f(x), 'b')

#scipy methods:
r_bisect = optimize.bisect(f, a, b)
r_newt = optimize.newton(f, x0)
r_brent = optimize.brentq(f, a, b)

print 'roots:', r_bisect, r_newt, r_brent

plot(r_bisect, f(r_bisect), 'ro')
plot(r_brent, f(r_brent), 'ko')
plot(r_newt, f(r_newt), 'go')

legend(['function', 'bisection', 'brents', 'newtons'])

show()