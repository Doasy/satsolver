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
