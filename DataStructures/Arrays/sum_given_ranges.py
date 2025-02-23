def prefix_sum(arr):

     prefix=[0]*len(arr)

     prefix[0]=arr[0]

     for i in range(1,len(arr)):

         prefix[i]=arr[i] + prefix[i-1]
     return prefix

     # l=0
     # r=len(arr)-1


def range_sum(prefix,k):
    result = []
    for l,r in k:

        if l==0:
            ans=prefix[r]

        else :
            ans=prefix[r]-prefix[l-1]

        result.append(ans)
    return result


arr=[4, 5, 3, 2, 5]
k=[(0,3),(1,4),(1,3)]
prefix=prefix_sum(arr)
print(range_sum(prefix,k))

