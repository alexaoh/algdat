"""Implementation of insertion sort."""

def insertion_sort(array):
    """Implementation of insertion sort. Sorts the array 'array'. """
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while array[j] > temp and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

# Test
A = [7, 5, 3, 2, 6, 4]
print("Unsorted", A)
insertion_sort(A)
print("Sorted", A)
