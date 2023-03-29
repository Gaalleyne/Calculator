def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def expo (num):
    return num * num

def solve(expr : list, value=0):
        result = 0

        while (len(expr) != 1) or ('x' in str(expr[0])):
            for obj in expr:

                if 'x' in str(obj):
                    expr.insert(expr.index(obj) + 1, str(value))

                    if len(str(obj)) > 1:
                        expr.insert(expr.index(obj) + 1, '*')
                        expr[expr.index(obj)] = obj[0:1]
                    else:
                        del expr[expr.index(obj)]

            if ('(' in expr) and (')' in expr):
                left_par = expr.index('(')
                right_par = 0
                par = expr.index('(')
                par_count = 0

                while True:
                    if '(' in expr[par:] and (expr.index('(', par) < expr.index(')', par)):
                        par = expr.index('(', par) + 1
                        par_count += 1

                    # Analyzing layers of parenthesis
                    elif par_count > 0:
                        while par_count != 0:
                            right_par = expr.index(')', par)
                            par = expr.index(')', par) + 1
                            par_count -= 1

                        par = len(expr) + 1

                    else:
                        break
                
                sub_equation = list(expr[left_par+1:right_par])

                sub_result = solve(sub_equation)
                expr[left_par] = sub_result
                del expr[left_par+1:right_par+1]

            elif ('\u00b2' in expr):

                expr[expr.index('\u00b2') - 1] = expo(float(expr[expr.index('\u00b2') - 1]))
                del expr[expr.index('\u00b2')]

            if ('*' in expr) or ('/' in expr):
                
                ind_mul = expr.index('*') if ('*' in expr) else len(expr) + 1
                ind_div = expr.index('/') if ('/' in expr) else len(expr) + 1

                if ind_mul < ind_div:
                    expr[ind_mul-1] = multiply(float(expr[ind_mul-1]), float(expr[ind_mul+1]))
                    expr.pop(ind_mul+1)
                    expr.remove('*')
                else:
                    expr[ind_div-1] = divide(float(expr[ind_div-1]), float(expr[ind_div+1]))
                    expr.pop(ind_div+1)
                    expr.remove('/')

            elif ('+' in expr) or ('-' in expr):
                ind_add = expr.index('+') if ('+' in expr) else len(expr) + 1
                ind_sub = expr.index('-') if ('-' in expr) else len(expr) + 1

                if ind_add < ind_sub:
                    expr[ind_add-1] = add(float(expr[ind_add-1]), float(expr[ind_add+1]))
                    expr.pop(ind_add+1)
                    expr.remove('+')
                else:
                    expr[ind_sub-1] = subtract(float(expr[ind_sub-1]), float(expr[ind_sub+1]))
                    expr.pop(ind_sub+1)
                    expr.remove('-')

        result = float(expr[0]) if (str(expr[0])[-2:] == '.0') else float(expr[0])
        return result