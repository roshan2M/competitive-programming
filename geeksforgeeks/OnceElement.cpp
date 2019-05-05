#include <iostream>
using namespace std;

class Node {
    public:
        int data;
        bool duplicate;
        Node *left;
        Node *right;
        
        Node(int data);
        void insert(int data);
        int findSingle();
};

Node::Node(int data) {
    this->data = data;
    this->duplicate = false;
}

void Node::insert(int data) {
    Node *current = this;
    while (true) {
        if (data == current->data) {
            current->duplicate = true;
            return;
        }
        if (data < current->data) {
            if (!current->left) {
                current->left = new Node(data);
                return;
            }
            current = current->left;
        } else {
            if (!current->right) {
                current->right = new Node(data);
                return;
            }
            current = current->right;
        }
    }
}

int Node::findSingle() {
    if (!this->duplicate) {
        return this->data;
    }
    int result = -1;
    if (this->left) {
        result = this->left->findSingle();
    }
    if (result == -1 && this->right) {
        result = this->right->findSingle();
    }
    return result;
}

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        int data;
        cin >> data;
        Node *node = new Node(data);
        --n;
        
        while (n--) {
            cin >> data;
            node->insert(data);
        }
        int single = node->findSingle();
        cout << single << endl;
    }
}
