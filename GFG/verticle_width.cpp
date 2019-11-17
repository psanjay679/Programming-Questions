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


int verticalWidth(Node* root)
{
    queue<pair<Node *, int>> q;
    q.push(make_pair(root, 0));
    int left = 0, right = 0;

    while (!q.empty())
    {

        pair<Node *, int> top = q.front();
        q.pop();

        if (top.first != NULL) {
            left = min(left, top.second - 1);
            right = max(right, top.second + 1);

            q.push(make_pair(top.first->left, top.second - 1));
            q.push(make_pair(top.first->right, top.second + 1));
        }
    }

    return right - left - 1;
}