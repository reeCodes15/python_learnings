l1 = [1,2,13,13,32,44,355,44]
# o/p == 13
# Only one element in this list is duplicate, find that out and print it!
#  We don't need twins, one twin is enough POOJA REENA, tough!!!!!
#   BHAGWAN BACHAYE

l1 = [1,2,13,13,32,44,355,44]
d1 = {}

for ele in l1:
    if l1.count(ele)>1:
        d1[ele] = True 


# d1 = {'13': True, '44':True}
for key in d1.keys():
    print(key)
        
