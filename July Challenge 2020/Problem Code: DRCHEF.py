t = int(input())

for _ in range(t):
    n,x = list(map(int, input().split()))
    c = list(map(int, input().split()))
    c.sort()
    d = 0
    i = 0
    while i < n:
        d+=1
        if c[i] - x <= 0:
            x = max(x,2*c[i])
            i+=1 
        else:
            x = 2*x  
    print(d)
        
    