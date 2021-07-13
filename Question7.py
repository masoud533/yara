number1 = int(input('enter nunber1: '))
number2 = int(input('enter nunber2: '))
number3 = number2 - 1
if __name__ == '__main__':

    for first in range(number1, number2):
        for second in range(number1, number2):
            print(number3 * first + second - number3)
