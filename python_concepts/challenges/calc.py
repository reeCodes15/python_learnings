# 1 - Simple Calculator
# 2 -  
# add, subtract, multiply, divide

def add(a,b):
    c=a+b
    return c

def subtract(a,b):
    c=a-b
    return c

def multiply(a,b):
    c=a*b
    return c

def divide(a,b):
    try:
        c=a/b
        return c

    except Exception as e:
        print("Server went down")

cd = divide(10,0)


# ca=multiply(12,23)
# print(ca)
# cs = add(3,4)
# print(cs)
