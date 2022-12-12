s = input()

result = 1

for i in range(len(s)) :
  num = int(s[i])
  
  if num <=1 :
    result += num
  else :
    result *= num

print(result)
