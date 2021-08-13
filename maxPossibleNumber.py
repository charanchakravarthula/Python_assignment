from itertools import permutations
inputList=list(map(int,input().split()))
l=[]
for i in permutations(inputList,len(inputList)):
    l.append("".join(map(str,i)))
print(max(l))