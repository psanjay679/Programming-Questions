#include <stdio.h>

#define INT_MIN -(15008 * 50000)

int min(int a, int b) {
    
    if (a > b) {
        return b;
    }
    return a;
}

int max(int a, int b) {

    if (a > b) {
        return a;
    }

    return b;
}

struct data {
    int sum;
    int ans;
    int pref;
    int suff;
};

struct data make_data(int val) {
    struct data res;
    res.sum = res.pref = res.suff = res.ans = val;
    return res;
}

struct data combine(struct data l, struct data r) {
    
    struct data res;
    res.sum = l.sum + r.sum;
    res.pref = max(l.pref, l.sum + r.pref);
    res.suff = max(r.suff, r.sum + l.suff);
    res.ans = max(max(l.ans, r.ans), l.suff + r.pref);
    return res;
}

void build(struct data tree[], int ar[], int node, int start, int end) {
    if (start == end) {
        tree[node] = make_data(ar[start]);
    }
    else {
        int mid = start + (end - start) / 2;
        build(tree, ar, 2 * node + 1, start, mid);
        build(tree, ar, 2 * node + 2, mid + 1, end);
        tree[node] = combine(tree[2 * node + 1], tree[2 * node + 2]);
    }
}

struct data query(struct data tree[], int node, int start, int end, int left, int right) {
    
    if (start > end || left > end || right < start) {
        return make_data(INT_MIN);
    }

    if (start == left && end == right) {
        return tree[node];
    }

    int mid = start + (end - start) / 2;
    struct data q1 = query(tree, 2 * node + 1, start, mid, left, min(right, mid));
    struct data q2 = query(tree, 2 * node + 2, mid + 1, end, max(mid + 1, left), right);
    return combine(q1, q2);
}

int main() {
    
    int n;
    scanf("%d", &n);

    int ar[n + 1];
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &ar[i]);
    }

    struct data tree[4 * n + 1];

    for (int i = 0; i < 4 * n + 1; i++) {

        tree[i] = make_data(INT_MIN);
    }

    build(tree, ar, 0, 0, n - 1);

    int t;
    scanf("%d", &t);

    while (t--) {

        int left, right;
        scanf("%d %d", &left, &right);

        printf("%d\n", query(tree, 0, 0, n - 1, left - 1, right - 1).ans);
    }
}