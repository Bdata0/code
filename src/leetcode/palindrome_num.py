"""9. Palindrome Number"""
class IsPalindromeSolution:
    """Class provides Solution for 9.Palindrome Number leetcode problem"""
    def description(self):
        """Function provides printing is_palindrome problem description"""
        descript = """
        9. Palindrome Number
        (https://leetcode.com/problems/palindrome-number/)

        Given an integer num, return true if num is a palindrome, and false otherwise.

        Example 1:

        Input: num = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.

        Example 2:

        Input: num = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left,
        it becomes 121-. Therefore it is not a palindrome.

        Example 3:

        Input: num = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


        Constraints:
        -231 <= num <= 231 - 1

        Follow up: Could you solve it without converting the integer to a string?
        """
        return print(descript)

    def is_palindrome(self, num: int) -> bool:
        """
        Check if a given number is a palindrome.

        Parameters:
            num (int): The number to be checked.

        Returns:
            bool: True if the number is a palindrome, False otherwise.
        """
        return False if num < 0 else num == int(str(num)[::-1])

    def test_is_palindrome(self):
        """Function provides testing is_palindrom function"""
        # Test cases for positive numbers
        assert self.is_palindrome(121) is True
        assert self.is_palindrome(12321) is True
        assert self.is_palindrome(12345) is False
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " positive numbers" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test cases for negative numbers
        assert self.is_palindrome(-121) is False
        assert self.is_palindrome(-12321) is False
        assert self.is_palindrome(-12345) is False
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " negative numbers" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test cases for single digit numbers
        assert self.is_palindrome(0) is True
        assert self.is_palindrome(1) is True
        assert self.is_palindrome(9) is True
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " single digit numbers" \
            " \033[2;30;43m passed \033[0;0m"
        )

if __name__ == "__main__":
    sol = IsPalindromeSolution()
    sol.description()
    sol.test_is_palindrome()
