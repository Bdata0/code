'''Module providing Functions to find a smallest number.'''
#def find_smallest(arr: list[int]) -> int:
#    """
#    Find the index of the smallest element in the given array.
#
#    Parameters:
#    - arr (list): A list of integers.
#
#    Returns:
#    - int: The index of the smallest element in the array.
#    """
#    smallest = arr[0]
#    smallest_index = 0
#    for i in range(1, len(arr)):
#        if arr[i] < smallest:
#            smallest = arr[i]
#            smallest_index = i
#    return smallest_index

# better solution below
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
