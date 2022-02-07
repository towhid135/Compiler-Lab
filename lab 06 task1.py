import re

number = []
operator_list = ["+","-","*","/"]
operator = []

val = input(("enter the operation:"))
length = len(val)

number = re.findall(r"\d+", val)

for i in range(length):
    if val[i] in operator_list:
        operator.append(val[i])
len_num = len(number)
len_opt = len(operator)
for i in range(len_num):
    number[i] = int(number[i])
indx = 0
for i in range(len_num-1):
    if operator[i] == "+":
        number[i+1] = number[i]+number[i+1]
    if operator[i] == "-":
        number[i + 1] = number[i] - number[i+1]
    if operator[i] == "*":
        number[i + 1] = number[i] * number[i+1]
    if operator[i] == "/":
        number[i + 1] = number[i] / number[i+1]

print(number[i+1])