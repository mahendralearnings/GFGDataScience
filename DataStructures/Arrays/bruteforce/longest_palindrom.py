#2. Find the Longest Palindromic Substring
'''
Here’s a textual flow of steps that could be visualized into a diagram for the brute force approach to find the longest palindromic substring:

Step-by-Step Diagram:
Start:

Input: The string s.
Outer Loop (i):

Start iterating over the string with index i (from 0 to len(s) - 1).
This defines the starting point of the substring.
Inner Loop (j):

For each i, start a second loop with index j (from i to len(s) - 1).
This defines the ending point of the substring.
Extract Substring:

Extract the substring from i to j+1 (s[i:j+1]).
Check if Palindrome:

Call the helper function is_palindrome(s[i:j+1]) to check if the substring is a palindrome.
Is Palindrome?

If the substring is a palindrome:
Compare the length of the palindrome with the current longest palindrome.
If it is longer, update the longest palindrome variable.
Continue Loop:

Continue iterating through all substrings for all i and j values.
End:

After all substrings have been checked, return the longest palindrome found.
Summary Flow:
Input → 2. Outer Loop (i) → 3. Inner Loop (j) → 4. Extract Substring → 5. Check Palindrome → 6. Update Longest → 7. Continue → 8. Return Longest
This sequence of steps is essentially what would appear in the diagram form, showing how the nested loops explore all substrings and check if they are palindromes. Each block of the diagram would represent these decision points and actions.

If you want, I can create a visual diagram based on these steps.
'''

'''
brute force approach
'''

def longest_palindrome(s):

    def is_palindrom_helper(sub):
        return sub==sub[::-1]
    longest=""

    for i in range(0,len(s)):

        for j in range(i,len(s)):

            if is_palindrom_helper(s[i:j+1]) and len(s[i:j+1]) > len(longest):
                longest=s[i:j+1]
    return longest

#driver program
s2="forgeeksskeegfor"

s="ababaabcdmadammalayalamsubvikatakavi"
#print(longest_palindrome(s))


"""

Time Complexity: O(n³) – O(n²) for checking all substrings and O(n) for checking if a substring is a palindrome.
Explanation: The brute force approach is slow because it checks every possible substring and validates each for being a palindrome.

"""

#----------------------------------------------------------------------------------------------
"""
Approach: 
      Every palindrome has a center. 
          Either the palindrome has a single center (odd-length palindrome)

          or two centers (even-length palindrome).
          
          Expand outward from the center and check for the longest palindrome.

"""

def palindrom_expandupwards(s):

    def expand_around_center(left,right):
        while left >=0 and right < len(s)  and s[left]==s[right]:

           left-=1
           right+=1
        return s[left+1:right]
    longest=""
    for i in range(len(s)):
        #for odd lenght

        odd_palindrom=expand_around_center(i,i)# left and right both are same for odd length  5/2 =2 (1,2,3,4,5)  2nd index makes ledt and right same no of elemnets
        if len(odd_palindrom) > len(longest):
            longest=odd_palindrom


        even_palindrom=expand_around_center(i,i+1)
        if len(even_palindrom) > len(longest):
            longest=even_palindrom
    return [longest,len(longest)]

s="abbaa"

print(palindrom_expandupwards(s))


'''
Time Complexity: O(n²)
Explanation: We expand around each character (and pairs of characters), and the expansion takes O(n) for each character.


'''


"""

for explaination

https://chatgpt.com/c/66ef8141-8c3c-8006-8dae-99a7dc158eb0
"""
