def my_func(var_1, var_2, var_3):
    var_sum = var_1 + var_2 + var_3
    return var_sum - min(var_1, var_2, var_3)


print(my_func(int(input('enter number: ')), int(input('enter number: ')), int(input('enter number: '))))
