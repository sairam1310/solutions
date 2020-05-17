k=list(map(int,input().split()))[:5]
s=sum(k)
max=s-max(k)
min=s-min(k)
print(max,min)
    
    
