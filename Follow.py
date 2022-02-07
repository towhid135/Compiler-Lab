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

print("Printing First")
print("{}{:^30}".format("Key","First"))
for key in key_list:
    hold_First = first(key)
    First[key] = hold_First
    print("{}{:^30}".format(key,str(First[key])))

Follow = {}

def follow(key):
    set_value1 = set()
    if key == key_list[0]:
        set_value1.add("$")
    for singlKey in key_list:
        if singlKey != key:
            for i in range(  len(Grammers[singlKey]) ):
                if Grammers[singlKey][i] == key: #if variable is found
                    if ( i+1 >= len( Grammers[singlKey] ) ) or (Grammers[singlKey][i+1]=="|"):
                        set_value1 = Follow[singlKey]
                    elif Grammers[singlKey][i+1] in Terminal:
                        set_value1.add(Grammers[singlKey][i+1])
                    elif Grammers[singlKey][i+1] in NonTerminal:
                        for first1 in First[ Grammers[singlKey][i+1] ]:
                            if first1 != "#":
                                set_value1.add(first1)
                            else:
                                for follow1 in Follow[singlKey]:
                                    set_value1.add(follow1)

    Follow[key] =  set_value1




for key in key_list:
    follow(key)
print("Printing Follow")
print("{}{:^30}".format("Key","Follow"))
for key in key_list:
    print("{}{:^30}".format(key,str(Follow[key])))
