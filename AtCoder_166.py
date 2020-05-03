# A
S = input()

if S == 'ABC':
  print('ARC')
else:
  print('ABC')

# B
N, K = map(int, input().split())
l_d = []
l_A = []
for i in range(K):
  di = int(input())
  Ai = list(map(int, input().split()))
  l_d.append(di)
  l_A.append(Ai)

l = [0]*N
for i in range(len(l_A)):
  for j in l_A[i]:
    l[j-1] = 1

print(l.count(0))

# C
# from pprint import pprint
import numpy as np

N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = []
for i in range(M):
  ABi = list(map(int, input().split()))
  AB.append(ABi)

matrix = np.zeros((N,N))
for i in range(N):
  matrix[i][i] = H[i] - 0.5
# pprint(matrix)
for m in range(M):
  Am, Bm = AB[m]
  matrix[Am-1][Bm-1] = H[Bm-1]
  matrix[Bm-1][Am-1] = H[Am-1]
# pprint(matrix)
max_index_list = []
for i in range(N):
  max_index = np.argmax(matrix[i])
  max_index_list.append(max_index)
# print(max_index_list)
correct_index_list = list(range(N))
# print(correct_index_list)
count = [max_index_list[i] == correct_index_list[i] for i in range(N)]
# print(count)
print(sum(count))

