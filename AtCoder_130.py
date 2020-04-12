# A
X, A = map(int, input().split())
 
if X < A:
  X = 0
else:
  X = 10
  
print(X)

# B
import numpy as np
 
N, X = map(int, input().split())
L = list(map(int, input().split()))
 
L = np.array(L)
D = np.zeros(N+1)
 
count = 1
for i in range(1, N+1):
  D[i] = D[i-1] + L[i-1]
  if D[i] <= X:
    count += 1
  else:
    pass

# C
W, H, x, y = map(int, input().split())
 
s_max = W * H / 2.0
 
if x==W/2 and y==H/2:
  print(s_max, 1)
else:
  print(s_max, 0)