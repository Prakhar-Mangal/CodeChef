t = int(input())

for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    s = list(map(int, input().split()))
    m = min(min(f),min(s))
    count = {}
    swap_list = []
    swap = 0
    for K in range(n):
        if f[K] in count:
            count[f[K]] += 1
        else:
            count[f[K]] = 1
            
    for K in range(n):
        if s[K] in count:
            count[s[K]] -= 1
        else:
            count[s[K]] = -1
       
    for key, value in  count.items():
        if value == 0: pass
        elif value % 2 == 0:
            diff = int(abs(value) / 2)
            swap += diff
            for i in range(diff):
                swap_list.append(min(key,2*m))
        else:
            swap = -1
            break
        
    if swap == 0:
        print(0)
    elif swap == -1 or swap % 2 == 1:
        print(-1)
    else:
        swap = int(swap/2)
        swap_list.sort()
        # print(listA[:swap])
        ans = sum(swap_list[:swap])
        print(ans)
