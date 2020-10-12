import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot 

x, y = symbols('x, y') 

plot_implicit(2*(2*x-y)<2*(x+y)-4, (x,-100,100), (y,-100,100), title='2(2x-y)<2(x+y)-4', line_color='red')