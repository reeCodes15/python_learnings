l1 = [11,12,13,4,14,25,5]

# Output ==> 4

currentmin=float('inf')
for ele in l1:
    if currentmin>ele:
        currentmin=ele
print(currentmin)

