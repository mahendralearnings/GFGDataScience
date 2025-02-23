# GFGDataScience

# recursive call working

    Step 1: Push function calls onto the stack
    Stack state: 
    
    | factorial(1) |
    | factorial(2) |
    | factorial(3) |
    | factorial(4) |
    | factorial(5) |

    Step 2: Pop off the stack as base case is reached and return values
    Unwinding:
    
    Return 1 from factorial(1)
    Return 2 from factorial(2)
    Return 6 from factorial(3)
    Return 24 from factorial(4)
    Return 120 from factorial(5)



tailing of zeros in n!

Formula:
To find the number of trailing zeros in 
𝑛
!
n!, you calculate how many multiples of 5 are there in the numbers from 1 to 
𝑛
n, including powers of 5 (e.g., 25, 125, etc.) because they contribute additional factors of 5.

The formula to compute the number of trailing zeros is:

Trailing Zeros
=
⌊
𝑛
5
⌋
+
⌊
𝑛
25
⌋
+
⌊
𝑛
125
⌋
+
⌊
𝑛
625
⌋
+
⋯
Trailing Zeros=⌊ 
5
n
​
 ⌋+⌊ 
25
n
​
 ⌋+⌊ 
125
n
​
 ⌋+⌊ 
625
n
​
 ⌋+⋯
Explanation:
⌊
𝑛
5
⌋
⌊ 
5
n
​
 ⌋ counts the number of multiples of 5.
⌊
𝑛
25
⌋
⌊ 
25
n
​
 ⌋ counts the multiples of 25 (which contribute an extra factor of 5).
Continue this process until 
𝑛
5
𝑘
5 
k
 
n
​
  is less than 1.
Example:
Let’s calculate the trailing zeros in 
100
!
100!:

⌊
100
5
⌋
=
20
⌊ 
5
100
​
 ⌋=20
⌊
100
25
⌋
=
4
⌊ 
25
100
​
 ⌋=4
⌊
100
125
⌋
=
0
⌊ 
125
100
​
 ⌋=0
So, the total number of trailing zeros in 
100
!
100! is 
20
+
4
=
24
20+4=24.

Would you like me to implement this in Python or provide a few more examples?



#reduce vs accumulator


''
reduce() vs accumulate() 

Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.  

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a iterator containing the intermediate results. The last number of the iterator returned is summation value of the list.
reduce(fun, seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.