f=open("question_3.txt","r")
a=f.readlines()
for i in a:
    if "delhi" in i:
        f1=open("delhi.txt","a")
        f1.write(i)
        f1.write("\n")
    elif "shimla" in i:
        f2=open("shimla.txt","a")
        f2.write(i)
        f2.write("\n")
    else:
        f3=open("others.txt","a")
        f3.write(i)
        f3.write("\n")
f.close()