
n = int(input())
# n = 7
X = [int(i) for i in input().split()]
# X = [-10,-5,-3,-1,0,1,4]
P = [int(i) for i in input().split()]
# P = [2,5,6,5,2,1,7]
# [0,1,3,6,10]
q = int(input())
# q=8
L = [[int(i) for i in input().split()] for j in range(q)]
# L = [[-8,-3]]

# [1,2,3,4,5,6]
# [0,1,3,6,10,15,21]
P_sum = [0]

#事前に村人の和を配列にする
# これを累積和という
for i in P:
    P_sum.append(P_sum[-1] + i)

# [11,12,13,14,15,16]
# [0,1,3,6,10,15,21]

# X = [1,3,5,7]
Status = {X[i]:P_sum[i+1] for i in range(n)}
Status[-10000000000] = 0
X.insert(0,-10000000000)
#X[0,1,3,5,7]
# print(Status)

for l in L:
    per_sum = 0
    # スタート座標
    # start_point = -10000000000
    # goal_point = -10000000000

    # スタートp_sum
    start_p_sum = 0
    goal_p_sum = 0

    X_copy = X.copy()
    
    #[1,3,5,7]
     # start
    while len(X_copy) != 1:
        median_index = len(X_copy)//2
        median = X_copy[median_index]

        if l[0]-1 < median:
            X_copy = X_copy[:median_index]
        else:
            X_copy = X_copy[median_index:]
        # print(median,X_copy,l[0])

    start_p_sum = Status[X_copy[0]]
    # print("start")
    # print(X_copy)
    # print(Status,X_copy[0])
    # print(Status[X_copy[0]])

    X_copy = X.copy()

    # goal
    while len(X_copy) != 1:
        median_index = len(X_copy)//2
        median = X_copy[median_index]

        if l[1] < median:
            X_copy = X_copy[:median_index]
        else:
            X_copy = X_copy[median_index:]
        # print(median,X_copy,l[1])

    
    # print("goal")
    # print(X_copy)
    # print(Status,X_copy[0])
    # print(Status[X_copy[0]])

    
    goal_p_sum = Status[X_copy[0]]

    # print({"start":{"x":start_point,"sum":start_p_sum},"goal":{"x":goal_point,"sum":goal_p_sum}})
    print(goal_p_sum - start_p_sum)

