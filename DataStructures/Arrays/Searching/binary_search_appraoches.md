
# Binary Search Approaches in Python

## 1. Iterative Binary Search

This is a simple iterative version of binary search, which avoids recursion and uses a loop.

```python
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if the target is at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
        
        # If target is smaller, ignore the right half
        else:
            high = mid - 1
    
    # Target is not found
    return -1
```

## 2. Recursive Binary Search

This version uses recursion instead of an iterative loop.

```python
def binary_search_recursive(arr, low, high, target):
    # Base case: If the range is invalid, return -1 (target not found)
    if low > high:
        return -1
    
    # Find the middle element
    mid = (low + high) // 2
    
    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    
    # If the target is smaller, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    
    # If the target is larger, search the right half
    else:
        return binary_search_recursive(arr, mid + 1, high, target)
```

## 3. Binary Search Using Python's Built-in `bisect` Module

The `bisect` module provides a way to perform binary search efficiently. You can use `bisect_left` to get the position where the target should be inserted to maintain sorted order.

```python
import bisect

def binary_search_bisect(arr, target):
    index = bisect.bisect_left(arr, target)
    
    # Check if the target is actually present at the found index
    if index < len(arr) and arr[index] == target:
        return index
    else:
        return -1
```

## 4. Binary Search with Custom Comparator (for Complex Objects)

If you're searching within a list of complex objects, you can create a comparator function to extract the field to be compared.

```python
def binary_search_with_comparator(arr, target, key=lambda x: x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = key(arr[mid])  # Use key to extract value for comparison
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example usage for a list of dictionaries
arr = [{'id': 1}, {'id': 3}, {'id': 5}, {'id': 7}]
target = 5
result = binary_search_with_comparator(arr, target, key=lambda x: x['id'])
```

## 5. Binary Search with Tolerance (for Floating Point Numbers)

When dealing with floating-point numbers, exact comparisons may fail due to precision issues. This function searches within a tolerance.

```python
def binary_search_with_tolerance(arr, target, tol=1e-6):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # If the difference is within tolerance, consider it found
        if abs(arr[mid] - target) < tol:
            return mid
        
        # Adjust the search range
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
```

---

### Summary of Use Cases:

1. **Iterative Binary Search**: For simple integer or sorted array searches.
2. **Recursive Binary Search**: If you prefer a recursive approach.
3. **Using `bisect` module**: For a quick and efficient binary search using a library function.
4. **With custom comparator**: If searching in complex objects or non-primitive data structures.
5. **With tolerance**: Useful when working with floating-point values.
