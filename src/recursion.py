'''Module provides recursion functions.'''
def countdown(i: int) -> int:
    """
    countdown is a function that takes
    an integer parameter i and returns an integer value.
    """
    print(i)
    if i <= 0:
        return 0
    else:
        countdown(i - 1)

#print(countdown(5))
