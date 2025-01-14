# FizzBuzz
# 
# for numbers from 1 to 100. 
# For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for multiples of both, print "FizzBuzz".

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBUZZ",i)
    elif i%3==0:
        print("Fizz",i)
    elif i%5==0: 
        print("BUZZ",i)
    