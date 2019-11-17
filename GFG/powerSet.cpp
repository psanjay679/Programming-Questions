#include <bits/stdc++.h>

using namespace std;

void gen_set(string s, string curr, int index, vector<string> &ans, unordered_set<char> us)
{

    if (index == s.length()) {
        ans.push_back(curr);
    }
    else {

        gen_set(s, curr, index + 1, ans, us);

        if (us.find(s[index]) == us.end()) {
            us.insert(s[index]);
            gen_set(s, curr + s[index], index + 1, ans, us);
        }
    }
}

vector <string> powerSet(string s)
{
    vector<string> ans;
    unordered_set<char> us;
    ans.clear();
    gen_set(s, "", 0, ans, us);
    sort(ans.begin(), ans.end());
    return ans;
}

int main() {

    string s = "aabc";
    vector<string> ans = powerSet(s);
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << endl;
    }

    return 0;
}