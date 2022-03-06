#include<vector>

class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        std::vector<float> prev_memo (query_row + 1, float(poured));
        std::vector<float> memo (query_row + 1, float(poured));
        for(int i=1; i < query_row + 1; i++) {
            for(int j=0; j < i+1; j++) {
                memo[j] = 0.0;
                int lf = j - 1;
                int rt = j;
                if(lf >= 0) {
                    float v = (prev_memo[lf] - 1.0) / 2.0;
                    v = v > 0.0 ? v : 0.0;
                    memo[j] += v;
                }
                if(rt < i) {
                    float v = (prev_memo[rt] - 1.0) / 2.0;
                    v = v > 0.0 ? v : 0.0;
                    memo[j] += v;
                }
            }
            prev_memo = memo;
        }
        float ret = memo[query_glass];
        ret = ret < 1.0 ? ret : 1.0;
        return ret;
    }
};
