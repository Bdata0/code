'''Module main.py'''
import src
import src.leetcode

MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
UNSORTED_LIST = [5, 3, 6, 2, 10]
NUM = 5

def two_sum_output():
    """
    This function calls the description and test methods of the `Solution` class
    from the `src.leetcode.two_sum` module.
    """
    sol = src.leetcode.two_sum.Solution()
    sol.description()
    sol.test_two_sum()

if __name__ == "__main__":

    print(f'The position #{NUM} in {MY_LIST} is {src.binary_search(MY_LIST, NUM)}')
    print(f'Binary-sorted list: {src.selection_sort(UNSORTED_LIST)}')
    print(f'The end of recursion: {src.countdown(NUM)}')
    print(f'The factorial of {NUM} is equal to {src.fact_number(NUM)}')

    two_sum_output()
