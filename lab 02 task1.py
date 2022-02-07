keyword = ["int","float","double","scanf","printf","do","while","for","if","else"]
invalid = [" ","!","@","#","$","%","^","&","*","(",")","{","}","[","]","+","-","/","\\",'|',"'",'"',]
num = ['0','1','2','3','4','5','6','7','8','9']

Iteration = int(input('Total iteration: '))
for It in range(1,Iteration+1):
    str = input("Enter your input:")
    flag = True  # true means valid
    if len(str) > 31:
        flag = False
    else:
        # print("yes1")
        if (str[0] in num):
            # print("yes2")
            flag = False
        else:
            # print("yes3")
            for i in invalid:
                for j in str:
                    if i == j:
                        flag = False
                if flag == False:
                    break
            if str in keyword:
                flag = False
    if flag == True:
        print("Valid")
    else:
        print("Invalid")





