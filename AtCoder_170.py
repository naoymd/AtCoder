# A
x_list = list(map(int, input().split()))

for i, xi in enumerate(x_list):
  if xi == 0:
    out = i+1
    break
  else:
    pass

print(out)


# B
X, Y = map(int, input().split())

if Y % 2 == 0 and Y >= 2*X and Y <= 4*X:
  print('Yes')
else:
  print('No')


# C
X, N = map(int, input().split())
p_list = list(map(int, input().split()))

if N == 0:
  print(X)
else:
  p_list = sorted(p_list)
  all_range = list(range(102))
  A = [i for i in all_range if i not in p_list]
  B = [abs(i - X) for i in A]
#   print(p_list)
#   print(all_range)
#   print(A)
#   print(B)
#   print(min(B))

  low = X - min(B)
  high = X + min(B)
#   print(low, high)

  output = 0
  if high > 101:
    output = low
  if low < 0:
    output = high

  if output != 0:
    print(output)
  elif high in p_list:
    print(low)
  elif low in p_list:
    print(high)
  else:
    print(low)


# D
N = int(input())
A_list = list(map(int, input().split()))

output_list = []
A_list = sorted(A_list)
# print(A_list)
A_len = len(A_list)
while True:
  n = A_list[0]
  if len(A_list) > 1 and A_list[1] == n:
    pass
  else:
    output_list.append(n)
  A_list = [i for i in A_list if i % n != 0]
  # print(A_list)
  A_len = len(A_list)
  if A_len == 0:
    break
  
# print(output_list)
print(len(output_list))

