def check_palindrom_check(s):

     for x in s:
         if x==x[::-1]:

             return True
         else:
             return False



s="madam"
print(check_palindrom_check(s))

'''
we can use two pijnter technique to optimize above one

'''
def two_pointer_tech(s):
    left,right=0,len(s)-1
    while left < right :
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

'''
Time Complexity: O(n)
Explanation: The two-pointer approach only loops through the string once, 
making it as efficient as the brute force solution but without creating an additional reversed string.


Why the Time Complexity is O(n)
The two-pointer technique uses a single loop that runs from the start of the string (left pointer) to the end (right pointer).
In each iteration of the loop, two comparisons are made: one for the characters at the current left and right pointers. After the comparison, both pointers are moved towards the center (i.e., left += 1, right -= 1).
The loop runs until the left pointer is no longer less than the right pointer, which means it covers half the string in total.

'''



''''
2.2. Find the Longest Palindromic Substring
Given a string, find the longest palindromic substring in it.

Explanation:
The goal is to find the longest part of the string that is a palindrome. 
The string might have multiple palindromic substrings, and the longest one needs to be returned.

Example:
Input: "babad"
Output: "bab" (or "aba")

'''

'''
psudo code

read string and find the len

babad


left and right pointers and compare both of them or same or not if same swap it
iterate the string and 

'''