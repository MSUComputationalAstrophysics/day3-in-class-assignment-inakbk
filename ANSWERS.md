The characteristics of functions or chosen intervals [a,b] that tend to break root-finding algorithms: oscillatory functions are hard to find the roots of, and intervals with even nr of roots are hard for some of the methods(?).

The bisection method is very robust, but it uses long convergence time. The Brents method claims to be unbreakable, but I guess it is possible if you find a   function with very poorly behaved derivatives?

Error message (breaking the newtons method):

Traceback (most recent call last):
  File "/Users/Ina/Documents/V2017/Num-astro 905-003/day3-in-class-assignment-inakbk/break_rootfinder.py", line 21, in <module>
    r_newt = optimize.newton(f, x0)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/optimize/zeros.py", line 161, in newton
    raise RuntimeError(msg)
RuntimeError: Failed to converge after 50 iterations, value is 0.00447556684192

The function that broke newtons: f(x) = sin(x)*x^6

Broken because of the many oscillations of the functions, the tagent tries to get closer to the root, but only hits a new point with a tangent pointing further away or to another root --> never converges..