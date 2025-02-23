""""
Problem:
Given the array of network traffic changes:
[100, -30, 50, -10, 60, -20], we want to find the subarray that represents
the period with the maximum traffic increase, which would give the highest sum.
"""


def traffic_sub_max(arr):

    max_so_far=arr[0]
    current_max=arr[0]
    # Track the indices of the subarray
    start = 0
    end = 0
    temp_start = 0

#traverse in the array
    for i in range(1,len(arr)):

        current_max=max(arr[i],current_max+arr[i])

        max_so_far=max(max_so_far,current_max)
    return max_so_far

arr=[100, -30, 50, -10, 60, -20]
print(traffic_sub_max(arr))