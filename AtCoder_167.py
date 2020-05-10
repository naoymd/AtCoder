# A
S = list(input())
T = list(input())

T = T[:len(T)-1]
if S == T:
  print('Yes')
else:
  print('No')

# B
A, B, C, K = map(int, input().split())

Ka = max(0, min(K, A))
Kb = max(0, min(B, K-Ka))
Kc = max(0, min(C, K-Ka-Kb))

output = 1*Ka + 0*Kb + (-1)*Kc
print(output)

# C
import numpy as np

N, M, X = map(int, input().split())
CA = []
for i in range(N):
  CAi = list(map(int, input().split()))
  CA.append(CAi)

def function(CA, n, total, skill, C, X_l):
  CAn = CA[n]
  An = CAn[1:]
  skill = np.array(skill) + np.array(An)
  skill = list(skill)
  total += CAn[0]
  if skill >= X_l:
    C.append(total)
  return total, skill, C

C = []
X_l = [X]*M

count = 0
for a in range(N):
  total = 0
  skill = [0]*M
  total_a, skill_a, C = function(CA, a, total, skill, C, X_l)
  for b in range(a+1, N):
    total_b, skill_b, C = function(CA, b, total_a, skill_a, C, X_l)
    for c in range(b+1, N):
      total_c, skill_c, C = function(CA, c, total_b, skill_b, C, X_l)
      for d in range(c+1, N):
        total_d, skill_d, C = function(CA, d, total_c, skill_c, C, X_l)
        for e in range(d+1, N):
          total_e, skill_e, C = function(CA, e, total_d, skill_d, C, X_l)
          for f in range(e+1, N):
            total_f, skill_f, C = function(CA, f, total_e, skill_e, C, X_l)
            for g in range(f+1, N):
              total_g, skill_g, C = function(CA, g, total_f, skill_f, C, X_l)
              for h in range(g+1, N):
                total_h, skill_h, C = function(CA, h, total_g, skill_g, C, X_l)
                for i in range(h+1, N):
                  total_i, skill_i, C = function(CA, i, total_h, skill_h, C, X_l)
                  for j in range(i+1, N):
                    total_j, skill_j, C = function(CA, j, total_i, skill_i, C, X_l)
                    for k in range(j+1, N):
                      total_k, skill_k, C = function(CA, k, total_j, skill_j, C, X_l)
                      for l in range(k+1, N):
                        total_l, skill_l, C = function(CA, l, total_k, skill_k, C, X_l)

if len(C) == 0:
  print('-1')
else:
  print(min(C))
