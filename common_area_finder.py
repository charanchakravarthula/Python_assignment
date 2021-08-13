class area:
    def __init__(self,*args):
        if len(args)==1:
            print(args[0]*args[0])
        elif len(args)==2:
            print(args[0]*args[1])
area(2)
area(2,3)