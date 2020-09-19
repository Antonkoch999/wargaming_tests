
# Входные данные
n = int(input())
a1, a2, a3, a4, a5, a6, a7, a8, a9 = input().split(' ')


final_list = []
list_tuple = [(1, int(a1)), (2, int(a2)), (3, int(a3)), (4, int(a4)),
              (5, int(a5)), (6, int(a6)), (7, int(a7)), (8, int(a8)),
              (9, int(a9))]

list_tuple.sort(key=lambda x: (x[1], -x[0]))
dct = dict(list_tuple)

general_number = n // list_tuple[0][1]
for count_number in range(1, general_number + 1):
    final_list.append(str(list_tuple[0][0]))
first_modulo = n % list_tuple[0][1]
if n < list_tuple[0][1]:
    print(-1)
else:
    while first_modulo:
        last_number = final_list[-1]
        final_list.pop()
        last_gold = first_modulo + dct[int(last_number)]
        for key in dct.keys():
            if last_gold // dct[key]:
                if key > int(last_number):
                    last_number = key
        final_list.append(str(last_number))
        final_list.sort(reverse=True)
        first_modulo = last_gold % dct[int(last_number)]
        if int(last_number) == int(final_list[-1]):
            break
    print(''.join(final_list))
