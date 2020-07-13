t = int(input())

def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
  
for _ in range(t):
    n = int(input())
    c1,m1=0,0
    for i in range(n):
        c,m = list(map(int, input().split()))
        cp = sum_digits3(c)
        mp = sum_digits3(m)
        if cp > mp:
            c1+=1 
        elif mp > cp:
            m1+=1 
        else:
            m1+=1 
            c1+=1 
    if c1 > m1:
        print(0,c1)
    elif m1 > c1: 
        print(1,m1)
    else:
        print(2,c1)
        