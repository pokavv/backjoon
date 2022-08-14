hour, minute, second = map(int, input().split(':'))
hour1, minute1, second1 = map(int, input().split(':'))

time = (hour * 3600) + (minute * 60) + second
take_time = (hour1 * 3600) + (minute1 * 60) + second1
if hour > hour1:
    take_time += 24 * 3600

time = take_time - time
atime = str(time // 3600)
btime = str((time % 3600) // 60)
ctime = str((time % 3600) % 60)
if (time // 3600) // 10 == 0:
    atime = "0" + str(time // 3600)
if ((time%3600)//60)//10 == 0:
    btime = "0" + str((time%3600)//60)
if ((time%3600)%60) // 10 == 0:
    ctime = "0" + str((time%3600)%60)
print(atime + ":" + btime + ":" + ctime)