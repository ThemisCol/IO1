import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot 

x, y = symbols('x, y') 

plot_implicit(And((2*x+3*y)<=60, x >= 0, y >= 0), (x,-40,40), (y,-40,40), title='2x+3y <= 60 || x >= 0 || y >= 0', line_color='red')