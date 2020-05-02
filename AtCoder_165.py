# A
K = int(input())
A, B = map(int, input().split())

x = list(range(A, B+1))

for i in x:
  if i % K == 0:
    print('OK')
    break
  elif i == B:
    print('NG')
  else:
    pass

# B
X = int(input())

a = 100
i = 0
while a < X:
  a = int(1.01*a)
  i += 1

print(i)

# C
N, M, Q = map(int, input().split())
l = []
for i in range(Q):
  l.append(list(map(int, input().split())))

A_N = [[i] for i in range(1, M+1)]
for i in range(N-1):
  a = []
  for j in range(len(A_N)):
    last = A_N[j][-1]
    for k in range(last, M+1):
      a.append(A_N[j] + [k])
  A_N = a

high_score = 0
for i in range(len(A_N)):
  A = A_N[i]
  score = 0
  for j in range(len(l)):
    aj, bj, cj, dj = l[j]
    if A[bj-1]-A[aj-1] == cj:
      score += dj
  high_score = max(high_score, score)

print(high_score)

# D
import math
A, B, N = map(int, input().split())

x = min(B-1, N)
y = math.floor(A*x/B) - A * math.floor(x/B)
print(y)