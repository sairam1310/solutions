x1,v1,x2,v2=list(map(int,input().split()))
if((x2 > x1 and v2 >= v1) or ((x1-x2) % (v2-v1)) != 0):
    print("NO")
else:
    print("YES")
