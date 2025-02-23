def gcd(a,b):

    if a==0:
       return b
    if b==0:
        return a

    if a==b:

        return a
    if a > b:

       return  gcd(b,a-b)
    else:
       return  gcd(a,b-a)

print(gcd(20,30))

#2nd approach

def gcd_second_approach(a,b):

    return a if  b==0 else gcd(b,a%b)