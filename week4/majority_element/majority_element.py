# Uses python2


import sys


def get_majority_element(array, start_index, end_index):
    """Return majority element else -1"""
    if start_index == end_index:
        return array[start_index]

    # Define bounds
    mid = (start_index + end_index) / 2

    left_start = start_index
    left_end = mid

    right_start = mid + 1
    right_end = end_index

    maj_one = get_majority_element(array, left_start, left_end)
    if maj_one > -1:
        count = 0
        for i in range(left_start, right_end + 1):
            if array[i] == maj_one:
                count += 1
        if count > ((right_end - left_start + 1) / 2):
            return maj_one

    maj_two = get_majority_element(array, right_start, right_end)
    if maj_two > -1:
        count = 0
        for i in range(left_start, right_end + 1):
            if array[i] == maj_two:
                count += 1
        if count > ((right_end - left_start + 1) / 2):
            return maj_two

    return -1


if __name__ == '__main__':
    a = [int(i) for i in sys.stdin.read().split()]
    n = a[0]

    if get_majority_element(a[1:], 0, n - 1) != -1:
        print(1)
    else:
        print(0)
