from datetime import datetime
instance=datetime.now()
print(instance.strftime("%A, %d. %B %Y %I:%M%p"))
print("It is {0:%d} {0:%A} , {0:%B} {0:%Y} {0:%I}:{0:%M} {0:%p} ".format(instance))
