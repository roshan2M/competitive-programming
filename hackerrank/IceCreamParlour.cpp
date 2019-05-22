#include <bits/stdc++.h>
#include <map>

using namespace std;

// Complete the whatFlavors function below.
void whatFlavors(vector<int> costs, int money) {
    map<int, int> costMap;
    for (int i = 0; i < costs.size(); ++i) {
        int cost = costs[i];
        auto it = costMap.find(money - cost);
        if (it != costMap.end()) {
          cout << (*it).second + 1 << " " << i + 1 << endl;
          return;
        }
        costMap[cost] = i;
    }
}
