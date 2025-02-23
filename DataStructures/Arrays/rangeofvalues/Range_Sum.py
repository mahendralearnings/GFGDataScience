def range_sum_array(arr,queries):
    n=len(arr)
    prefix=[0]*n

    prefix[0]=arr[0]

    #prefix sum caliculation for rnage n

    for i in range(1,n):
        prefix[i] =arr[i] + prefix[i-1]


    # prefis sum fotr queries
    results=[]
    for l,r in queries:
        if l==0:
            ans=prefix[r]
        else:
            ans=prefix[r] -prefix[l-1]
        results.append(ans)
    return results
arr=[4, 5, 3, 2, 5]
queries=[(0,3),(2,4),(1,3)]
print(range_sum_array(arr,queries))




#realtime scenarios
