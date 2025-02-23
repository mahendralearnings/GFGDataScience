def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Loop until the search space is exhausted
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found, return its index

        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1

        # If the target is smaller, ignore the right half
        else:
            high = mid - 1

    # If the element is not found, return -1
    return -1


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 10
result = binary_search(arr, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")