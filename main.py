'''Module main.py'''
import src
import src.leetcode

MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
UNSORTED_LIST = [5, 3, 6, 2, 10]
NUM = 5

def two_sum_output():
    """
    This function calls the description and test methods of the `TwoSumSolution` class
    from the `src.leetcode.two_sum` module.
    """
    sol = src.leetcode.two_sum.TwoSumSolution()
    sol.description()
    sol.test_two_sum()

def is_palindrome_output():
    """
    This function calls the description and test methods of the `IsPalindromeSolution`
    class from the `src.leetcode.palindrome_num` module.
    """
    sol = src.leetcode.palindrome_num.IsPalindromeSolution()
    sol.description()
    sol.test_is_palindrome()

def roman_to_integer_output():
    """
    This function calls the description and test methods of the `RomanToIntegerSolution`
    class from the `src.leetcode.roman_to_integer` module.
    """
    sol = src.leetcode.roman_to_integer.RomanToIntegerSolution()
    sol.description()
    sol.test_roman_to_int()

def longest_common_prefix_output():
    """
    This function calls the description and test methods of the
    `LongestCommonPrefixSolution` class from the `src.leetcode.longest_common_prefix`
    module.
    """
    sol = src.leetcode.longest_common_prefix.LongestCommonPrefixSolution()
    sol.description()
    sol.test_longest_common_prefix()

if __name__ == "__main__":

    print(f'The position #{NUM} in {MY_LIST} is {src.binary_search(MY_LIST, NUM)}')
    print(f'Binary-sorted list: {src.selection_sort(UNSORTED_LIST)}')
    print(f'The end of recursion: {src.countdown(NUM)}')
    print(f'The factorial of {NUM} is equal to {src.fact_number(NUM)}')

    two_sum_output()
    is_palindrome_output()
    roman_to_integer_output()
    longest_common_prefix_output()
