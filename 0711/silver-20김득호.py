import math
import sys
input = sys.stdin.readline()
n = int(input)

dp = [k for k in range (n+1)]

for i in range(1,n+1):
    for j in range(int(math.sqrt(i)),0,-1):
        if (i - (j*j)) == 0:
            dp[i] = 1
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])


# import sys
# import math
#
# input = sys.stdin.readline()
# n = int(input)
#
# dp = [0 for _ in range(n+1)]
# pow_num = []
# alpa = 1
# for i in range(1, n+1):
#     if math.sqrt(i) == alpa:
#         dp[i] = 1
#         pow_num.append(i)
#         alpa += 1
#     else:
#         pow_num.sort(reverse=True)
#         f_min = 5
#         for m in range(len(pow_num)):
#             cur_num = i
#             cur_min = 0
#             for l in range(m,len(pow_num)):
#                 while cur_num > 0:
#                     if cur_num - pow_num[l] <0 :
#                         break
#                     else:
#                         cur_num -= pow_num[l]
#                         cur_min += 1
#                         if cur_min > 4:
#                             break
#                         if cur_num == 0:
#                             if cur_min < f_min:
#                                 f_min = cur_min
#                                 dp[i] = f_min
#
#
# print(dp[n])
