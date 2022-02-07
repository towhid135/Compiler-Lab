import re

keyword = ["int","float","double","scanf","printf","do","while","for","if","else"]
operator = ["+","-","=","/","<",">","*"]
special_char = ["(",")",",",";"]
lis = []
key_lis = []
operator_lis = []
numerical = []
variable = []
variable1 = []

str = input("Enter the string: ")

lis = str.split()

result = re.findall(r"\d*\.\d+|\d+", str)

"""for num in lis:
   if num.isdigit():
      numerical.append(int(num))
print(num) """


for j in str:
    if j in operator:
        if j not in operator_lis:
            operator_lis.append(j)

for i in range(len(lis)):
    if lis[i] in keyword:
        key_lis.append(lis[i])
    if lis[i] not in keyword:
        if lis[i] not in operator:
            if lis[i] not in special_char:
                variable.append(lis[i])
for var in variable:
    if var.isalpha():
        if var not in variable1:
            variable1.append(var)


print("keywords: ",key_lis,",operator: ",operator_lis,",Number: ",result,",variable: ",variable1)
