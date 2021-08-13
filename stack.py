
class stack:
    def __init__(self,l=[]):
        self.stackobj=l
        self._top=len(self.stackobj)-1
    def push(self,element):
        self.stackobj.append(element)
        self._top+=1
    def pop(self):
        self.stackobj=self.stackobj[0:len(self.stackobj)-1]
        self._top-=1
    def max(self):
        max_val=self.stackobj[0]
        for i in self.stackobj:
            if i>max_val:
                max_val=i
        return max_val
    def min(self):
        min_val=self.stackobj[0]
        for i in self.stackobj:
            if i<min_val:
                min_val=i
        return min_val
    @property
    def top(self):
        return self.stackobj[self._top]
    def __str__(self):
        return " ".join(map(str,self.stackobj[-1::-1]))
 
a=stack([1,2,3,4,5,6])
a.push(10)
a.pop()
print(a.top)
print(a)
print(a.max())
print(a.min())