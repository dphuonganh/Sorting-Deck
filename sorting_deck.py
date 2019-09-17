#!/usr/bin/env python3
import argparse


def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', metavar='N', type=int, nargs='+',
                        help='an integer for the list to sort')
    parser.add_argument('--algo', metavar='ALGO',
                        choices=['bubble', 'insert', 'quick', 'merge'],
                        help='''specify which algorithm to use for
                        sorting among [bubble|insert|quick|merge],
                        default bubble''', default='bubble')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    return parser.parse_args()


def bubble_sort(number):
    # Go through the elements of the array
    for i in range(len(number) - 1):
        # The last i elements are already in place t
        for j in range(len(number) - 1):
            change_element(i, j, number)


def change_element(i, j, number):
    # Traverse the array from 0 to n-i-1
    # Swap if the element found is greater than the next element
    if number[j] > number[j + 1]:
        number[j], number[j + 1] = number[j + 1], number[j]
        print(*number)


'''
    Move elements in insertion_sort function of number[0..i-1],
    that are greater than key,
    to one position ahead of their current position.
 '''


def insertion_sort(number):
    size = len(number)
    # Traverse through 1 to len(number)
    for i in range(1, size):
        if number[i] < max(number[:i]):
            key = number[i]
            j = i - 1
            j = get_index(j, number, key)
            number[j + 1] = key
            print(*number)


def get_index(j, number, key):
    while j >= 0 and key < number[j]:
        number[j + 1] = number[j]
        j -= 1
    return j


'''
The main function that implements quick_sort
arr: arr to be sorted
first: starting index
last: ending index
'''


def quick_sort(arr, first, last):
    if first < last:
        # pivot_index is partitioning index
        pivot_index = partition(arr, first, last)
        # sort elements separately before
        # partition and after partition
        quick_sort(arr, first, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, last)


'''
This function takes first element as pivot, places the pivot element at its
correct position in sorted array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right of pivot.
'''


def partition(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    print("P: ", pivot)
    while True:
        while left <= right and arr[left] < pivot:
            left += 1
        while right >= left and arr[right] > pivot:
            right -= 1
        if left > right:
            break
        swap_number(arr, left, right)
        left += 1
        right -= 1
    swap_number(arr, right, first)
    print_list(arr)
    return right


def swap_number(list, index_a, index_b):
    list[index_a], list[index_b] = list[index_b], list[index_a]


def merge_sort(arr):
    if len(arr) > 1:
        # Find the mid of the array
        mid = len(arr) // 2
        # Divide the array elements into 2 halves
        left = arr[:mid]
        right = arr[mid:]
        # Sorting the first half
        merge_sort(left)
        # Sorting the second half
        merge_sort(right)
        i = j = k = 0
        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        print_list(arr)


def print_list(arr):
    """
    Print the list with string type
    """
    number_list = " ".join(str(element) for element in arr)
    print(number_list)


def choose_sort_algo(gui, sort_option, list_number):
    if gui and len(list_number) > 15:  # --gui
        print('You are wrong.')
    elif sort_option == 'bubble':
        bubble_sort(list_number)
    elif sort_option == 'insert':
        insertion_sort(list_number)
    elif sort_option == 'quick':
        quick_sort(list_number, 0, len(list_number) - 1)
    elif sort_option == 'merge':
        merge_sort(list_number)


def main():
    args = handle_arguments()
    gui = args.gui
    sort_option = args.algo
    list_number = args.number
    choose_sort_algo(gui, sort_option, list_number)


if __name__ == "__main__":
    main()
