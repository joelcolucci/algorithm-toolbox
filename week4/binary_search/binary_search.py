# Uses python2
import sys

def binary_search(array, x):
    high = len(array) - 1 # Offset to handle zero indexed array
    low = 0

    while low <= high:
        mid = (low + high) / 2

        if x == array[mid]:
            return mid
        elif x < array[mid]:
            high = mid - 1
        elif x > array[mid]:
            low = mid + 1

    return -1

    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    data = [int(i) for i in sys.stdin.read().split()]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print str(binary_search(a, x)) + ' '
