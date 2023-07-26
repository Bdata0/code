'''Module providing Functions to sort a selectioned list.'''
def find_smallest(arr: list[int]) -> int:
    """
    Find the index of the smallest element in the given array.

    Parameters:
    - arr (list): A list of integers.

    Returns:
    - int: The index of the smallest element in the array.
    """
    smallest_index = 0
    for i, num in enumerate(arr):
        if num < arr[smallest_index]:
            smallest_index = i
    return smallest_index

def selection_sort(arr: list[int]) -> list[int]:
    """
    Sorts the given list in ascending order using the selection sort algorithm.

    Parameters:
        arr (list[int]): The list to be sorted.

    Returns:
        list[int]: The sorted list.
    """
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

#print(selection_sort([5, 3, 6, 2, 10]))
