val = input("Enter parenthesis: ")

correct_flag = 0
valid_flag = 0
index_f1 = []
index_f2 = []
count_f1 = 0
count_f2 = 0
length = len(val)

# first bracket
for i in range(length):
    if val[i] == "(":
        index_f1.append(i)
    if val[i] == ")":
        index_f2.append(i)

if len(index_f1) == len(index_f2):
    correct_flag = 1
if correct_flag == 1:
    for i in range(len(index_f1)):
        if index_f1[i] > index_f2[i]:
            correct_flag = 0
            break
if correct_flag == 1:
    valid_flag = 1
#if valid_flag==1:
    #print("valid")

if valid_flag == 1:
    # Second bracket
    correct_flag = 0
    index_f1 = []
    index_f2 = []
    for i in range(length):
        if val[i] == "{":
            index_f1.append(i)
        if val[i] == "}":
            index_f2.append(i)

    if ( len(index_f1) != 0 ) and ( len(index_f2) != 0 ):
        if (len(index_f1) == len(index_f2)):
            correct_flag = 1
        if correct_flag == 1:
            for i in range(len(index_f1)):
                if index_f1[i] > index_f2[i]:
                    correct_flag = 0
                    break
        if correct_flag == 0:
            valid_flag = 0
        if correct_flag == 1:
            valid_flag = 1
    elif (len(index_f1) == 0) and (len(index_f2) != 0):
        valid_flag = 0
    elif (len(index_f1) != 0) and (len(index_f2) == 0):
        valid_flag = 0

if valid_flag == 1:
    # third bracket
    correct_flag = 0
    index_f1 = []
    index_f2 = []
    for i in range(length):
        if val[i] == "[":
            index_f1.append(i)
        if val[i] == "]":
            index_f2.append(i)

    if (len(index_f1) != 0) and (len(index_f2) != 0):
        if len(index_f1) == len(index_f2):
            correct_flag = 1
        if correct_flag == 1:
            for i in range(len(index_f1)):
                if index_f1[i] > index_f2[i]:
                    correct_flag = 0
                    break
        if correct_flag == 0:
            valid_flag = 0
        if correct_flag == 1:
            valid_flag = 1
    elif (len(index_f1) == 0) and (len(index_f2) != 0):
        valid_flag = 0
    elif (len(index_f1) != 0) and (len(index_f2) == 0):
        valid_flag = 0


if valid_flag==1:
    print("valid")
if valid_flag == 0:
    print("invalid")