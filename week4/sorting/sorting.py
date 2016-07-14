# Uses python2


import sys
import random


# BAD
# When we do this j could very well be
# a repeated element! This means we swap
# the same element to the end of array!
# We now have to find a way to deal with
# shifting matching elements

# Flop j to k + 1
# If j is equal to pivot we are fine
# If j is greater than pivot we are fine


def partition3(array, start_index, end_index):
    pivot_index = start_index
    pivot_value = array[pivot_index]

    # Partition values
    # j equals first GREATER THAN
    # This is why we swap to j - 1
    # to ensure a the upper stays upper
    # print array
    j = start_index + 1
    k = start_index + 1
    for i in range(start_index + 1, end_index + 1):
        if array[i] < pivot_value:
            if k > j:
                # Flip j to k
                temp_low = array[i]

                array[i] = array[k]
                array[k] = array[j]
                array[j] = temp_low
            else:
                # Swap to lower partition
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

            # Increment upper partition index
            j += 1
            k += 1
        elif array[i] == pivot_value:
            temp = array[i]
            array[i] = array[k]
            array[k] = temp
            k += 1

    # Swap pivot value to final place
    final_pivot_index = j - 1

    array[pivot_index] = array[final_pivot_index]
    array[final_pivot_index] = pivot_value

    return j - 1, k - 1


def randomized_quick_sort(array, start_index, end_index):
    # print "\n"
    # print array
    # print "start index: " + str(start_index)
    # print "end index: " + str(end_index)
    if start_index >= end_index:
        return

    # Get the partition index
    pivot_index = random.randint(start_index, end_index)
    # print "pivot index: " + str(pivot_index)

    # Swap partition index to front of array
    temp = array[start_index]
    array[start_index] = array[pivot_index]
    array[pivot_index] = temp

    #use partition3
    m1, m2 = partition3(array, start_index, end_index)

    # print "m1: " + str(m1)
    # print "m2: " + str(m2)
    # print "array: " + str(array) + '\n'

    randomized_quick_sort(array, start_index, m1 - 1)
    randomized_quick_sort(array, m2 + 1, end_index)


if __name__ == '__main__':
    a = [int(i) for i in sys.stdin.read().split()]
    n = a[0]

    array = a[1:]
    randomized_quick_sort(array, 0, n - 1)
    for x in array:
        print str(x) + ' '
