def max_second_max(arr):

    n=len(arr)

    #if array has fewer than 2 elements then
    #first ele is max and secondmax is -1

    if n < 2:

        return (arr[0],-1) if len(arr)==0 else(-1,-1)
    max1=-float('inf')
    max2=-float('inf')


    for num in arr:

        if num > max1:
            max2=max1
            max1=num
        elif num > max2 and num !=max1:

            max2=num

        if max2==float('-inf'):

           max2=-1
    return [max1,max2]

#arr=[10,10,10,10,10]
#arr=[-19,-8,-100,-1000,-2]

arr=[-19,-8,-100,-1000,-2]
print(max_second_max(arr))