#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

int manhattan_distance(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

void next_move(int posr, int posc, vector <string> board) {
    int r, c, min_dist = numeric_limits<int>::max();
    for (int i = 0; i < board.size(); ++i) {
        int length = board[i].length();
        for (int j = 0; j < length; ++j) {
            if (board[i][j] == 'd') {
                int new_dist = manhattan_distance(posr, posc, i, j);
                if (new_dist < min_dist) {
                    min_dist = new_dist;
                    r = i; c = j;
                }
            }
        }
    }
    if (min_dist == 0) {
        cout << "CLEAN" << endl;
    } else if (abs(posr - r) > abs(posc - c)) {
        if (posr > r) {
            cout << "DOWN" << endl;
        } else {
            cout << "UP" << endl;
        }
    } else {
        if (posc > c) {
            cout << "LEFT" << endl;
        } else {
            cout << "RIGHT" << endl;
        }
    }
}

int main(void) {
    int pos[2];
    vector<string> board;
    cin >> pos[0] >> pos[1];
    for(int i = 0; i < 5; i++) {
        string s; cin >> s;
        board.push_back(s);
    }
    next_move(pos[0], pos[1], board);
    return 0;
}
