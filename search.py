def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    # once implemented, change linear_search to call linear_search_recursive
    #  to verify that your recursive implementation passes all tests
    if(len(array) <= index):
        return None
    elif(array[index] == item):
        return index
    linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    #Set the left to the begging of array and right to end of the array
    left = 0
    right = len(array) - 1

    #Loop through the the array while the left is less than the right
    while left <= right:
        mid = (left + right) // 2 #Get middle index of the array
        if(array[mid] == item): #Return the index if middle = item
            return mid
        else: #Increarse left/right variable based on item < or >
            if item < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    #Set up left and right variables if they are empty
    if(left == None):
        left = 0
        right = len(array) - 1

    #Find the middle of left and right
    mid = (left + right) // 2
    #If item is found return the index
    if left > right:
        return None
    if(array[mid] == item):
        return mid

    #Based on < 0r > to item recursive index +-1
    if (array[mid] > item):
        return binary_search_recursive(array, item, left, mid-1)
    if (array[mid] < item):
        return binary_search_recursive(array, item, mid+1 , right)
