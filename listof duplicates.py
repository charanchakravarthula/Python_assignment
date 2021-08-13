inputlist=input().split()
temp_dic={}
for i in inputlist:
    if(i in temp_dic.keys()):
        temp_dic[i]+=1
    else:
        temp_dic[i]=1
duplicates=[]
for i in temp_dic.keys():
    if(temp_dic[i]>1):
        duplicates.append(i)
print(duplicates)