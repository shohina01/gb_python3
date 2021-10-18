def division(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        var_2 = 0
        return 'ZeroDivisionError'


print(division(10, 0))

