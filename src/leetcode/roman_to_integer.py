"""13. Roman to Integer"""
class RomanToIntegerSolution(object):
    """Class provides Solution for 13.Roman to Integer leetcode problem"""
    def description(self):
        """Function provides printing two_sum problem description"""
        descript = """
        13. Roman to Integer
        (https://leetcode.com/problems/roman-to-integer/)

        Roman numerals are represented by seven different symbols: I,V,X,L,C,D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        For example, 2 is written as II in Roman numeral, just two ones added together.
        12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
        which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right.
        However, the numeral for four is not IIII. Instead, the number four is written
        as IV. Because the one is before the five we subtract it making four.
        The same principle applies to the number nine, which is written as IX.

        There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.

        Example 1:

        Input: s = "III"
        Output: 3
        Explanation: III = 3.

        Example 2:

        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.

        Example 3:

        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


        Constraints:
        1 <= s.length <= 15
        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        It is guaranteed that s is a valid roman numeral in the range [1, 3999].
        """
        return print(descript)

    def roman_to_int(self, input_str: str) -> int:
        """
        Convert a Roman numeral to an integer.

        Parameters:
        - input_str (str): The Roman numeral to be converted.

        Returns:
        - int: The corresponding integer value of the Roman numeral.
        """
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        res = 0

        for i, char in enumerate(input_str):
            if i+1 < len(input_str) and roman[char] < roman[input_str[i+1]]:
                res -= roman[char]
            else:
                res += roman[char]

        return res

    def test_roman_to_int(self):
        """Function provides testing roman_to_integer function"""

        # Test cases with single Roman numerals
        assert self.roman_to_int("I") == 1
        assert self.roman_to_int("V") == 5
        assert self.roman_to_int("X") == 10
        assert self.roman_to_int("L") == 50
        assert self.roman_to_int("C") == 100
        assert self.roman_to_int("D") == 500
        assert self.roman_to_int("M") == 1000
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " single Roman numerals" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test cases with subtractive notation
        assert self.roman_to_int("IV") == 4
        assert self.roman_to_int("IX") == 9
        assert self.roman_to_int("XL") == 40
        assert self.roman_to_int("XC") == 90
        assert self.roman_to_int("CD") == 400
        assert self.roman_to_int("CM") == 900
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " subtractive notation" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test cases with multiple Roman numerals
        assert self.roman_to_int("III") == 3
        assert self.roman_to_int("XII") == 12
        assert self.roman_to_int("XXIV") == 24
        assert self.roman_to_int("XXXIX") == 39
        assert self.roman_to_int("CCLXVIII") == 268
        assert self.roman_to_int("MCMXCIX") == 1999
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " multiple Roman numerals" \
            " \033[2;30;43m passed \033[0;0m"
        )


if __name__ == "__main__":
    sol = RomanToIntegerSolution()
    sol.description()
    sol.test_roman_to_int()
