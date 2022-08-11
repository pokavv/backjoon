num = int(input())
cute = 0

for i in range(num):
    if int(input()) == 1:
        cute += 1

if cute > num // 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")