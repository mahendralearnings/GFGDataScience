#https://chatgpt.com/c/66f2f1e1-d88c-8006-90ed-b3568a32458d


def zerostoend(arr):

    n=len(arr)
    j=0
    for i in range(n):

        if arr[i]!=0:

            arr[i],arr[j]=arr[j],arr[i]

            j+=1
    return arr
arr = [5, 6, 0, 4, 6, 0, 9, 0, 8]

#print(zerostoend(arr))


def zerostoend(arr):

    nonzero_ele=[  x for x in  arr if x!=0]

    count_zeros=arr.count(0)

    #add these countzero at then end uaing extend

    nonzero_ele.extend([0]*count_zeros)

    return nonzero_ele
arr = [5, 6, 0, 4, 6, 0, 9, 0, 8]
print(zerostoend(arr))

"""
But the complexity time 0(n)
and space is also o(n)
we are creating a new array here 

"""