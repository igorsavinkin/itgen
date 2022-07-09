a = [int(i) for i in input().split()]
sum_ = 0
if len(a) == 0:
    print(0)
    print(0)
else:
    b = a[0]

    for i in range(0, len(a),2):
        sum_ += a[i]
    print(sum_)
    print( sum_ * b )
