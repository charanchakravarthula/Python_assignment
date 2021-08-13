temp_dic={}
dict
inputString=input()
for i in inputString:
    if(i in temp_dic.keys()):
        temp_dic[i]+=1
    else:
        temp_dic[i]=1
for i in inputString:
    if(temp_dic[i]==1):
        print(i)
        break
