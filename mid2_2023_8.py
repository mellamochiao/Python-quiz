r = int(input('Enter the number of rows : '))
c = int(input('Enter the number of columns : '))
rs = input('Enter the reserved seats : ')
rseat = rs.split('|')

#處理輸入位置
seat = []
for s in range(0, len(rseat)):
    seat.append(rseat[s].split(','))

#計算需要更改的是第幾個位置
ste = []
snte = []
for s in range(0, len(rseat)):
    if int(seat[s][0]) <= r and int(seat[s][1]) <= c and int(seat[s][0])!=0 and int(seat[s][1])!=0 :
        ste.append(((int(seat[s][0])-1)*c + int(seat[s][1]))-1) #index start with 0
    else:
        snte.append(','.join(seat[s]))
        
#更改座位表
tseat = ['A']*r*c
for s in range(0, len(ste)):
    tseat[ste[s]] = 'R'

#印出座位表
seatarrange = ''
for i in range(0, r*c, c):
    row = (tseat[i : i+c])
    seatarrange += ' '.join(row) + '\n'
if len(snte) != 0:
    print('Out of range reserved seats : ', end='')
    print('|'.join(snte))
print('Seating Arrangement : ')
print(seatarrange)