
'''

Geeks for geeks problems

'''

''''

Given an array arr of positive integers. 
The task is to return the maximum of j - i subjected to the constraint of arr[i] < arr[j] and i < j.

Examples:

Input: arr[] = [1, 10]
Output: 1
Explanation: arr[0] < arr[1] so (j-i) is 1-0 = 1.

'''


"""
Btuteforce approach

"""

def find_max_index_diff(arr):
    left=0
    right=len(arr)-1
    ans=-1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):

            if arr[i] < arr[j] :
                ans=max(ans,j-i)
    return ans if ans!=-1 else 0
    #     #while left < right:
    #          if left[i]==right[i]:
    #
    #              return False
    #
    #          if left[i] < right[i]:
    #              left+=1
    #              right-=1
    # return right-left
arr=[34, 8, 10, 3, 2, 80, 30, 33, 1]

#Input: arr[] =

print(find_max_index_diff(arr))