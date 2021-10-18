def my_func(x, y):
    pow_ = 1
    for i in range(y * (-1)):
        pow_ *= x
    return 1 / pow_


print(my_func(x=float(input('enter number: ')), y=int(input('enter negative number: '))))
