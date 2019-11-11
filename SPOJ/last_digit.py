def bin_exp(a, b):
    if b == 0:
        return 1
    
    if a == 0:
        return 0
    
    res = bin_exp(a, b >> 1) % 10
    
    if b % 2 == 0:
        return (res * res) % 10
    else:
        return (a * res * res) % 10


def main():
    
    t = int(input())
    
    for _ in range(t):
        
        a, b = [int(k) for k in input().split()]
        print(bin_exp(a, b) % 10)
    

if __name__ == '__main__':
    main()