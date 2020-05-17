# A
N = input()

n = N[-1]

hon = ['2', '4', '5', '7', '9']
pon = ['0', '1', '6', '8']
bon = ['3']
if n in hon:
  print('hon')
elif n in pon:
  print('pon')
elif n in bon:
  print('bon')


# B
K = int(input())
S = input()

if len(S) <= K:
  print(S)
else:
  print(S[:K] + '...')


# C
import math

A, B, H, M = map(int, input().split())

wA = 360 / (12*60)
wB = 360 / 60

theta_A = (60*H+M) * wA
theta_B = M * wB

theta = abs(theta_A - theta_B)
output = math.sqrt(abs(A**2 + B**2 - 2*A*B*math.cos(math.radians(theta))))
print(output)
