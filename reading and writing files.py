
with open("./random.txt","r") as f:
    with open("./copyrandom.txt","w") as e:
        e.write(f.read())

