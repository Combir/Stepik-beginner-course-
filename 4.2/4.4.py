a = int(input())
if 1000 <= a <= 9999:
    if a % 7 == 0 or a % 17 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

### 2 способ ###

a = int(input())
if len(str(a)) == 4 and (a % 7 == 0 or a % 17 == 0):
    print("YES")
else:
    print("NO")