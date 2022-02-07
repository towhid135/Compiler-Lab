Terminal = ["+", "-", "(", ")", "[", "]", "*","#"]
Epsilon = "#"
NonTerminal = []
Grammers = {} #dictionary
First = {} #dictionary
# taking terminals and non-terminals
for i in range(97, 123):
    Terminal.append(chr(i))
    NonTerminal.append(chr(i - 32))

#print(Terminal)
#print(NonTerminal)
#Taking grammers
TotalGrammer = int(input("Enter Total Number of Grammer:"))
for i in range(TotalGrammer):
  SingleGrammer = input()
  hold = SingleGrammer.split("=")
  Grammers[ hold[0] ] = hold[1]

#print(Grammers)

key_list = list(Grammers.keys()) #keeps all the left hand side values
#print(key_list)
def first(key):
   temp_First = {}
   set_value = set()
   sum1 = ""
   if Grammers[key][0] in Terminal:
       for i in range(len(Grammers[key])):
           if Grammers[key][i] not in Terminal:
               break
           else:
               sum1 += Grammers[key][i]
       set_value.add( sum1 )
       temp_First[key] = set_value
       length = len(Grammers[key])
       for i in range(length):
           if Grammers[key][i] == "|":
               set_value.add(Grammers[key][i+1])
               temp_First[key] = set_value
               break
   else:
       hold_First = first(Grammers[key][0])
       temp_First[key] = hold_First

   return temp_First[key]

print("{}{:^30}".format("Key","First"))
for key in key_list:
    hold_First = first(key)
    First[key] = hold_First
    print("{}{:^30}".format(key,str(First[key])))





