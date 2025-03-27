from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))
    count = 0

    while q:
        poprint = q[0]  

        if poprint < max(q): 
            q.append(q.popleft()) 
            if M == 0:  
                M = len(q) - 1 
            else:
                M -= 1  
        else:
            count += 1
            q.popleft()  
            if M == 0:  
                print(count)
                break
            M -= 1