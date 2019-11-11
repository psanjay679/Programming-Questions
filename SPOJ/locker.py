md = 10**9 + 7


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


def main():
    t = int(input())
    
    for _ in range(t):
        
        n = int(input())
        if n <= 3:
            print(n)
        else:
            if n % 2 == 0:
                print(bin_exp(2, n >> 1))
            else:
                print(bin_exp(2, (n >> 1) - 1) * 3)
        
        
if __name__ == '__main__':
    main()
