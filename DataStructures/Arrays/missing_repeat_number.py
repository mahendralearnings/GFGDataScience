def missing_repeat(arr):

    n=len(arr)

    freeq=[0]*(n+1)

    for num in arr:

        freeq[num]+=1

    missing,repeat=-1,-1
    for i in (range(1,n+1)):
        if freeq[i]==2:
            repeat=i
        if freeq[i]==0:
            missing=i
    return [repeat ,missing]


arr=[1,3,3]

print(missing_repeat(arr))