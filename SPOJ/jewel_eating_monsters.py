md = 10 ** 7 + 7

def bin_exp(a, b):
    if b == 0:
        return 1
    
    if a == 0:
        return 0
    
    res = bin_exp(a, b >> 1) % md
    
    if b % 2 == 0:
        return (res * res) % md
    else:
        return (a * res * res) % md


while True:
    n, k = list(map(int, input().split()))
    if n == 0 and k == 0:
        break
    ans = (bin_exp(n, k) + bin_exp(n, n) + 2 * bin_exp(n - 1, k) + 2 * bin_exp(n - 1, n - 1)) % (10 ** 7 + 7)
    print(ans)
