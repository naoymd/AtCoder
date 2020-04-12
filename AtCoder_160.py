# A
S = input()
 
if S[2] == S[3] and S[4] == S[5]:
  print('Yes')
else:
  print('No')

# B
X = int(input())
y_500 = X // 500
x_500 = X % 500
y_5 = x_500 // 5
x_5 = x_500 % 5
 
z = y_500 * 1000 + y_5 * 5
print(z)

# C
K, N = map(int, input().split())
A = list(map(int, input().split()))
n = K + min(A)
A.append(n)
A = sorted(A)
l = len(A)
B = []
for i in range(l-1):
  b = abs(A[i+1] - A[i])
  B.append(b)
x = sum(B) - max(B)
print(x)