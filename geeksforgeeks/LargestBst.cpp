#include <bits/stdc++.h>
#include <algorithm>
#include <limits>
using namespace std;

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* newNode(int data) {
    struct Node* node = new Node;
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return(node);
}

void inorder(Node *root) {
    if (root == NULL)
       return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);    
}

// Implemented later
int largestBst(Node *root);

// Driver Program for question
int main() {
    int t;
    scanf("%d", &t);

    while (t--)
    {
        map<int, Node*> m;
        int n;
        scanf("%d",&n);
        struct Node *root = NULL;
        struct Node *child;
        while (n--)
        {
            Node *parent;
            char lr;
            int n1, n2;
            scanf("%d %d %c", &n1, &n2, &lr);
            if (m.find(n1) == m.end())
            {
                parent = newNode(n1);
                m[n1] = parent;
                if (root == NULL)
                    root = parent;
            }
            else
                parent = m[n1];
            child = newNode(n2);
            if (lr == 'L')
                parent->left = child;
            else
                parent->right = child;
            m[n2]  = child;
        } 
        cout << largestBst(root) << endl;
    }
    return 0;
}

/* Determines if a tree is a BST */
bool isBst(Node *node, int min, int max) {
    if (!node) {
        return true;
    }
    if (node->data < min || node->data > max) {
        return false;
    }
    return isBst(node->left, min, node->data) &&
           isBst(node->right, node->data, max);
}


/* Gets the size of a tree */
int getSize(Node *root) {
    if (!root) {
        return 0;
    }
    return getSize(root->left) + getSize(root->right) + 1;
}

/* Determines the largest BST - what the question is asking */
int largestBst(Node *root) {
    if (!root) {
        return 0;
    }
    if (isBst(root, numeric_limits<int>::min(), numeric_limits<int>::max())) {
        return getSize(root);
    }
    return max(largestBst(root->left), largestBst(root->right));
}
