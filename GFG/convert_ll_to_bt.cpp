#include <bits/stdc++.h>

using namespace std;

struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};
struct TreeNode {
    int data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) {
        data = x;
        left = NULL;
        right = NULL;
    }
};

void convert(Node *head, TreeNode *&root) {
    
    if (head == NULL) {
        root = NULL;
    }
    else {
        Node *curr = head;
        struct TreeNode *new_node = new TreeNode(curr->data);
        root = new_node;
        queue<TreeNode *> q;
        q.push(root);
        curr = curr->next;
        while (curr != NULL)
        {
            TreeNode *tree = q.front();
            q.pop();
            new_node = new TreeNode(curr->data);
            q.push(new_node);
            tree->left = new_node;
            curr = curr->next;
            if (curr)
            {
                new_node = new TreeNode(curr->data);
                tree->right = new_node;
                q.push(new_node);
                curr = curr->next;
            }
        }
    }
}