# A
N = input()
l = []

for i in range(len(N)):
  l.append(N[i])

if '7' in l:
  print('Yes')
else:
  print('No')

# B
N = input()

fizz = []
buzz = []
fizzbuzz = []
x = 0

for n in range(1, int(N)+1):
  x += n
  if n % 3 == 0:
    fizz.append(n)
  if n % 5 == 0:
    buzz.append(n)
  if n % 15 == 0:
    fizzbuzz.append(n)

fizz = sum(fizz)
buzz = sum(buzz)
fizzbuzz = sum(fizzbuzz)
y = x - fizz - buzz + fizzbuzz
print(y)

# C
import math
from functools import reduce

K = int(input())

def gcd(*numbers):
  return reduce(math.gcd, numbers)

output = 0

for a in range(1, K+1):
  for b in range(a, K+1):
    for c in range(b, K+1):
      if a == b == c:
        output += gcd(a, b, c)
      elif a != b and b != c and c != a:
        output += 6 * gcd(a, b, c)
      else:
        output += 3 * gcd(a, b, c)

print(output)

# D
N = int(input())
S = input()

r = []
g = []
b = []

for i, s in enumerate(S):
  if s == 'R':
    r.append(i+1)
  elif s == 'G':
    g.append(i+1)
  elif s == 'B':
    b.append(i+1)

count = 0

for i in r:
  for j in g:
    for k in b:
      if abs(j-i) != abs(k-j) and abs(k-j) != abs(k-i) and abs(k-i) != abs(j-i):
        count += 1
      else:
        pass

print(count)