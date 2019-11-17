#include <bits/stdc++.h>

using namespace std;

typedef struct mpair {

    int di;
    int ti;
    int si;

    mpair() : di(NULL), ti(NULL), si(NULL) {}
    
}mpair;

bool cmp(mpair &p, mpair &q) {
    return p.di < q.di;
}

void min_sadness(vector<mpair> dts, int d) {
    
    priority_queue<pair<int, int>> PQ;

    sort(dts.begin(), dts.end(), cmp);

    int i = 0;

    for (; i < dts.size(); i++) {

        mpair mp = dts[i];

        if (PQ.empty()) {
            mp.ti -= 1;
            PQ.push(make_pair(mp.si, mp.ti));
            continue;
        }

        if (mp.si >= PQ.top().first) {
            mp.ti -= 1;
            if (mp.ti > 0) {
                PQ.push(make_pair(mp.si, mp.ti));
            }
        }
        else{
            pair<int, int> top = PQ.top();
            PQ.pop();
            top.second -= 1;
            if (top.second > 0) {
                PQ.push(top);
            }
            PQ.push(make_pair(mp.si, mp.ti));
        }
    }

    pair<int, int> top;

    while (i < d && !PQ.empty())
    {
        top = PQ.top();
        PQ.pop();

        while (i < d && top.second > 0)
        {
            top.second--;
            i++;
        }
    }

    unsigned long long int sum = top.first * top.second;
    while (!PQ.empty()) {

        top = PQ.top();
        sum += top.first * top.second;
        PQ.pop();
    }

    cout << sum << endl;
}

int
main()
{
    int t;
    cin >> t;
    while (t--) {

        int n, d;
        cin >> n >> d;
        vector<mpair> dts;

        for (int i = 0; i < n; i++) {
            
            mpair mp;
            cin >> mp.di >> mp.ti >> mp.si;
            dts.push_back(mp);
        }

        min_sadness(dts, d);
    }
    return 0;
}