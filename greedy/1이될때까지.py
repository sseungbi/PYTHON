n, k = map(int, input().split())

count = 0  #최소 횟수

while n != 1:
  if n % k == 0:
    n //= k
    count += 1
  else:
    n -= 1
    count += 1

print(count)
