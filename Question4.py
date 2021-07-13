X = int(input('Put a lower number:  '))
y = int(input('Enter the large number:  '))
operation = 0
if X < y:
    while X <= y:
        X += 1
        X = X * 2
        operation += 1
else:
    print('Please be careful when entering numbers')

print(f'Number of operations: {operation}')
