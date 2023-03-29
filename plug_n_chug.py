from aggieCalcOperations import solve

def createTable(expression : str, value : int):
    
    list_expr = expression.split(' ')
    find_y = 0

    find_y = solve(list_expr, value)

    return find_y