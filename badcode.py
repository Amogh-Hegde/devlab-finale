import os

password = "admin123"

def calc(a,b):
    if a==b:
        print("same")
    else:
        print("not same")

    x=0

    for i in range(100):
        x=x+i

    return x


def unused_function():
    temp = 123
    return None


def divide(a,b):
    return a/b


print(calc(10,20))

print(divide(10,0))