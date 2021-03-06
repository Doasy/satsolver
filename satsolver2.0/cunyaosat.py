#!/usr/bin/python


from random import *
import sys

def runsat(clauses, n_vars):
    F = clauses
    literals_in_clauses = createDataStruct(F, n_vars)
    # print "Literals: " + str(literals_in_clauses)
    while(1):

        sol = RandomSolution(n_vars)
        num_sat_lit = createDataStruct2(F, sol)

        for i in xrange(3*n_vars):

            positions_with_zero = [i for i, j in enumerate(num_sat_lit) if j == 0]

            if len(positions_with_zero) == 0:

                return printer(sol)

            x = positions_with_zero[randint(0, len(positions_with_zero)-1)]
            
            broken_info = broken(F[x], num_sat_lit, literals_in_clauses, sol)    

            if broken_info[1] > 0 and random() < 0.30 :
                to_swap = abs(F[x][randint(0, len(F[0]) - 1)])
            else:
                to_swap = broken_info[0]

            swapper(num_sat_lit, literals_in_clauses, to_swap, sol)

def printer(sol):

    print "s SATISFIABLE"
    print "v " + ' '.join(str(e) for e in sol) + " 0"
    return sol

def swapper(num_sat_lit, literals_in_clauses, to_swap, sol):

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
            for element in literals_in_clauses[-abs(literal)]:
                if num_sat_lit[element] == 1:
                    broken += 1
        else:
            for element in literals_in_clauses[abs(literal) - 1]:
                if num_sat_lit[element] == 1:
                    broken += 1
        if broken < minimum:
            minimum = broken
            to_swap = literal
    return abs(to_swap), minimum


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

def RandomSolution(n_var):
    sol = range(1, n_var+1)
    for i in xrange(len(sol)):
        if random() < 0.5:
            sol[i] *= -1
    return sol

def ParseCnfFormula(CNF):
    clauses = []
    n_vars = 0
    for line in CNF:
        line = line.split()
        if line[0] != 'c' and line[0] != 'p':
            clauses.append([int(x) for x in line[:-1]])
        elif line[0] == 'p':
            n_vars = line[2]
    return int(n_vars), clauses

if __name__ == '__main__':

    n_vars, clauses = ParseCnfFormula(open(sys.argv[1], "r"))
    runsat(clauses, n_vars)
