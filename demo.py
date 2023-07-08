def gcd(a, b):
 if(b == 0):
    return a
 else:
    return gcd(b, a % b)
 
a = int(input("enter a value :"))
b = int(input("enter b value :"))
print("GCD of a and b is:", end="")
print(gcd(a, b))
