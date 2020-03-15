#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int countPalindrome(vector<vector<int> > mat, int r, int c, int N, int M)
{
    int cnt = 1;
    int d = 1;
    while (r - d >= 0 && r + d < N && c - d >= 0 && c + d < M)
    {
        if (mat[r-d][c] == mat[r + d][c] && mat[r][c - d] == mat[r][c + d])
        {
            cnt++;
            d++;
        }
        else
        {
            break;
        }
    }
    return cnt;
}

int main() {
    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        cin >> N >> M;
        //vector<vector<int> > mat(N, vector<int>(M, NULL));
        int mat[N][M];
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                cin >> mat[i][j];
            }
        }
        int ans = 0;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                int d = 1;
                int cnt = 1;
                while (i - d >= 0 && i + d < N && j - d >= 0 && j + d < M) {
                    if (mat[i - d][j] == mat[i + d][j] && mat[i][j - d] == mat[i][j + d]) 
                    {
                        cnt++;
                        d++;
                    }
                    else
                    {
                        break;
                    }
                }
                ans += cnt;
            }
        }
        cout << ans << endl;               
    }
    return 0;
}
