"""14. Longest Common Prefix"""
class LongestCommonPrefixSolution:
    """Class provides Solution for 14.Longest Common Prefix leetcode problem"""
    def description(self):
        """Function provides printing is_palindrome problem description"""
        descript = """
        14. Longest Common Prefix
        (https://leetcode.com/problems/longest-common-prefix/)

        Write a function to find the longest common prefix string amongst
        an array of strings.

        If there is no common prefix, return an empty string "".

        Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

        Example 2:

        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.

        Constraints:
        1 <= strs.length <= 200
        0 <= strs[i].length <= 200
        strs[i] consists of only lowercase English letters.
        """
        return print(descript)


    def longest_common_prefix(self, strs: list[str]) -> str:
        """
        Find the longest common prefix among a list of strings.

        Parameters:
            strs (list[str]): A list of strings to find the longest common prefix from.

        Returns:
            str: The longest common prefix among the given strings.
        """
        if not strs:
            return ""

        prefix = ""

        for char in zip(*strs):  # Using zip to iterate over characters at the same pos.
            if len(set(char)) == 1:
                prefix += char[0]
            else:
                break

        return prefix

    def test_longest_common_prefix(self):
        """Function provides testing longest_common_prefix function"""

        # Test case 1: Empty list
        assert self.longest_common_prefix([]) == ''
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " Empty list" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test case 2: List with one string
        assert self.longest_common_prefix(['abcd']) == 'abcd'
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " List with one string" \
            " \033[2;30;43m passed \033[0;0m"
        )
        # Test case 3: List with two strings, no common prefix
        assert self.longest_common_prefix(['abc', 'def']) == ''
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " List with two strings, no common prefix" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test case 4: List with two strings, common prefix
        assert self.longest_common_prefix(['abc', 'abd']) == 'ab'
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " List with two strings, common prefix" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test case 5: List with multiple strings, common prefix
        assert self.longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " List with multiple strings, common prefix" \
            " \033[2;30;43m passed \033[0;0m"
        )

        # Test case 6: List with multiple strings, no common prefix
        assert self.longest_common_prefix(['dog', 'racecar', 'car']) == ''
        print(
            "\033[48;5;236m\033[38;5;231m Test |" \
            " List with multiple strings, no common prefix" \
            " \033[2;30;43m passed \033[0;0m"
        )

if __name__ == "__main__":
    sol = LongestCommonPrefixSolution()
    sol.description()
    sol.test_longest_common_prefix()
