"""Module providing Functions to perform binary search."""
def binary_search(lst: list[int], item: int) -> int:
    """
    Perform a binary search on a list to find the index of a given item.

    Args:
        lst (list): The list to search in.
        item: The item to search for in the list.

    Returns:
        int or None: The index of the item in the list, or None if the item is not found
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, -5))
