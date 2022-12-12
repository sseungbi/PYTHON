n = int(input())
x = list(map(int, input().split()))
x.sort()

grp_cnt = 0
x_cnt = 1

for i in x :
  if x_cnt == i :
    x_cnt = 1
    grp_cnt += 1
  else :
    x_cnt += 1

print(grp_cnt)