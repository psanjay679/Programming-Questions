#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

int countMinDelete(string s) {
    int zOneCnt = 0;
    int oZeroCnt = 0;

    int start = 0;
    int end;

    // 0101
    while (end < s.length()) {

        while (start < s.length() && s[start] == '1') {
            start++;
        }

        end = start + 1;

        while (end < s.length() && s[end] == '0') {
            end++;
        }

        if (end < s.length()) {
            zOneCnt++;
        }
        start = end;
    }

    start = 0;
    // 1010
    while (end < s.length()) {

        while (start < s.length() && s[start] == '0')
        {
            start++;
        }
        end = start + 1;
        
        while (end < s.length() && s[end] == '1') {
            end++;
        }

        if (end < s.length()) {
            oZeroCnt++;
        }
        start = end;
    }

    return max(oZeroCnt, zOneCnt) - 1;
}

int main() {

    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        cout << countMinDelete(s) << endl;
    }

    return 0;
}