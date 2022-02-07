
# transition for if
'''iteration = int(input("Enter Iteration Number: "))
for i in range(iteration+1):
  val = input("Enter Input: ")
  index = 0;
  last_index = len(val)-1
  state = 0;
  if state==0:
    if val[index]=="i" and index != last_index:
      state += 1;
      index += 1;
    else:
      print("identifier")
  if state == 1:
    if val[index] == "f" and index == last_index:
      print("keyword")
    else:
      print("identifier")'''
index = 0
state = 0
count = 0
dic = {1:"less than",2:"greater than",3:"equal",4:"not"}
iterator = int(input("Enter Iteration: "))
for i in range(iterator):
  index = 0
  state = 0
  sign = 0
  sign1 = 0
  val = input("Enter Operator: ")
  last_index = len(val)-1;
  if state==0:
    if val[index]=="<":
      state += 1
      sign = 1
    elif val[index]==">":
      state += 1
      sign = 2
    elif val[index]=="=":
      state += 1
      sign = 3
    else:
      state += 1
      sign = 4
  if state==1:
    if index == last_index:
      print(dic[sign])
    else:
      index += 1
      state += 1
  if state==2:
    if val[index]=="=":
      sign1 = 3
      print(dic[sign],end=" ")
      if sign1 != 0:
          print(dic[sign1])
#print(count)
