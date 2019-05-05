#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* right;
    Node* left;
    
    Node(int x){
        data = x;
    }
};

Node *insert(Node *root,int data)
{
    if(root==NULL)
    root=new Node(data);
    else if(data<root->data)
    root->left=insert(root->left,data);
    else
    root->right=insert(root->right,data);
    return root;
}

//Position this line where user code will be pasted.
int main() {
    int testcases;
    cin>>testcases;
    while(testcases--)
    {
        Node *root=NULL;
        int sizeOfArray;
        cin>>sizeOfArray;
        int arr[sizeOfArray];
        
        for(int i=0;i<sizeOfArray;i++)
        cin>>arr[i];
        
        for(int i=0;i<sizeOfArray;i++)
        {
            root=insert(root,arr[i]);
        }
        int l,h;
        cin>>l>>h;
        cout<<getCountOfNode(root,l,h)<<endl;
    }
	return 0;
}

/*
The structure of a BST node is as follows:
struct Node
{
    int data;
    Node *left;
    Node *right;
};
*/
int getCountOfNode(Node *root, int l, int h) {
    int c = 0;
    if (!root) {
        return c;
    }
    if (root->data >= l && root->data <= h) {
        ++c;
    }
    if (root->data >= l) {
        c += getCountOfNode(root->left, l, h);
    }
    if (root->data <= h) {
        c += getCountOfNode(root->right, l, h);
    }
    return c;
}
