# t, k = input().split()
# t, k = int(t), int(k)
# lst = []
# for inpt in range(1, t + 1):
#     m, n = input().split()
#     lst.append((int(m), int(n),))
#
# for el in lst:
#     even = (el[0] - 1) + (el[1] - 1)
#     count = (min(el) - 1) // k
#     if not count:
#         if not even:
#             print('-')
#         elif even % 2:
#             print('+')
#         else:
#             print('-')
#     elif count == 1:
#         if even % 2:
#             if min(el) - 1 <= k:
#                 print('+')
#             else:
#                 print('-')
#         else:
#             print('+')
#     elif count % 2:
#         if even % 2:
#             if k == 1:
#                 print('-')
#             else:
#                 print('+')
#         else:
#             if k == 1:
#                 print('+')
#             elif ((min(el) - 1) - (k * count)) % 2:
#                 print('-')
#             elif not ((min(el) - 1) - (k * count)) % 2:
#                 print('+')
#             else:
#                 print('-')
#     else:
#         if even % 2:
#             print('-')
#         else:
#             print('+')

t, k = input().split()
t, k = int(t), int(k)
lst = []
for inpt in range(1, t + 1):
    m, n = input().split()
    lst.append((int(m), int(n)))

for el in lst:
    even = (el[0] - 1) + (el[1] - 1)
    count = (min(el) - 1) // k
    ostatok = (min(el) - 1) % k
    if not even:
        print('-')
    elif even % 2:
        if not count:
            print('+')
        elif count == 1:
            if (min(el) - 1) <= k:
                print('+')
            else:
                print('-')
        elif count % 2:
            if k == 1:
                print('+')
            elif not ostatok:
                print('+')
            elif ostatok % 2:
                print('-')
            else:
                print('+')
        else:
            if k == 1:
                print('+')
            elif not ostatok:
                print('-')
            elif ostatok % 2:
                print('+')
            else:
                print('+')
    else:
        if not count:
            print('-')
        elif count == 1:
            print('+')
        elif count % 2:
            if k == 1:
                print('+')
            elif not ostatok:
                print('-')
            elif ostatok % 2:
                print('-')
            else:
                print('+')
        else:
            if k == 1:
                print('-')
            elif not ostatok:
                print('+')
            elif ostatok % 2:
                print('+')
            else:
                print('-')

