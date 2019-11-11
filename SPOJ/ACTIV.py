def get_ans(ar):
    
    ans = [0] * len(ar)
    
    for i in range(len(ar) - 1, 0, -1):
        j = 0
        while ar[j][1] <= ar[i][0]:
            ans[]
    

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == -1:
            break
        
        ar = list()
        a, b = [int(k) for k in input().split()]
        ar.append([a, b])
        ar.sort(key=lambda k: k[1])