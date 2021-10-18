def sum_nums(nums_str, stop):
    nums_list = nums_str.split(' ')
    sums_list = 0
    for i in nums_list:
        if i == stop:
            break
        sums_list += int(i)
    return sums_list


stopper = '$'
finished = False
sum_ = 0
while not finished:
    nums_str_input = input('enter number separated by space: ')
    sum_ += sum_nums(nums_str_input, stopper)
    finished = stopper in nums_str_input
    print(f'Sum = {sum_}')
