n=int(input())
s=[]
for i in range(n):
    k=int(input())
    s.append(k)
for i in range(len(s)):
    if(s[i]>=38):
        a=(s[i]//5)*5
        b=a+5
        if(s[i]-a>b-s[i]):
            x=b
            if(x-s[i]<3):
                print(x)
            elif(x-s[i]==3):
                print(s[i])
        else:
            x=a
            if(x-s[i]<3):
                print(s[i])
            elif(x-s[i]==3):
                print(x)
    else:
        print(s[i])
