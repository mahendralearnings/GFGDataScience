def maxIndexDiff(arr, n):
    if n <= 1:
        return 0  # No valid difference for arrays of length <= 1

    # Step 1: Create leftMin and rightMax arrays
    leftMin = [0] * n
    rightMax = [0] * n

    # Fill leftMin: Stores the minimum from the left up to index i
    leftMin[0] = arr[0]
    for i in range(1, n):
        leftMin[i] = min(leftMin[i - 1], arr[i])

    # Fill rightMax: Stores the maximum from the right from index j
    rightMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        rightMax[j] = max(rightMax[j + 1], arr[j])

    # Step 2: Traverse leftMin and rightMax with two pointers
    i, j = 0, 0
    maxDiff = 0

    while i < n and j < n:
        if leftMin[i] <= rightMax[j]:
            maxDiff = max(maxDiff, j - i)
            j += 1
        else:
            i += 1

    return maxDiff


# Example usage
arr = [3, 5, 4, 2, 6, 8, 1, 9]
n = len(arr)
result = maxIndexDiff(arr, n)
print(f"The maximum difference (j - i) is: {result}")
