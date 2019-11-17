#include <bits/stdc++.h>

using namespace std;

void permutate(string s, int l, int r) {
    if (l == r) {
        cout << s << endl;
    }
    else {
        for (int i = l; i <= r; i++){
            swap(s[i], s[l]);
            permutate(s, l + 1, r);
            swap(s[i], s[l]);
        }
    }
}

int main() {
    string s = "abc";
    int n = s.size();
    permutate(s, 0, n - 1);
    return 0;
}