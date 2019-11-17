def permutate(s, l, r):
    if l == r:
        print(s)
    else:
        for i in range(1, r + 1):
            s[l], s[i] = s[i], s[l]
            permutate(s, l + 1, r)
            s[l], s[i] = s[i], s[l]

s = ['a', 'b', 'c']
permutate(s, 0, 2)