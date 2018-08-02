
str=raw_input("Enter string\n");
arrC=[0]*150
for c in str:
    arrC[ord(c)]+=1
fnd=0
for i in range(150):
    if(arrC[i]>1):
        print("not unique")
        fnd=1
        break
if(fnd==0):
    print("unique")