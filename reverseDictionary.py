dic={'a':1,"b":2,"c":3,"d":4}
newdic={}
for i in dic.items():
    newdic[i[1]]=i[0]
print(newdic)
# dic comprehension
newdic2={v:k for k,v in dic.items()}
print(newdic2)