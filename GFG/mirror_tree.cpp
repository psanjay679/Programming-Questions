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


void mirror(Node* node) 
{
    if (node == NULL) {
        return;
    }

    mirror(node->left);
    mirror(node->right);

    Node *left = node->left;
    Node *right = node->right;

    node->left = right;
    node->right = left;
}

