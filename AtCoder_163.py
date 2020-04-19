# A
import math

R = int(input())
output = 2* R * math.pi

print(output)

# B
N, M = map(int, input().split())
A = list(map(int, input().split()))

a = sum(A)
output = max(N - a, -1)

print(output)

# C
N = int(input())
A = list(map(int, input().split()))

B = [print(A.count(i)) for i in range(1, N+1)]

# C (別解:rktf)
N=int(input())
A=list(map(int,input().split()))
ans_list=[0]*(N+1)

for i in range(N-1):
  ans_list[A[i]] +=1
for i in range(1,N+1):
  print(ans_list[i])

# D
N , K = map(int, input().split())

def C(n, m):
  l = [i for i in range(m)]
  output = n*m + 1 - 2*sum(l)
  return output

S = [C(N, i) for i in range(K, N+2)]
print(sum(S) % (10**9+7))


# D (別解:rktf)
NK=list(map(int,input().split()))

data_list=[i for i in range(NK[0]+1)]
reverse_data_list=sorted(data_list, reverse=True)

#累積和格納リスト
min_sum_data_list=[0]*(NK[0]+1)
max_sum_data_list=[0]*(NK[0]+1)

#初期値設定
min_sum_data_list[0]=data_list[0]
max_sum_data_list[0]=reverse_data_list[0]
ans_data=0

#累積和の計算
for i in range(1,NK[0]+1):
  min_sum_data_list[i]+=min_sum_data_list[i-1]+data_list[i] % (pow(10,9)+7)
  max_sum_data_list[i]+=max_sum_data_list[i-1]+reverse_data_list[i] % (pow(10,9)+7)

for i in range(NK[1]-1,NK[0]+1):
  ans_data+=(max_sum_data_list[i]-min_sum_data_list[i]+1) % (pow(10,9)+7)
  
print(ans_data % (pow(10,9)+7)) 
