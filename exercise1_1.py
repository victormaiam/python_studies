""""
Write a function that returns the maximum of two numbers.
"""

def getDivisors(number):
    divisors = []
    c = 1
    while c <= number:
        if number % c == 0:
            divisors.append(c)
        c = c+1
    return divisors


def getMaximum(number_divisor1, number_divisor2):
    number_divisor1 = getDivisors(number1)
    number_divisor2 = getDivisors(number2)
    mdc = 1
    for x in number_divisor1:
        if x in number_divisor2 and x > mdc:
            mdc = x
    return mdc
    

number1 = int(input("> "))
number2 = int(input("> "))
print(getMaximum(number_divisor1, number_divisor2))