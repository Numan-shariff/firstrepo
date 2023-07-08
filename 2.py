def newton_method(num,n=100):
    a=float(num)
    for i in range(num):
        num=0.5*(num+a/num)
    return num
a=int(input("Enter a value"))
print("Square root of a is :",newton_method(a))