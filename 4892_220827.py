num = 0

while True :
  n = int(input())
  num += 1
  if n == 0 :
    break
  if n % 2 != 0 :
    print(num, ". odd ", n // 2, sep='')
  else :
    print(num, ". even ", n // 2, sep='')