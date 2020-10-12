import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot 

x, y = symbols('x, y') 

plot(180-2*x,(160-x)/2,100-x,0,(x,-100,100), line_color='red', title='Ejercicio 6')
