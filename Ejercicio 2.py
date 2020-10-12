import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot 

x, y = symbols('x, y') 

plot_implicit(y <= 5, (x,-50,50), (y,-50,50), title='y <= 5', line_color='red')