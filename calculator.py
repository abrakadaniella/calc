import pyinputplus as pyip


def plus(num_1, num_2):
    return num_1 + num_2


def minus(num_1, num_2):
    return num_1 - num_2


def division(num_1, num_2):
    return num_1 / num_2


def mult(num_1, num_2):
    return num_1 * num_2


def perc(num_1, num_2):
    return num_1 * (num_2 / 100)


def operations(operation, first_num, second_num):
    result = 0
    if operation == '+':
        result = plus(first_num, second_num)
    elif operation == '-':
        result = minus(first_num, second_num)
    elif operation == '/':
        try:
            result = division(first_num, second_num)
        except ZeroDivisionError:
            print("You cannot divide by 0, please try again")
            calc()
    elif operation == '*':
        result = mult(first_num, second_num)
    elif operation == '%':
        result = perc(first_num, second_num)
    return result


def more_actions():
    action = pyip.inputMenu(['I want to make more calculations', 'I\'m done, bye'], numbered=True)
    if action == 'I want to make more calculations':
        calc()
    elif action == 'I\'m done, bye':
        print("Thank you for using the calculator, hope it was helpful!")


def calc():
    operation = pyip.inputMenu(['+', '-', '/', '*', '%'])
    first_num = pyip.inputInt(prompt="Please enter the first number:\n")
    second_num = pyip.inputInt(prompt="Please enter the second number(or the whole percent):\n")
    answer = operations(operation, first_num, second_num)
    if operation == '%':
        print("\n{n2}% of {n1} = {a}\n".format(n2=second_num, n1=first_num, a=answer))
    else:
        print("\n{n1} {op} {n2} = {a}\n".format(n1=first_num, n2=second_num, op=operation, a=answer))
    more_actions()


calc()