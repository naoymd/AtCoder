# A
alpha = input()
if alpha.isupper() == True:
  print('A')
else:
  print('a')


# B
N, K = map(int, input().split())
p_list = list(map(int, input().split()))

p_list = sorted(p_list)
print(sum(p_list[:K]))


# C
N = int(input())

def base_10_to_n(x, base):
  output = []
  while True:
    a = x % base
    output.append(a)
    x //= base
    if x == 0:
      for i in range(1, len(output)):
        if output[i-1] <= 0:
          output[i] = output[i] -1
      output = output[::-1]
      if output[0] == 0:
        output.pop(0)
      break
  return output

# def base_10_from_n(x, base):
#   output = 0
#   for i in reversed(range(len(x)-1)):
#     output += base ** i
#   return output

base = 26
output = base_10_to_n(N, base)

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name = ''
for i in output:
  name += alphabet_list[i-1]
print(name)

