import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot 

x, y = symbols('x, y') 

plot_implicit(And(2*x+y > 3, 2*y - 1 > 0, x>=y), (x,-10,10), (y,-10,10), title='2x+y > 3 || 2y-1 > 0 || x>=y', line_color='red')