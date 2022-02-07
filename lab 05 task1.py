count = 1
compress = []

val = input("Enter string:")
length = len(val)

for i in range(length-1):
    if val[i] == val[i+1]:
        count += 1
    if val[i] != val[i+1]:
        compress.append(val[i])
        if count > 1:
            compress.append(count)
            count = 1
        if i == length - 2:
            compress.append(val[i+1])
            compress.append(count)
    if(val[i]==val[i+1]) and (i==length-2): #if last index and last index-1 matches
        compress.append(val[i])
        compress.append(count)
print(compress)

val2 = input("Enter compressed string:")
num = 0

length2 = len(val2)
for j in range(length2):
    if val2[j].isalpha():
        print(val2[j],end="")
    if val2[j].isdigit():
        num = int(val2[j])
        for i in range(num-1):
            print(val2[j-1],end="")
