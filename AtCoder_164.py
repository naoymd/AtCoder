# A
S, W = map(int, input().split())

if W - S >= 0:
  print('unsafe')
else:
  print('safe')

# B
A, B, C, D = map(int, input().split())

x0 = C // B
x1 = C % B

y0 = A // D
y1 = A % D

if x1 == 0:
  y0 += 1
if y1 == 0:
  x0 += 1

if x0 - y0 <= 0:
  print('Yes')
else:
  print('No')

# C
N = int(input())
S = {}
for i in range(N):
  si = input()
  if si in S:
    S[si] += 1
  else:
    S[si] = 1

print(len(S))
