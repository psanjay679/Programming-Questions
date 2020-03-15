dp = list()


def is_word_break(s, idx, word_set):

    global dp

    if idx == len(s):
        return True

    if dp[idx] is not None:
        return dp[idx]

    word = ""
    ans = False

    for i in range(idx, len(s)):
        word += s[i]

        if word in word_set:
            ans = ans or is_word_break(s, i + 1, word_set)

    dp[idx] = ans

    return ans




s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
word_set = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

dp = [None] * len(s)

print(is_word_break(s, 0, word_set))