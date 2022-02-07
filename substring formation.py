string = input("Enter string:")
substring = input("Enter string:")
flag=0
count=0
count_sub = 0

string_len = len(string)
mark_string = [0]*string_len
substring_len = len(substring)
mark_substring = [0]*substring_len

while 1:
    for i in range(string_len):
        still_there_is_zero = 0
        if mark_string[i] == 0:
            still_there_is_zero = 1
            if string[i] not in substring:
                mark_string[i] = 1
            for j in range(substring_len):
                if mark_substring[j]==0:
                    if string[i]==substring[j]:
                        mark_string[i] = 1
                        mark_substring[j] = 1
                        count += 1
                        if count == substring_len:
                            count_sub += 1
                            count = 0
                            mark_substring = [0] * substring_len

                        break
    if 0 not in mark_string:
        break

print(count_sub)
print(mark_string)
#print(mark_string)
#print(mark_substring)




