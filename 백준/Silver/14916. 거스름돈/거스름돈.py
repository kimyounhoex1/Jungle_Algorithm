import sys

price = int(sys.stdin.readline())

if price==1 or price==3:
    print(-1)
else:
    if price % 5 == 1:
        price = int(price/5)+2
    elif price % 5 == 2:
        price = int(price/5)+1
    elif price % 5 == 3:
        price = int(price/5)+3
    elif price % 5 == 4:
        price = int(price/5)+2
    else:
        price = int(price/5)
    print(price)