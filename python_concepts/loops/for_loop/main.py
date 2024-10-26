#  Range
# range(start, stop, step) , ==> start - inclusive, stop exclusive, step -- jumps it will take


# ele_name = [ ele_list ]

cricketers = ["Virat", "Dhoni", "Rohit", "Bumrah", "KL Rahul"]
            #   0, 1,2,3   

# for i in range(2,15,3):
#     print(i)


# print(cricketers)

# print(cricketers[0])
# print(cricketers[3])

# for looping_element in list_name:
#   print(looping_element)



# for a in cricketers:
#     print(a)


test= ["reena", "pooja", "sunny", "nidhi"]
# print(test[2])


# for a in test:

#     # a = "reena"
#     # print(a[2] +"chugh")
   
#     # if a == "sunny":
#     #     print(a+"chugh")

#     # a= reena
#     print(test[2])
#     print(a)

test.append("rahul")

print(test)

# list_name.append("element")

# list_name.inset(index, "element")
test.insert(2, "harsh")
print(test)




test.remove("harsh")
test.pop(2)
print(test)
