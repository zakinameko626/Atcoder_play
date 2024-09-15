# 371 B問

n,m = [int(i) for i in input().split()]
A = [input().split() for i in range(m)]
# H = {}

# for i in A:
#     H[i[0]] = True
H = { i[0]:True for i in A }

for i in A:
    if i[1] == 'M' and H[i[0]] == True:
        print('Yes')
        H[i[0]] = False
    else:
        print('No')
    


# print(A)
# A = [[1,M],[2,F]]