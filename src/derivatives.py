# Chapter 1 covers some essential derivatives.
# Computation of derivatives I always found challenging.
# Luckily, programming allows for treatment of these elemetned in more abstract concepts

import sympy as sp

x = sp.Symbol('x')
f_of_x = (
    10 -
    0.5 * x ** 2 +
    (sp.ln(1 + x **2)) ** 0.5 -
    ((4 * sp.ln(x)) / sp.exp(x))
)
print(f_of_x)

f_dash_x = f_of_x.diff()

print(f_dash_x)

usable_func = sp.lambdify(x, f_dash_x)

print(usable_func(5))

# In this way, mathematical functions can be defined in code and the computation done using robust packages.