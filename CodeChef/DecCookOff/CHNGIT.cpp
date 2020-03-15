#include <iostream>
#include <vector>
#include <unordered_set>


using namespace std;

int findMinMoves(vector<int> ar) {
    int freqAr[101];
    
    for (int i = 0; i <= 100; i++) {
        freqAr[i] = 0;
    }
    
    int maxFreq = 0;

    for (int i = 0; i < ar.size(); i++) {
        freqAr[ar[i]]++;
        maxFreq = max(maxFreq, freqAr[ar[i]]);
    }

    return ar.size() - maxFreq;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> ar(n, NULL);
        for (int i = 0; i < n; i++) {
            cin >> ar[i];
        }

        cout << findMinMoves(ar) << endl;
    }

    return 0;
}