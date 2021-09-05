banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("exercise.txt","w")
i=0
while i<len(banks_list):
    f.write(banks_list[i])
    f.write("\n")
    i+=1
f.close()
