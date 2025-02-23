def count_frequencies_bruteforce(arr, n):
    # Step 1: Initialize a count array to store frequencies of numbers from 1 to n
    count = [0] * n  # This will store the count for each number from 1 to n

    # Step 2: Count the occurrences of each number from 1 to n in the original array
    for i in range(len(arr)):
        if 1 <= arr[i] <= n:  # Only count if the number is between 1 and n
            count[arr[i] - 1] += 1

    # Step 3: Modify the original array to reflect the frequencies
    for i in range(n):
        arr[i] = count[i]

# Test case
arr = [3,3,3,3]  # Original array
n = len(arr)  # Size of the array (we care only about the range from 1 to n)

# Call the function to modify arr in-place
count_frequencies_bruteforce(arr, n)

# Output the modified array showing frequencies
print(arr)
