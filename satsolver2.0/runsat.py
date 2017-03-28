#!/usr/bin/python

from RandomSolution import *
from random import *
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

# positions_with_zero = [i for i, j in enumerate(num_sat_lit) if j == 0]
# x = positions_with_zero[randint(0, len(positions_with_zero)-1)]


def runsat(clauses, n_vars):
    F = clauses
    literals_in_clauses = createDataStruct(F, n_vars)
    # print "Literals: " + str(literals_in_clauses)
    while(1):
        sol = RandomSolution(n_vars)
        num_sat_lit = createDataStruct2(F, sol)
        for i in xrange(3 * n_vars):
            # print num_sat_lit
            positions_with_zero = [
                i for i, j in enumerate(num_sat_lit) if j == 0]
            if len(positions_with_zero) == 0:
                print "s SATISFIABLE"
                print "v " + ' '.join(str(e) for e in sol) + " 0"
                return sol
            x = positions_with_zero[randint(0, len(positions_with_zero) - 1)]
            # print "x:"+str(x)
            # for x in range(len(num_sat_lit)):
            if num_sat_lit[x] == 0:
                # print "x:"+str(x)
                if random() < 0.25:
                    to_swap = abs(F[x][randint(0, len(F[0]) - 1)])
                else:
                    to_swap = broken(F[x], num_sat_lit,
                                     literals_in_clauses, sol)
                # break

            if sol[to_swap - 1] < 0:
                for element in literals_in_clauses[to_swap - 1]:
                    num_sat_lit[element] += 1
                for element in literals_in_clauses[-to_swap]:
                    num_sat_lit[element] -= 1
            else:
                for element in literals_in_clauses[to_swap - 1]:
                    num_sat_lit[element] -= 1
                for element in literals_in_clauses[-to_swap]:
                    num_sat_lit[element] += 1
            sol[to_swap - 1] *= -1


def broken(clause, num_sat_lit, literals_in_clauses, sol):

    minimum = 10000
    for literal in clause:
        broken = 0
        if sol[abs(literal) - 1] < 0:
            '''for element in literals_in_clauses[abs(literal) - 1]:
                if num_sat_lit[element] == 0:
                    broken -= 1'''
            for element in literals_in_clauses[-abs(literal)]:
                if num_sat_lit[element] == 1:
                    broken += 1
        else:
            for element in literals_in_clauses[abs(literal) - 1]:
                if num_sat_lit[element] == 1:
                    broken += 1
            '''for element in literals_in_clauses[-abs(literal)]:
                if num_sat_lit[element] == 0:
                    broken -= 1'''
        if broken < minimum:
            minimum = broken
            to_swap = literal
    return abs(to_swap)


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
    runsat(clauses, n_vars)
