def get_all_perms(ar, l, r):
    if l == r:
        ans = list()
        for j in range(len(ar[0])):
            _ans = ""
            for el in ar:
                _ans += el[j]
            
            print (_ans)
    else:
        for i in range(r + 1):
            ar[l], ar[i] = ar[i], ar[l]
            get_all_perms(ar, l + 1, r)
            ar[l], ar[i] = ar[i], ar[l]

def possibleWords(a, N):
    dict = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m',' n', 'o'],
    }
    b = list()

    get_all_perms(ar, 0, N - 1)

ar = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]