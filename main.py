'''Module main.py'''
import src

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(src.binary_search(my_list, 6))
    print(src.selection_sort([5, 3, 6, 2, 10]))
    print(src.countdown(5))
