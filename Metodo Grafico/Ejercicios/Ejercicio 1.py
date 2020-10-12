import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot 

x, y = symbols('x, y') 

plot_implicit(y < (5-2*x), (x,-100,100), (y,-100,100), title='y < 5-2x', line_color='red')
