lis = []
length = []
n = int(input("enter string number:"))
str = ""
for i in range(0,n):
    val = input("enter the string:")
    lis.append(val)
    length.append(len(val))

for i in range(0,n-1):
    index = 0;
    flag = 0
    last_index_flag = 0
    for j in range(length[i]):
        if lis[i][j] == lis[i+1][index]:
                flag = 1
                index += 1
                if j == length[i] - 1:
                    last_index_flag = 1
        else:
            flag = 0
            index = 0
            last_index_flag = 0
    #print(lis[i + 1])
    if last_index_flag == 1:
        if i==0:
            #print(lis[i + 1])
            str = str + lis[i] + lis[i + 1][index:]
        else:
            #print(lis[i + 1])
            str = str + lis[i+1][index:]
    else:
        if i==0:
            #print(lis[i + 1])
            str = str + lis[i] + lis[i + 1][:]
        else:
            #print(lis[i + 1])
            str = str + lis[i+1][:]

print(str)






