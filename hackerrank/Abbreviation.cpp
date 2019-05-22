#include <bits/stdc++.h>

using namespace std;

// Complete the abbreviation function below.
string abbreviation(string a, string b) {
    bool **valid = new bool *[a.length()+1];
    for (int i = 0; i <= a.length(); ++i) {
        valid[i] = new bool[b.length()+1];
    }
    valid[0][0] = true;
    bool containsUpper = false;
    for (int k = 1; k <= a.length(); ++k) {
        if ((a[k-1] >= 'A' && a[k-1] <= 'Z') || containsUpper) {
            containsUpper = true;
            valid[k][0] = false;
        } else {
            valid[k][0] = true;
        }
    }
    for (int k = 1; k <= b.length(); ++k) {
        valid[0][k] = false;
    }

    for (int k = 1; k <= a.length(); ++k) {
        for (int l = 1; l <= b.length(); ++l) {
            if (a[k-1] == b[l-1]) {
                valid[k][l] = valid[k-1][l-1];
            } else if (a[k-1]-32 == b[l-1]) {
                valid[k][l] = valid[k-1][l-1] || valid[k-1][l];
            } else if (a[k-1] >= 'A' && a[k-1] <= 'Z') {
                valid[k][l] = false;
            } else {
                valid[k][l] = valid[k-1][l];
            }
        }
    }
    return valid[a.length()][b.length()] ? "YES" : "NO";
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string a;
        getline(cin, a);
        string b;
        getline(cin, b);
        string result = abbreviation(a, b);
        fout << result << "\n";
    }
    fout.close();
    return 0;
}
