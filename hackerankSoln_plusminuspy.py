n=int(input())
l=list(map(int,input().split()))[:n]
c=0
s=0
k=0
for i in range(len(l)):
    if(l[i]>0):
        c+=1
    elif(l[i]==0):
        s+=1
    else:
        k+=1
c=c/len(l)
s=s/len(l)
k=k/len(l)
print('%.6f'%(c))
print('%.6f'%(k))
print('%.6f'%(s))





