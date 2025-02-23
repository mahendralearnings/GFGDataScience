#Input: arr[] = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170}, x = 110
#output :6

ind =0
def search_ele(arr,ele):
    x=len(arr)
    if ele not in arr:
        return -1
    low=0
    high=len(arr)-1
    mid =(low + high)//2

    while low<=high:
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            high=mid-1
        elif arr[mid] < ele:
            low=mid+1
    return -1


arr=[10, 20, 30, 60, 60, 60, 110, 130, 140, 170]
ele=60
print(search_ele(arr,ele))