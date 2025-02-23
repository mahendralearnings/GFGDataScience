#1. Find the Maximum Number in a List

def max_num(arr):
    max_num=0

    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):

            if arr[i] > arr[j]:
                max_num=arr[i]
            else:
                max_num=arr[j]

    return max_num





arr=[10, 24, 15, 3, 56, 22]
#print(max_num(arr))
#Output: 56
'''

time coplexity is o(n2)  => O(n*n)

then how to optimize this 

'''




def find_max_num(nums):
    max_num=nums[0]

    for num in nums:

        if num > max_num:
            max_num=num
    return max_num

arr=[10, 24, 15, 3, 56, 22]
print(find_max_num(arr))
