#!/usr/bin/env python3
import random
import sys
import argparse
from sympy import symbols, Symbol
from sympy.solvers import solve
from sympy.parsing.sympy_parser import parse_expr,\
standard_transformations,\
implicit_multiplication_application
from sympy.plotting import plot
def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="The function to graph contour lines from")
    parser.add_argument("number_contours", help="The number of contour lines to display", type=int, nargs='?')
    parser.add_argument("step",help="the step of x between contour lines",type=int, default=1, nargs='?')
    args=parser.parse_args()
    #number of contour lines.
    numc = args.number_contours if args.number_contours else 5
    #step between contour lines
    step = args.step if args.step else 1
    func = parse_expr(args.function.replace('^','**'), transformations=\
    (standard_transformations + (implicit_multiplication_application,)))
    y = Symbol('y')
    contour_map = None
    #the number of undefined answers or constant answers to the given function
    #ex: 0/0 or y=0
    total_lines=0
    for i in range(0,numc, step):
        contours = solve(func-i,y)
        #import pdb; pdb.set_trace()
        if str(contours[0]).isdigit():
            continue
        for n,line in enumerate(contours):
            print("Graphing line: y=", str(line).replace('**','^'), end='\r');
            if contour_map is None:
                contour_map = plot(line, show=False)
                contour_map[0].label='k=%d'%i
                contour_map[0].line_color=(random.random(),random.random(),random.random())
            elif n is 0:
                contour_map.extend(plot(line, show=False))
                total_lines+=1
                contour_map[total_lines].label='k=%d'%i
                contour_map[total_lines].line_color=(random.random(),random.random(),random.random())
            else:
                contour_map.extend(plot(line, show=False))
                total_lines+=1
                contour_map[total_lines].label=''
                contour_map[total_lines].line_color=contour_map[total_lines-n].line_color
    try:
        contour_map.legend = True
    except AttributeError:
        print("Please ensure your function is three dimensional")
        exit()
    print("\nDone")
    contour_map.show()
if __name__=='__main__':
    main(sys.argv[1:])
