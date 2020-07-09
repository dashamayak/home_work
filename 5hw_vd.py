dict1 = {key: value for key, value in zip(['2о21', 'd22', 'n1', 'l', 's', '3'], ['МЕТТРЕЙД', 'АГРОСФЕРА', 'ОПТОВИК', 'Промтехмаш', 'ОПТОВИК', 'АГРОСФЕРА1'])}
l1 = []
l2 = []
del_k = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'w', 'a', 's', 'd']
for key, value in dict1.items():
    if key[-1] != del_k[0]:
        l1.append(value)
    else:
        l2.append(value)
print(l1)
print(l2)
l1_set = (set(l1))
l2_set = (set(l2))
print(l1_set.intersection(l2_set))

