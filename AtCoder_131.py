# A
S = list(map(int, input()))
 
t = 0
for i in range(len(S)-1):
  if S[i] == S[i+1]:
    t = 1
    break  
  else:
    pass
 
if t == 0:
  print('Good')
else:
  print('Bad')

# C
import fractions
A, B, C, D = map(int, input().split())
 
gcd = fractions.gcd(C, D)
lcm = C * D // gcd
a_c = (A-1) // C
a_d = (A-1) // D
b_c = B // C
b_d = B // D
a_lcm = (A-1) // lcm
b_lcm = B // lcm
count = (B - A + 1) - ((b_c - a_c) + (b_d - a_d) - (b_lcm - a_lcm))
print(int(count))
