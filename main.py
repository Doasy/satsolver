#!/usr/bin/python

from satsolver import *
from RandomSolution import RandomSolution
from ParseCnfFormula import *
import sys


if __name__ == '__main__':

    n_vars, clauses = ParseCnfFormula(open(sys.argv[1], "r"))
    sat = 0

    for x in xrange(20000000000):

        solution = RandomSolution(n_vars)
        if checkSatisfiability(solution, clauses) is True:
            print "s SATISFIABLE"
            print "v " + ' '.join(str(e) for e in solution)
            sat = 1
            break
    if sat == 0:
        print "Insatisfiable"
