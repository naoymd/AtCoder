# A
A, B = map(int, input().split())
out = A * B
print(out)


# B
from operator import mul
from functools import reduce
N = int(input())
A = list(map(int, input().split()))

# out = reduce(mul, A)
# if out <= 1e18:
#   print(out)
# else:
#   print('-1')

A.sort(reverse=True)
out = 1
if A[-1] == 0:
  out = 0
else:
  for i in A:
    out *= i
    if out > 1e18:
      out = -1
      break
print(out)


# C
A, B = map(float, input().split())
out = A * B
print(int(out))


# D
import math

def eratosthenes(limit):
  limit = max(limit, 2)
  A = [i for i in range(2, limit+1)]
  P = []
  while True:
    prime = min(A)
    if prime > math.sqrt(limit):
      break
    P.append(prime)
    i = 0
    while i < len(A):
      if A[i] % prime == 0:
        A.pop(i)
        continue
      i += 1
  for a in A:
    P.append(a)
  return P

# def fermat(limit):
#   n = 0
#   limit = max(limit, 2)
#   for k in range(2, limit+1):
#     if k % 2 == 0 and k != 2:
#       continue
#     if pow(2, k-1, k) == 1:
#       n += 1   
#   return n

N = int(input())
p = 2
P = eratosthenes(N)
# print(P)
count = 0
if N == P[-1]:
  count = 1
else:
  while p <= N:
    if N % p == 0:
    #   print(p)
      N //= p
      count += 1
      P = eratosthenes(N)
      if N == P[-1] or N == 1:
        break
    p += 1
print(count)
