"""Module providing Functions to calculate factorial of a number."""

def fact_number(number: int) -> int:
    """Returns the factorial of number"""
    j = 1
    if isinstance(number, float):
        raise ValueError("number must be an integer")
    for i in range(2, number + 1):
        j *= i
    return j

# print(fact_number(5))

def factorial(num: int) -> int:
    """Returns the factorial of n"""
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


#print(factorial(5))
