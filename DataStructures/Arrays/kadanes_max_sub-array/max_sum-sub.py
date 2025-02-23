

"""
Problem #3 : Largest Sum Subarray

Description : We are given an array of positive and negative integers. We have to find the subarray having maximum sum.
Input
[-3, 4, -1, -2, 1, 5]
Output
7

"""


def largest_sum_subarray(arr):

    max_so_far=0
    current_max=0

    for i in range(1,len(arr)):

        current_max=max(arr[i],current_max+arr[i])
        max_so_far=max(current_max,max_so_far)

    return max_so_far

arr=[-3, 4, -1, -2, 1, 5]
res=largest_sum_subarray(arr)

print(f"largest of sum of the array is ",res)