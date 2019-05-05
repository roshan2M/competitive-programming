#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

class Trie {
    public:
        Trie **children;
        bool isEndOfWord;

        void insert(string s);
        int find(string s);
        
        Trie(bool isEndOfWord);
        ~Trie();
};

Trie::Trie(bool isEndOfWord) {
    this->isEndOfWord = isEndOfWord;
    this->children = new Trie *[26];
}

Trie::~Trie() {
    for (int i = 0; i < 26; ++i) {
        if (this->children[i]) {
            delete this->children[i];
        }
    }
}

void Trie::insert(string s) {
    if (s.length() == 0) {
        return;
    }
    int index = tolower(s[0]) - 'a';
    if (!children[index]) {
        bool isEndOfWord = false;
        if (s.length() == 1) {
            isEndOfWord = true;
        }
        this->children[index] = new Trie(isEndOfWord);
    }
    this->children[index]->insert(s.substr(1));
}

int Trie::find(string s) {
    if (s.length() == 0) {
        return this->isEndOfWord ? 1 : 0;
    }
    int index = tolower(s[0]) - 'a';
    if (!this->children[index]) {
        return 0;
    }
    return this->children[index]->find(s.substr(1));
}

int main() {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; ++i) {
        Trie trie = new Trie(false);
        int words;
        cin >> words;
        for (int j = 0; j < words; ++j) {
            string s;
            cin >> s;
            trie.insert(s);
        }
        
        string wordToFind;
        cin >> wordToFind;
        
        int isInTrie = trie.find(wordToFind);
        cout << isInTrie << endl;
    }
    return 0;
}
