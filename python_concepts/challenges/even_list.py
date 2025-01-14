a = [1,2,3,4,5,6,7,8]

# print even numbers from this list

#Give me sum of even numbers  and store this in a new list of even numbers
# reverse that new list
# b = [2,4,6,8]
b=[]
sum=0
for i in a:
    if i%2==0:
        b.append(i)
        sum=sum+i
                # print("sum of even number is", sum)

print("sum of even numbers is", sum)
print(b)
print(b[::-1])

