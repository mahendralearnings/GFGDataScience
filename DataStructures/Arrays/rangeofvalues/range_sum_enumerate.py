"""

When to Use enumerate:
You should use enumerate whenever you need both the index and value of the array elements during iteration.

It makes the code cleaner and more readable by avoiding the need for range(len(arr)) or manual index handling.

"""

def range_sum_enumerate(arr,queries):
    n=len(arr)

    prefix=[0]*n

    for i,val in enumerate(arr):
        if i==0:
            prefix[i]=val
        else:
            prefix[i]=val+prefix[i-1]
    results=[]
    for l,r in queries:
        if l==0:
            ans=prefix[r]
        else:
            ans=prefix[r]-prefix[l-1]
        results.append(ans)
    return results
arr=[4, 5, 3, 2, 5]
queries=[(0,3),(2,4),(1,3)]
print(range_sum_enumerate(arr,queries))