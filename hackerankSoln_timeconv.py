k=list(map(str,input().split(":")))
if "AM" in k[2]:
    if(int(k[0])==12):
        p=int(k[0])-12
        print(str(0)+str(p)+":"+k[1]+":"+k[2][0]+k[2][1])
    else:
        p=0+((12+int(k[0]))-12)
        print(str(0)+str(p)+":"+k[1]+":"+k[2][0]+k[2][1])
else:
    if "PM" in k[2]:
        if(int(k[0])==12):
            print(str(k[0])+":"+k[1]+":"+k[2][0]+k[2][1])
        else:
            p=int(k[0])+12
            print(str(p)+":"+k[1]+":"+k[2][0]+k[2][1])
  
