
from functools import reduce

#caliculate for two number
def gcd(a,b):
    return  a if b==0  else  gcd(b, a%b)

def gcd_mul_numbers(numbers):

    return  reduce(gcd,numbers)




#2nd approach

def gcd(a,b):

    return a if b==0 else gcd(b,a%b)

def gcd_mult(numberss):
    res=numberss[0]

    for number in numberss[1:]:
        return gcd(res,number)

numberss=[10,100,50]

print("GCD of", numberss, "is", gcd_mult(numberss))


"""
1. Using reduce
Pros:
Concise: It reduces the amount of code and focuses on the operation rather than implementation details.
Functional Programming Style: For those comfortable with functional programming, reduce makes the intention clear—applying a function iteratively across a sequence.
Good for Aggregations: It’s particularly well-suited for operations that naturally involve accumulation (like sum, product, or GCD).
Cons:
Less Readable for Some: If you’re working with others who may not be as familiar with reduce, it might make the code harder to read.
Error Handling: reduce can be less flexible for handling intermediate steps, like logging or debugging between iterations.



2. Loop-Based Approach
Pros:
More Readable for Many: A straightforward loop may be more familiar and accessible, especially to those with a background in imperative programming.
Flexibility: It allows you to handle errors, add logging, and debug between iterations more easily.
Easier Debugging: If you’re dealing with complex data or edge cases, the loop approach is easier to step through.
Cons:
More Code: While it’s a small amount of extra code, it’s slightly more verbose than reduce.
Potentially Slightly Slower: In very large cases (hundreds of thousands of numbers), reduce might be marginally faster due to internal optimizations, but this difference is usually negligible.
"""