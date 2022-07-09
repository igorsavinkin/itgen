a = input().split()
b = input().split()
for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i]:
            print(a[j])
