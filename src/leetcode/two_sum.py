"""1. Two Sum"""
class TwoSumSolution:
    """Class provides Solution for 1.Two Sum leetcode problem"""
    def description(self):
        """Function provides printing two_sum problem description"""
        descript = """
        1. Two Sum
        (https://leetcode.com/problems/two-sum/)

        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.

        You can return the answer in any order.

        Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]


        Constraints:

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.


        Follow-up: Can you come up with an algorithm
        that is less than O(n2) time complexity?
        """
        return print(descript)

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in the given list `nums`
        that add up to the target number `target`.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the indices
            of the two numbers that add up to the target sum.
        """
        hash_map = {}  # val:index
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], idx]
            hash_map[num] = idx
        return

    def test_two_sum(self):
        """Function provides testing two_sum function"""
        # Test case 1: Basic input
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.two_sum(nums, target)
        assert result == expected, f"Expected {expected}, but got {result}"
        print(
            f"\033[48;5;236m\033[38;5;231m Test |" \
            f" nums = {nums}," \
            f" target = {target}," \
            f" expected: {expected} " \
            f" \033[2;30;43m passed \033[0;0m"
        )

        # Test case 2: No solution
        nums = [2, 7, 11, 15]
        target = 10
        expected = None
        result = self.two_sum(nums, target)
        assert result == expected, f"Expected {expected}, but got {result}"
        print(
            f"\033[48;5;236m\033[38;5;231m Test |" \
            f" nums = {nums}," \
            f" target = {target}," \
            f" expected: {expected} " \
            f" \033[2;30;43m passed \033[0;0m"
        )

        # Test case 3: Multiple solutions
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.two_sum(nums, target)
        assert result == expected, f"Expected {expected}, but got {result}"
        print(
            f"\033[48;5;236m\033[38;5;231m Test |" \
            f" nums = {nums}," \
            f" target = {target}," \
            f" expected: {expected} " \
            f" \033[2;30;43m passed \033[0;0m"
        )

if __name__ == "__main__":
    sol = TwoSumSolution()
    sol.description()
    sol.test_two_sum()
