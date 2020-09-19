def a():
    n, k = input().split(' ')
    top_line = int(n)
    k = int(k)
    count = 0
    for i in range(1, top_line + 1):
        if not k % i and i * top_line >= k:
            count += 1
    return count


a()
