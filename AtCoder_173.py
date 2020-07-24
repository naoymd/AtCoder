# A
N = int(input())

x = N % 1000
if x == 0:
  print(0)
else:
  print(1000 - x)


# B
N = int(input())
S_list = []
for _ in range(N):
  S = str(input())
  S_list.append(S)
# print(S_list)
AC_list = [S == 'AC' for S in S_list]
WA_list = [S == 'WA' for S in S_list]
TLE_list = [S == 'TLE' for S in S_list]
RE_list = [S == 'RE' for S in S_list]
print('AC x {}'.format(sum(AC_list)))
print('WA x {}'.format(sum(WA_list)))
print('TLE x {}'.format(sum(TLE_list)))
print('RE x {}'.format(sum(RE_list)))


# D
N = int(input())
A_list = list(map(int, input().split()))
A_list.sort(reverse=True)

if N % 2 == 0:
  k = N // 2
  print(A_list[0] + 2*sum(A_list[1:k]))
else:
  k = N // 2
  print(A_list[0] + 2*sum(A_list[1:k]) + A_list[k])