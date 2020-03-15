#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <libc.h>
#include <unordered_set>

using namespace std;

class Solution {
    public:
        vector<int> solve(int A, int B, vector<int> &C);
};

int binSearchB(int pow1, int B, int C) {
    
    int low = 0;
    int high = 31;
    int mid;
    int ans = -1;

    while (low < high) {
        mid = (low + high) / 2;
        if (pow1 + pow(B, mid) < C) {
            ans = mid;
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    return ans;
}

int findScaryCount(int A, int B, int C)
{
    int cnt = 0;

    if (A != 1 && B != 1) {

        for (int x = 0; x < 31; x++)
        {
            int k = binSearchB(pow(A, x), B, C);
            if (k != -1) {
                cnt += k;
            }
        }
        return max(0, cnt - 1);
    }

    if (B == 1) {
        swap(A, B);

        int cnt = 0;
        for (int i = 0; i < 31; i++) {
            if (1 + pow(B, i) < C) {
                cnt += 1;
            }
            else {
                break;
            }
        }

        return cnt;
    }
}

vector<int> Solution::solve(int A, int B, vector<int> &C)
{
    vector<int> ans;

    for (int i = 0; i < C.size(); i++)
    {
        ans.push_back(findScaryCount(A, B, C[i]));
    }

    return ans;
}

void printVector(vector<int> ans) {
    
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << endl;
}
