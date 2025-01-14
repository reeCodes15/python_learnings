# Create a function which determines whether a number is even or odd
# ask the number from user
# Push the code you do to the git repo. Ree man would finally become a github woman🥺

n = int(input("Enter a number: "))

def evenodd(a):
    if a%2==0:
        print("number is even")
    else:
        print("number is odd")
    
    return a


output = evenodd(n)
print(output)

