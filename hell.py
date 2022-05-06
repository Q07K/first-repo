for i in range(1, 21):
    if i % 15 == 0:
        a = 'yeardream'
    elif i % 3 == 0:
        a = 'year'
    elif i % 5 == 0:
        a = 'dream'
    else:
        a = i
    print(a)
