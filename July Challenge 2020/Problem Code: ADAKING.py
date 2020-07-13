t = int(input())

for _ in range(t):
    n = int(input())
    c = 1
    for i in range(8):
        for j in range(8):
            if i == 0 and j==0:
                print('O',end="")
                c+=1
            elif c <= n:
                print('.',end="")
                c+=1
            else:
                print('X',end="")
        print()
    
