#python2



def calculate_max_pairwise_product(array, n):
    """Calculate the max pairwise product"""
    max_index = 0
    for i in range(0, n):
        if array[i] > array[max_index]:
            max_index = i

    # Zero out max value from array so we can use same algorithm to find second largest
    max_num = array[max_index]
    array[max_index] = 0

    sec_max_index = 0

    for i in range(0, n):
        if array[i] > array[sec_max_index]:
            sec_max_index = i

    sec_max_num = array[sec_max_index]

    return max_num * sec_max_num


if __name__ == '__main__':
    n = int(raw_input())
    array = [int(x) for x in raw_input().split()]

    assert(len(array) == n)

    result = calculate_max_pairwise_product(array, n)

    print(result)
