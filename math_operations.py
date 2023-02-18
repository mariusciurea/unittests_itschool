"""Math operations - division and multiplication"""


def inmultire(num1, num2):
    return num1 * num2


def impartire(num1, num2):
    if num2 == 0:
        raise ValueError('2nd number must be != 0!!!')
    return num1/num2

    # try:
    #     result = num1/num2
    #     return num1 / num2
    # except ZeroDivisionError as e:
    #     print('cannot divide by 0!!!')
    #     return


