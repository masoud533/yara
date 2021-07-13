def Missing(list):
    n = len(list)
    total = (n + 1)*(n + 2)/2
    sum_of_list = sum(list)
    return total - sum_of_list

list = []

while True:
    number = input('Enter a number or press Enter to continue:  ')
    if number == '':
        break
    elif int(number).__int__():
        list.append(int(number))

miss = Missing(list)
print(miss)

