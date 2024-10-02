# Non-Random Pivot Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  
        left = [x for x in arr[:-1] if x <= pivot]  
        right = [x for x in arr[:-1] if x > pivot]  
        return quicksort(left) + [pivot] + quicksort(right)


# Random Pivot Quicksort
import random

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)  
        pivot = arr[pivot_index]
        left = [x for x in arr if x < pivot]  
        right = [x for x in arr if x > pivot] 
        equal = [x for x in arr if x == pivot]  
        return quicksort_random(left) + equal + quicksort_random(right)


# Test cases
arr = [10, 7, 8, 9, 1, 5]

# Non-random pivot
sorted_non_random = quicksort(arr)
print("Sorted array (non-random):", sorted_non_random)

# Random pivot
sorted_random = quicksort_random(arr)
print("Sorted array (random):", sorted_random)
