def checkSatisfiability(possibleSolution, cnfFormulaParsed):

    for formula in cnfFormulaParsed:
        if isSatisfiable(possibleSolution, clause) is False:
            return False
    return True


def isSatisfiable(solution, formula):
    for element in formula:
        if int(element) == solution[abs(int(element)) - 1]:
            return True
    return False
