# A
X, Y, Z = map(int, input().split())
print(Z, X, Y)

# B
N, M = map(int, input().split())
A = list(map(int, input().split()))
 
A = sorted(A, reverse=True)
 
X = A[M-1]
Y = sum(A)
th = Y / (4*M)
 
if X >= th:
  print('Yes')
else:
  print('No')

# C
N, K = map(int, input().split())

I = N // K
J = N % K
j = J

if J == 0:
  pass
else:
  j = J
  for i in range(I+2):
    J = abs(J - K)
    if J <= j:
      j = J
    else:
      break
      
print(j)