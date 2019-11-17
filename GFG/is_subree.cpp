#include <bits/stdc++.h>

using namespace std;

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};

bool isIdentical(Node *r1, Node *r2)
{
    if (r1 == NULL && r2 == NULL) {
        return true;
    }
    else if ((r1 != NULL && r2 == NULL) || (r1 == NULL && r2 != NULL)) {
        return false;
    }
    else {
        bool res = r1->data == r2->data;
        res = res & isIdentical(r1->left, r2->left) && isIdentical(r1->right, r2->right);
        return res;
    }
}

bool isSubtree(Node* T1, Node* T2) {

    if (T1 == NULL) {
        return T2 == NULL;
    }

    bool res = isIdentical(T1, T2);
    res = res | isIdentical(T1->left, T2);
    res = res | isIdentical(T1->right, T2);
    return res;
}