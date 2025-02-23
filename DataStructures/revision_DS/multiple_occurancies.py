def bin_all_occurances(arr,ele):

    index=binary_search(arr,ele)

    if index==-1:
        return []
    occurances=[index]

    left=index-1
    while left >=0 and arr[left]==ele:
        occurances.append(left)
        left=left-1
    right=index+1

    while right < len(arr) and arr[right]==ele:
        occurances.append(right)
        right=right+1

    occurances.sort()
    return occurances
def binary_search(arr,ele):
    left=0
    right=len(arr)-1
    mid=(left + right) // 2 #floor division

    while left <=right:

        if arr[mid] ==ele:
            return mid
        elif arr[mid] < ele:
            left=mid+1
        else:
            right=mid+1
    return -1


arr=[10, 20, 30,60,60,60, 60, 60, 110, 130, 140, 170]
ele=60
print(bin_all_occurances(arr,ele))


