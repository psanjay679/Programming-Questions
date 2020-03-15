#include <bits/stdc++.h>
#define md 1000000007

using namespace std;

int fib[100000 + 1];
int ar[100000 + 1];


int main() {

    int n;
    int q;
    int a, b;
    int l, r;

    scanf("%d%d", &n, &q);
    scanf("%d%d", &fib[0], &fib[1]);
    scanf("%d%d", &a, &b);

//     cout << n << " " << q << endl;
//     cout << fib[0] << " " << fib[1] << endl;
//     cout << a << " " << b << endl;

    for (int i = 0; i < n; i++) {
        scanf("%d", &ar[i]);
        if (i > 1){
            fib[i] = ((b * fib[i - 1]) % md + (a * fib[i - 2]) % md) % md;
        }
    }

//     for (int i = 0; i < n; i++) {
//         cout << fib[i] << " ";
//     }
//     cout << endl;

    for (int i = 0; i < q; i++) {
        scanf("%d%d", &l, &r);
        for (int i = l - 1; i < r; i++) {
            ar[i] = (ar[i] + fib[i - l + 1]) % md;
        }
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", ar[i]);
    }
    printf("\n");
    return 0;
}