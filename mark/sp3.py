i = [int(m)for m in input().split()]
i.sort(reverse=True)
print(*i[:3])
