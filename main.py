N, K = map(int, input().split())

count = 0  #최소 횟수

while N != 1:
  if N % K == 0:
    N //= K
    count += 1
  else:
    N -= 1
    count += 1

print(count)
