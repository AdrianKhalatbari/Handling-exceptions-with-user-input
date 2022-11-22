import math

while True:
    print("What do you want to do:")
    print("1) Test for ValueError")
    print("2) Test for IndexError")
    print("3) Test for ZeroDivisionError")
    print("4) Test for TypeError")
    print("0) Stop")
    try:
        while True:
            try:
                choice = int(input("Your choice:"'\n'))
                break
            except ValueError:
                print('ValueError happened. Enter the selection as an integer.')
        if choice == 1:
            value_input = int(input("Give a non-negative integer:\n"))
            try:
                print(f'Square Root of {value_input} is {math.sqrt(value_input)}')
            except ValueError:
                print('ValueError happened. Non-negative number expected for square root.')
        if choice == 2:
            index_input = int(input('Input index 0-4:''\n'))
            if index_input > 4 or index_input < 0:
                raise IndexError('Got an IndexError, index {}.'.format(index_input))
        if choice == 3:
            divider = int(input("Enter divider:\n"))
            try:
                float(10 / int(divider))
            except ZeroDivisionError:
                print("ZeroDivisionError occurred, divider 0.")
        if choice == 4:
            type_input = input("Enter number:\n")
            print(type_input * type_input)
        if choice == 0:
            break


    except IndexError as ve:
        print('Got an IndexError, index {}.'.format(index_input))
    except TypeError as ve:
        print('Got TypeError, ' + str(type_input + '*' + type_input) + ' with strings failed.'.format(type_input))
