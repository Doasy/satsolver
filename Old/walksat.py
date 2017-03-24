#!/usr/bin/python

from RandomSolution import *
from random import randint
from ParseCnfFormula import *
import sys

'''
F <-input CNF formula
for i = 1 to max_tries do
    I <- random interpretation for F
    for j = 1 to max_flips do
        if I satisfies F then
            return I
        endif
        C <- a clause of F not satisfied by I
        S <- set of variables that appear in C
        b <- min({broken(p,F,I) | p in S})
        if b > 0 and with probability w(omega) then
            p <- a variable of S
        else
            p <- a variable of S s.t. broken(p,F,I) = b
        endif
        I <- I with the value of p flipped
    endfor
endfor
return "No solution found".
'''


def broken(C, F, sol):
    broke[0] * len(C)
    for clause in F:
        for literal in clause:
            lit = abs(literal)
            if lit in C and literal != sol[lit]:
                broke[lit] += 1
    return min(broke)


def createDataStruct2(F, initialSol):
    num_sat_lit = [0] * len(F)
    cont = 0
    for clauses in F:
        for literal in clauses:
            if int(literal) == initialSol[abs(int(literal)) - 1]:
                num_sat_lit[cont] += 1
        cont += 1
    return num_sat_lit


def walksat(clauses, n_vars):
     F = clauses
     createDataStruct(clauses, n_vars)
     while(1):
        sol = RandomSolution(n_vars)
        createDataStruct2(clauses, sol)
        for j in xrange(1000):
            C = checkSatisfiability(sol, F)
            if C is True:
                print "s SATISFIABLE"
                print "v " + ' '.join(str(e) for e in sol) + " 0"
                return sol
            # Lacking broken implementation
            to_swap = C[randint(0, len(C) - 1)]
            sol[abs(int(to_swap)) - 1] *= -1


def checkSatisfiability(possibleSolution, cnfFormulaParsed):

    for clause in cnfFormulaParsed:
        if isSatisfiable(possibleSolution, clause) is False:
            return clause
    return True


def isSatisfiable(solution, clause):
    for literal in clause:
        if literal == solution[abs(literal) - 1]:
            return True
    return False


def createDataStruct(clauses, n_var):
    array = []
    for i in xrange(n_var * 2):
        array.append([])

    for c in xrange(len(clauses)):
        for element in clauses[c]:
            if element > 0:
                array[element - 1].append(c)
            else:
                array[element].append(c)

    return array


def createDataStruct2(F, initialSol):
    num_sat_lit = [0] * len(F)
    cont = 0
    for clauses in F:
        for literal in clauses:
            if literal == initialSol[abs(literal) - 1]:
                num_sat_lit[cont] += 1
        cont += 1
    return num_sat_lit


if __name__ == '__main__':

    n_vars, clauses = ParseCnfFormula(open(sys.argv[1], "r"))
    walksat(clauses, n_vars)
