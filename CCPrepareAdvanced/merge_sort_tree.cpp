#include <bits/stdc++.h>

using namespace std;

// vector<int> combine(vector<int> a, vector<int> b) {
//     vector<int> ans;
//     int i = 0;
//     int j = 0;

//     while (i < a.size() && j < b.size()) {
//         if (a[i] < b[j]) {
//             ans.push_back(a[i++]);
//         }
//         else{
//             ans.push_back(b[j++]);
//         }
//     }
    
//     while (i < a.size()) {
//         ans.push_back(a[i++]);
//     }
//     while (j < b.size()) {
//         ans.push_back(b[j++]);
//     }

//     return ans;
// }

void build(vector<int> tree[], int ar[], int node, int start, int end) {
    
    if (start == end) {
        tree[node] = vector<int>(1, ar[start]);
    }
    
    else {
        int mid = start + (end - start) / 2;
        build(tree, ar, 2 * node + 1, start, mid);
        build(tree, ar, 2 * node + 2, mid + 1, end);

        merge(tree[2 * node + 1].begin(), tree[2 * node + 1].end(),
            tree[2 * node + 2].begin(), tree[2 * node + 2].end(),
            back_inserter(tree[node]));
    }
}

// void print_vector(vector<int> v) {

//     cout << "Printing the vector..." << endl;
//     for (auto it = v.begin(); it != v.end(); it++) {
//         cout << *it << " ";
//     }
//     cout << endl;
// }

int query(vector<int> tree[], int node, int start, int end, int left, int right, int value) {
    
    if (start > end || left > end || right < start)
        return 0;
    
    if (start == left && right == end) {

        vector<int>::iterator pos = lower_bound(tree[node].begin(), tree[node].end(), value);
        // print_vector(tree[node]);

        // cout << "pos_val: " << pos - tree[node].begin() << endl;

        if (pos == tree[node].begin()) {
            return tree[node].size();
        }
        else {
            if (pos == tree[node].end()) {
                return 0;
            }

            return tree[node].end() - pos;
        }
    }
    else {
        
        int mid = start + (end - start) / 2;
        return query(tree, 2 * node + 1, start, mid, left, min(right, mid), value) + 
                query(tree, 2 * node + 2, mid + 1, end, max(mid + 1, left), right, value);
    }
}

// void update(multiset<int> tree[], int ar[], int node, int start, int end, int index, int value) {
    
//     tree[node].erase(tree[node].find(ar[index]));
//     tree[node].insert(value);

//     if (start != end) {
//         int mid = start + (end - start) / 2;
//         if (index <= mid) {
//             update(tree, ar, 2 * node + 1, start, mid, index, value);
//         }
//         else {
//             update(tree, ar, 2 * node + 2, mid + 1, end, index, value);
//         }
//     }else {
//         ar[index] = value;
//     }
// }

int main() {
    
    int n;
    scanf("%d", &n);

    int ar[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &ar[i]);
    }

    vector<int> tree[4 * n + 1];
    build(tree, ar, 0, 0, n - 1);

    int t;
    scanf("%d", &t);

    int l, r, x;
    while (t--) {

        scanf("%d%d%d", &l, &r, &x);

        int ans = query(tree, 0, 0, n - 1, l - 1, r - 1, x + 1);
 
        printf("%d\n", ans);
    }

    return 0;
}