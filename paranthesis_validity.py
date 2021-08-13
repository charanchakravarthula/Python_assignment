paran_string=input()
stack=[]
counter=0
for i in paran_string:
    if(i=='('):
        stack.append(i)
    elif(i==')' and len(stack)):
        stack.pop()
    else:
        print("false")
        counter=1
        
if(len(stack)):
    print("false")
else:
    if(not counter):
        print("true")