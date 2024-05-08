list = input('Input list : ')
list = list.split(' ')
list = [int(x) for x in list]
low = int(input('Input low : '))
high = int(input('Input high : '))


if low < list[0]:
    list.insert(0, low-1)
if high > list[-1]:
    list.append(high+1)

mr = []
now = list[0]
for i in range(1, len(list)):
    if now+1 == list[i]:
        now = list[i]
        continue
    if now+2 == list[i]:
        mr.append(str((now+1)))
        now = list[i]
        continue   
    else:
        mr.append(str((now+1))+'->'+str((list[i]-1)))
        now = list[i]
print(mr)

