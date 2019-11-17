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

int max_height(Node* node, int &max_diam) 
{
   if (node == NULL)
      return 0;

   int left_ht = 1 + max_height(node->left, max_diam);
   int right_ht = 1 + max_height(node->right, max_diam);
   
   max_diam = max(left_ht + right_ht + 1, max_diam);
   return max(left_ht, right_ht);
}

int diameter(Node* node)
{

   if (node == NULL) {
      return 0;
   }

   int max_diam = 0;
   max_height(node, max_diam);

   return max_diam;
}
