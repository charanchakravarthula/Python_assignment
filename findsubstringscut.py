palindromic_substrings=[]
def palindrome(str):
    if(len(str)<=1):
        return False
    if(str==str[-1::-1]):
        return True
    else:
        return False
def sub(str):
    for p in range(0,len(str)):
        for q in range(p+1,len(str)+1):
            if(p==0 and q==len(str)+1):
                split=0
            elif(p!=0 and q!=len(str)+1):
                split=2
            else:
                split=1
            if(palindrome(str[p:q])):   
                palindromic_substrings.append((str[p:q],split))
sub(input())
for i in palindromic_substrings:
    print(i[0],"=>",i[1])



