#! /usr/bin/python3
# -*- coding: utf-8


def twoSum(arr, num):
    """
    While an array of integers and a target are given, return indeces in 
    the array that two numbers can sum up to target number
    >>> arr, target = [2, 4, 5, 8, 9, 10], 11
    >>> twoSum(arr, target)
    index1 = 1, index2 = 5
    >>> target = 30
    >>> twoSum(arr, target)
    No matched!
    >>> twoSum([3, 4, 5, 8, 9, 10], 17)
    index1 = 4, index2 = 5
    >>> twoSum([2, 4, 5, 8, 9, 10], 30)
    No matched!
    >>> twoSum([5, 4, 8, 14, 54, 67], 62)
    index1 = 3, index2 = 5
    """
    id1, id2 = 0, 0
    for i in range(len(arr)):
        rest = num - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == rest:
                id1, id2 = i, j
                break
            
    if arr[id1] + arr[id2] != num:
        print("No matched!")
    else:
        print("index1 = %d, index2 = %d" % (id1+1, id2+1))


# arr = [4, 3, 2, 9, 5, 4, 11]
# target = 13

# twoSum(arr, target)

if __name__ == "__main__":
    import doctest
    # Run doctest as: python3 -m *.py -v
    doctest.testmod()
    twoSum([3, 4, 5, 8, 9, 10], 17)
    twoSum([2, 4, 5, 8, 9, 10], 30)
    twoSum([2, 4, 8], 6)