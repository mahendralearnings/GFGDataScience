def is_palindrom(n):
    original = n
    rev = 0

    while n != 0:
        d = n % 10  # get the last digit
        rev = rev * 10 + d  ## Build the reversed number

        n = n // 10  # remove the last digit

    if original == rev:
        return True

    else:

        return False


#print(is_palindrom(1234))


#2nd approach using strings

def ispali_str(n):

    s=str(n)

    if s== s[::-1]:

        return True

    else:

        return False

print(ispali_str(1234))


