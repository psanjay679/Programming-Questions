def is_substr(s, i1, i2, l):
    for i in range(l):
        if s[i1] != s[i2]:
            return False

        i1 += 1
        i2 += 1

    return True


def rabin_karp(s, l):

    p = 0
    d = 256
    q = 31

    h = 1
    for i in range(l - 1):
        h = (h * d) % q

    for i in range(l):
        p = (d * p + ord(s[i])) % q

    word_map = dict()
    word_map[p] = 0

    for i in range(l, len(s)):
        p = (d * (p - h * ord(s[i - l])) + ord(s[i])) % q

        if p in word_map:
            if is_substr(s, word_map[p], i - l + 1, l):
                return True
        else:
            word_map[p] = i - l

