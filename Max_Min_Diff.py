num_string=input()
temp_dic={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for i in num_string:
    temp_dic[i]=temp_dic[i]+1
max_num=0
for i in range(9,-1,-1):
    for j in range(0,temp_dic[str(i)]):
        max_num=max_num*10+int(i)
min_num=0
for i in range(1,10):
    if(temp_dic[str(i)]):
        min_num=min_num*10+int(i)
        temp_dic[str(i)]=temp_dic[str(i)]-1
        break
for i in range(0,10):
    for j in range(0,temp_dic[str(i)]):
        min_num=min_num*10+int(i)

print(max_num-min_num)

    
