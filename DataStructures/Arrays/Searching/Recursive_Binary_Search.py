
# arr = [1, 3, 5, 7, 9, 11, 13]
# target = 5
def Recursive_Binary_Search(arr,lower,upper,target):

    # lower=0
    # upper=len(arr)-1
    while lower <= upper:
        mid= (lower + upper) //2
        if arr[mid]==target:
            return mid
        elif arr[mid] > target:
            return Recursive_Binary_Search(arr,lower,mid-1,target)
        else:
            return Recursive_Binary_Search(arr, mid+1, upper, target)
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 5
result = Recursive_Binary_Search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")