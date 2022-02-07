#important function of List

# 2D list creating
lis = []
temp = []

for i in range(2):
    value = list(map(int,input("Enter values").split()))
    lis.append(value)

print(lis)
print(lis[0][1])

#using format for specific decimal point
value = float(input("Enter float:"))
print("{:0.2f}".format(value))

#iterating by division
i = 123
while i != 0:
  print(i%10)
  i = i//10

#stack in python
stack = [1,2,3]
stack.append(4)
stack.append(5)
stack.pop()
print(stack)

#queue in python
queue = [1,2,3,4]
queue.append(5)
queue.append(6)
queue.pop(0)
print(queue)

#Double ended queue
Dqueue = [1,2,3,4]

Dqueue.insert(0,100) #push front
Dqueue.pop(0) #pop front

Dqueue.append(200) #push back
Dqueue.pop() #pop back
#print(queue)

#Dictionary
Dic = {}
lis = ['name','age','id']
value = ['Towhid',23,135]
for i in range(len(lis)):
  Dic[ lis[i] ] = value[i]
print(Dic[lis[0]])

#pair in python
#if we want to assign in tuple, we need to assign a full new pair value
pair = ('towhid',2)
print(pair[1])

#file input in python
f = open("input.txt","r")
lis = []
if f.mode == "r":
  for i in range(2):
    contents = f.readline()
    lis.append( list(map(int,contents.split()) ) )
print(lis)'''

