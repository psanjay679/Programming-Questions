def prefix_function(s):
    ans = [0] * len(s)
    
    for i in range(1, len(s)):
        j = ans[i - 1]
        
        while j > 0 and s[i] != s[j]:
            j = ans[j - 1]
        
        if s[i] == s[j]:
            j += 1
        
        ans[i] = j

    return ans


t = int(input())
while t > 0:
    s = input()
    k = len(s) - prefix_function(s)[-1]
    if len(s) % k == 0:
        print(k)
    else:
        print(len(s))
    
    t -= 1
#
# def compute_automation(s):
#     s += '#'
#     n = len(s)
#     pi = prefix_function(s)
#     aut = list()
#
#     for _ in range(n):
#         aut.append([0] * 26)
#
#     for i in range(n):
#         for c in range(26):
#             j = i
#             while j > 0 and s[i] != chr(c + 97):
#                 j = pi[j - 1]
#
#             if s[i] == chr(c + 97):
#                 j += 1
#
#             aut[i][c] = j
#
#     return aut
#
#
# def compute_automation_dp(s):
#     s += '#'
#     n = len(s)
#     pi = prefix_function(s)
#     aut = list()
#
#     for i in range(n):
#         aut.append([0] * 26)
#
#     for i in range(n):
#         for c in range(26):
#
#             if i > 0 and chr(c + 97) != s[i]:
#                 aut[i][c] = aut[pi[i - 1]][c]
#             else:
#                 if s[i] == chr(c + 97):
#                     aut[i][c] = i + 1
#                 else:
#                     aut[i][c] = i
#     return aut
#
#
# if __name__ == '__main__':
#     s = 'aaaaaa'
#     a1 = compute_automation(s)
#     a2 = compute_automation_dp(s)
#     print(a1)
#     print(a2)
#     print(a1 == a2)
