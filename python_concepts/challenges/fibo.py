#  n==7,  1 1 2 4 6 10 16

#  n==6,  1 1 2 4 6 10

#  n==5,  1 1 2 4 6 

#  n==4,  1 1 2 4  

#  [0, 1, 1, 2, 3, 5]


n = 6

fibo_seq = [0,1]



for i in range(2, n):
    print('value of i is ', i)
    print('value of fibo_seq  i-1 is', fibo_seq[i-1])
    fibo_ele = fibo_seq[i-1] + fibo_seq[i-2]
    fibo_seq.append(fibo_ele)


print(fibo_seq)


