#!/usr/bin/env python3
import random

def randdec():
    '''
    Returns a random number between 0 and 1
    '''
    rand1 = random.randint(0,100)
    rand2 = random.randint(0,100)
    if rand1>rand2:
        return (rand2/rand1)
    return(rand1/rand2)
import sys
from sympy import symbols, Symbol
from sympy.solvers import solve
from sympy.parsing.sympy_parser import parse_expr,\
standard_transformations,\
implicit_multiplication_application
from sympy.plotting import plot

if len(sys.argv) is 0:
    print("Please enter a function as an argument")
    exit()
#number of contour lines.
numc=5
#if len(sys.argv) is 2:
    #make default step function
    #if int(sys.argv[2]): sys.argv[2] else: quit()
func = parse_expr(sys.argv[1].replace('^','**'), transformations=\
(standard_transformations + (implicit_multiplication_application,)))
y = Symbol('y')
contour_map = None
#the number of undefined answers or constant answers to the gived function
#ex: 0/0 or y=0
total_lines=0
for i in range(0,numc, 1):
    contours = solve(func-i,y)
    for n,line in enumerate(contours):
        print("Graphing line: y=", line, end='\r');
        if contour_map is None:
            contour_map = plot(line, show=False)
            contour_map[0].label='k=%d'%i
            contour_map[0].line_color=(randdec(),randdec(),randdec())
        elif n is 0:
            contour_map.extend(plot(line, show=False))
            total_lines+=1
            contour_map[total_lines].label='k=%d'%i
            contour_map[total_lines].line_color=(randdec(),randdec(),randdec())
        else:
            contour_map.extend(plot(line, show=False))
            total_lines+=1
            contour_map[total_lines].label=''
            contour_map[total_lines].line_color=contour_map[total_lines-n].line_color
print("\nDone")
contour_map.legend = True
contour_map.show()
