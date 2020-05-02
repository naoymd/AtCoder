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
