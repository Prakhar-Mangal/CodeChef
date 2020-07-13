t = int(input())

for _ in range(t):
    n = int(input())
    dx ={} 
    dy = {}
    for i in range(4*n-1):
        x,y = list(map(int, input().split()))
        if x in dx:
            dx[x]+=1 
        else:
            dx[x] = 1
        if y in dy:
            dy[y]+=1 
        else:
            dy[y] = 1
    for x in dx:
        if dx[x]%2 != 0:
            print(x,end=" ")
    for y in dy:
        if dy[y]%2 != 0:
            print(y,end=" ")
    print()
   