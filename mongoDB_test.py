def find_first_non_equal(arr1, arr2):
    for element in arr2:
        if element not in arr1:
            return element
    return None  # If no non-equal element is found

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [2, 8, 6, 4, 5]

result = find_first_non_equal(array1, array2)
if result is not None:
    print(f"The first non-equal element is: {result}")
else:
    print("There is no non-equal element.")