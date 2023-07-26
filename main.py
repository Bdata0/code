'''Module main.py'''
import src

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unsorted_list = [5, 3, 6, 2, 10]
num = 5

if __name__ == "__main__":

    print(f'The position #{num} in {my_list} is {src.binary_search(my_list, num)}')
    print(f'Binary-sorted list: {src.selection_sort(unsorted_list)}')
    print(f'The end of recursion: {src.countdown(num)}')
    print(f'The factorial of {num} is equal to {src.fact_number(num)}')
