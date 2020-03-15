#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>


using namespace std;

string is_birbal_smart(vector<vector<int> > adj, vector<int> S) {
    
    queue<int> Q;
    vector<bool> visited(adj.size(), false);
    vector<bool> protect(adj.size(), false);
    
    for (int i = 1; i < adj.size(); i++) {
        if (S[i] >= 0) {
            
            if (S[i] > 0) {
                Q.push(i);
            }
            
            protect[i] = true;
        } 
    }
    
    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();
        
        if (visited[u]) {
            continue;
        }
        
        for (int i = 0; i < adj[u].size(); i++) {
            int v = adj[u][i];
            int s_val = max(S[u] - 1, S[v]);
            if (s_val >= 0) {
                if (s_val > 0){
                    Q.push(v);
                }
                
                protect[v] = true;
                
            } 
        }
        
        visited[u] = true;
    }
    
    for (int i = 1; i < protect.size(); i++) {
        if (!protect[i]) {
            return "No";
        }
    }
    
    return "Yes";
    
}

int main() {
    
    int T;
    cin >> T;
    while (T--) {
        
        int N, R, M, a, b;
        cin >> N >> R >> M;
        
        vector<vector<int> > adj(N + 1, vector<int>());
        
        for (int i = 0; i < R; i++) {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        
        vector<int> S(N + 1, -1);
        int k, s;
        for (int i = 0; i < M; i++) {
            cin >> k >> s;
            S[k] = s;
        }
        
        cout << is_birbal_smart(adj, S) << endl;        
    }
    
    return 0;
}
