#include<iostream>
#include<string>
#include<vector>
#include<tuple>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        int p = s.length() - 1;
        int count = 0;
        bool cont = true;
        bool striped = false;
        while (p >= 0 and cont) {
            if (s[p] != ' ') {
                p--;
                count++;
                striped = true;
            }
            else if (striped) {
                cont = false;
            }
            else {
                p--;
            }
        }
        return count;
    }
};

typedef std::tuple<std::string, int> answer;

int main() {
		Solution sol;
		std::vector<answer> arr = {
				answer ("Hello World", 5),
				answer ("Hello World  ", 5)};
		int p = 0;
		int n = arr.size();
		for (std::tuple<std::string, int> w: arr) {
				int v1 = sol.lengthOfLastWord(std::get<0>(w));
				int v2 = std::get<1>(w);
				std::cout << v1 << " " << v2 << " " << (v2 == v1) << "\n";
		}
}
