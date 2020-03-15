#include <vector>
#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

// struct Pair {
//     int first;
//     int second;

//     Pair(int first, int second){
//         first = first;
//         second = second;
//     }
// };

class Solution {
    public:
        int candy(vector<int> &A);
};

int assigValue(vector<pair<int, int> > pr, int index) {
    
    int leftVal;
    int rightVal;
    
    if (index == 0 || pr[index - 1].second == NULL) {
        leftVal = 0;
    }
    else {
        leftVal = pr[index - 1].second;
    }

    if (index + 1 == pr.size() || pr[index + 1].second == NULL) {
        rightVal = 0;
    }
    else {
        rightVal = pr[index + 1].second;
    }

    return max(leftVal, rightVal) + 1;
}

int Solution::candy(vector<int> &A) {

    vector<pair<int, int> > pa;

    for(int i = 0; i < A.size(); i++) {
        pa.push_back(make_pair(A[i], i));
    }

    sort(pa.begin(), pa.end());

    // for (int i = 0; i < pa.size(); i++) {
    //     cout << pa[i].first << " " << pa[i].second << endl;
    // }

    

    return 0;
}

int main() {
    vector<int> A;
    A.push_back(1);
    A.push_back(5);
    A.push_back(3);
    A.push_back(4);
    A.push_back(2);

    Solution s;
    s.candy(A);
    return 0;
}