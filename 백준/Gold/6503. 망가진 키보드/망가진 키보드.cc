#include <iostream>
#include <string>
using namespace std;

int main() {
    while (true) {
        int m;
        cin >> m;
        if (m == 0) break;
        cin.ignore();

        string str;
        getline(cin, str);

        int count[128] = {0};
        int distinct = 0;
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < str.size(); right++) {
            unsigned char c = str[right];

            if (count[c] == 0) {
                distinct++;
            }
            count[c]++;

            while (distinct > m) {
                unsigned char lc = str[left];
                count[lc]--;
                if (count[lc] == 0) {
                    distinct--;
                }
                left++;
            }

            int len = right - left + 1;
            if (len > maxLen) {
                maxLen = len;
            }
        }

        cout << maxLen << '\n';
    }

    return 0;
}