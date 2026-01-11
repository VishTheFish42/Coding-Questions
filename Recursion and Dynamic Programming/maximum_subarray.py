'''
MAXIMUM SUBARRAY
Given an array of integers, return the starting index and ending index of the subarray that has the largest sum.
Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> [3, 6] because 4 + -1 + 2 + 1 = 6 is the largest sum possible.
'''

def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    return [best_start, best_end]
