def kadane_algorithm(arr):
    max_so_far = arr[0]   # Maximum sum encountered so far
    current_max = arr[0]  # Maximum sum of the current subarray
    start = 0  # Start index of the maximum sum subarray
    end = 0    # End index of the maximum sum subarray
    temp_start = 0  # Temporary start index for tracking current subarray

    for i in range(1, len(arr)):
        # If the current element is greater than the current_max + arr[i], start a new subarray
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            temp_start = i  # Start a new subarray at index i
        else:
            current_max += arr[i]  # Otherwise, extend the current subarray

        # If the new current_max is better than max_so_far, update max_so_far and subarray indices
        if current_max > max_so_far:
            max_so_far = current_max
            start = temp_start  # Update the start to temp_start (where the new subarray started)
            end = i  # Update the end to the current index (i)

    # Return the maximum sum and the subarray that has this sum
    return max_so_far, arr[start:end + 1]

# Example usage
arr = [10, 30, -50, -10, 30,20, -20]
max_sum, subarray = kadane_algorithm(arr)
print(f"Maximum sum is: {max_sum}")
print(f"Subarray with the maximum sum is: {subarray}")
