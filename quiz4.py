input = input('Enter a sequence of integers swperated by whiltspace : ')
input_list = input.split() # 用空格分割

sequence = [] #創建空白串列
for num_str in input_list:
    num = int(num_str)
    sequence.append(num)    # 把輸入的數字變成串列

f_sequence = []
current = None
for i in sequence :
    if current is None:
        current = i
    if i > current:  #當i比上一個數字大時延長串列
        f_sequence.append(i)
        current = i


print('Length', len(f_sequence))
print('LICS', f_sequence)
