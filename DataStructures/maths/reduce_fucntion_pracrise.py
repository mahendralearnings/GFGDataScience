#1. Finding the Product of All Elements in a List
#https://www.geeksforgeeks.org/reduce-in-python/  --->reduce fucntion and acctumulate fucntion

from functools import reduce


def prodct_ele(l):

    return reduce(lambda x,y:(x*y) ,l)
    #simlilary we do x+y,x-y,x/y,x%y and so on
'''
reduce() vs accumulate() 

Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.  

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a iterator containing the intermediate results. The last number of the iterator returned is summation value of the list.
reduce(fun, seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.
'''


l=[1,2,3,4,5]
print("the prodcut of elements of listys are :",prodct_ele(l))


from itertools import accumulate
def accumelator_ex(l):

    return accumulate(l ,lambda x,y:x+y)
l=[1,2,3,4,5]
print("the summation  of elements of lists are :",list(accumelator_ex(l))) #cumilative sum  and prints intermediate results