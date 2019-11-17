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

int height(Node* node)
{
    if (node == NULL) {
        return 0;
    }

    int left = height(node->left);
    int right = height(node->right);
    int height = max(left, right) + 1;
    return height;
}

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

int isSumProperty(Node *node)
{
    if (node == NULL || node->left == NULL && node->right == NULL) {
        return true;
    }

    int sum = 0;

    if (node->left) {
        sum += node->left->data;
    }
    if (node->right) {
        sum += node->right->data;
    }

    int res = (sum == node->data);

    res = res & isSumProperty(node->left) & isSumProperty(node->right);
    return res;
}

void levelOrder(Node* node)
{
    queue<Node *> q;
    q.push(node);

    while (!q.empty())
    {
        Node *front = q.front();
        q.pop();
        if (front != NULL)
        {
            cout << front->data;
            q.push(front->left);
            q.push(front->right);
        }
    }
}


void printSpiral(Node *root)
{
    queue<pair<Node *, bool> > q;
    q.push(make_pair(root, false));

    while (!q.empty()) {

        pair<Node *, bool> top = q.front();
        q.pop();

        if (top.first != NULL) {

            cout << top.first->data << " ";

            if (top.second) {
                q.push(make_pair(top.first->right, false));
                q.push(make_pair(top.first->left, false));
            }
            else {
                q.push(make_pair(top.first->left, true));
                q.push(make_pair(top.first->right, true));
            }
        }
    }
}

int getMaxWidth(Node* root)
{
    queue<Node *> q;
    q.push(root);
    q.push(NULL);

    int max_width = 0;
    int cur_width = 0;

    while (!q.empty()) {
        
        Node *top = q.front();
        q.pop();
        if (top != NULL)
        {
            cur_width = 1;
            while (top != NULL)
            {
                cur_width++;
                q.push(top->left);
                q.push(top->right);
            
                top = q.front();
                q.pop();
            }
            q.push(NULL);
            max_width = max(cur_width, max_width);
        }
    }

    return max_width;
}

int height(Node *root)
{
    if (root == NULL) {
        return 0;
    }

    int lheight = height(root->left);
    int rheight = height(root->right);

    return max(lheight, rheight) + 1;

}

bool isBalanced(Node *root)
{
    if (root == NULL) {
        return true;
    }

    int lheight = height(root->left);
    int rheight = height(root->right);

    int res = abs(lheight - rheight) <= 1;
    res = res & isBalanced(root->left) & isBalanced(root->right);
    return res;
}

void topView(struct Node *root)
{
    queue<pair<Node *, int> > q;
    q.push(make_pair(root, 0));
    unordered_set<int> us;
    vector<pair<int, int>> ans;
    while (!q.empty())
    {
        pair<Node *, int> top = q.front();
        q.pop();

        if (top.first != NULL)
        {
            if (us.find(top.second) == us.end()) {
                us.insert(top.second);
                ans.push_back(make_pair(top.second, top.first->data));
            }

            q.push(make_pair(top.first->left, top.second - 1));
            q.push(make_pair(top.first->right, top.second + 1));
        }
    }

    sort(ans.begin(), ans.end());

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i].second << " ";
    }

}

void bottomView(Node *root)
{
    queue<pair<Node *, int>> q;
    q.push(make_pair(root, 0));
    unordered_map<int, vector<int> > ump;
    pair<Node *, int> top;

    while (!q.empty()) {

        top = q.front();
        q.pop();

        if (top.first != NULL) {
            
            if (ump.find(top.second) == ump.end()) {
                ump.insert({top.second, vector<int>(1, top.first->data)});
            }
            else {
                ump[top.second].push_back(top.first->data);
            }

            q.push(make_pair(top.first->left, top.second - 1));
            q.push(make_pair(top.first->right, top.second + 1));
        }
    }

    vector<pair<int, int>> ans;
    for (auto it = ump.begin(); it != ump.end(); it++) {

        int key = it->first;
        int value = it->second[it->second.size() - 1];

        ans.push_back(make_pair(key, value));
    }

    sort(ans.begin(), ans.end());

    for (auto it = ans.begin(); it != ans.end(); it++) {
        cout << it->second << " ";
    }
    
}

int main() {

    Node *root;
    root->data = 10;
    root->left = new Node(20);
    root->right = new Node(30);
    root->left->left = new Node(40);
    root->left->right = new Node(60);

    printSpiral(root);
    return 0;
}