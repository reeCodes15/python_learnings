# Remove Duplicates from a List
# Write a program to remove duplicate items from a list.



l1 = [1,2,3,4,1,3,13]

# # OUTPUT ==> [1,2,3,4,13]
d1={}
for ele in l1:
    d1[ele] = 'CODER REE DA!!!!! MANIFEST it to reality.'

# for  in d1.keys():
#     print(key, end=" ")
# print()
print(d1.keys())

for reena in d1.keys():
    print(reena, end=" ")
print()



print(list(set(l1)))

