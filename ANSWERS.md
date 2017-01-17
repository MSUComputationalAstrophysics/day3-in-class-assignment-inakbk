

brents need very poorly behaved derivatives to break?
påstår selv at er uslåelig



Error message (breaking the newtons method):

Traceback (most recent call last):
  File "/Users/Ina/Documents/V2017/Num-astro 905-003/day3-in-class-assignment-inakbk/break_rootfinder.py", line 21, in <module>
    r_newt = optimize.newton(f, x0)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/optimize/zeros.py", line 161, in newton
    raise RuntimeError(msg)
RuntimeError: Failed to converge after 50 iterations, value is 0.00447556684192

The function that broke newtons: f(x) = sin(x)*x^6

Broken because of the many oscillations of the functions, the tagent tries to 