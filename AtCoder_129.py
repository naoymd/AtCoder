# A
P, Q, R =map(int ,input().split())
print(min(P+Q, Q+R, R+P))

# B
import numpy as np

N = int(input())
W = list(map(int, input().split()))

S_min = np.sum(W)
for T in range(N+1):
  S1 = np.sum(W[:T])
  S2 = np.sum(W[T:])
  dif = np.abs(S1 -S2)
  if dif <= S_min:
    S_min = dif
  else:
    print(S_min)
    break
