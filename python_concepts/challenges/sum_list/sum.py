l1 = [1,2,3,4,5,77,33]
addn=0
for i in range(0,len(l1)):
    print('i=',i)
    print("currrent element of list is",l1[i])

    addn=addn+l1[i]
    print('AFTER Addition of current element, CURRENT SUM ==', addn)
print(addn)


# print(sum(l1)) 🥺


# for ele in l1:
#     print(ele)