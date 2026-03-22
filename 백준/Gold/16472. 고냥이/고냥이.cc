#include <iostream>
#include <string.h>
#include <vector>


int main() {
    int N;
    std::cin >> N;
    std::cin.ignore();
    std::string str;
    std::getline(std::cin, str);

    int left = 0;
    int count[256] = {0};
    int maxLen = 0;
    int distinct = 0;

    for(int right=0; right < str.size(); right++) {
        char rightch = str[right];
        if(count[rightch] == 0) {
            distinct++;
        }
        count[rightch]++;

        while(distinct > N) {
            char leftch = str[left];
            count[leftch]--;
            if(count[leftch] == 0) {
                distinct--;
            }
            left++;
        }
        if(maxLen < right - left+1) {
            maxLen = right-left+1;
        }
    }

    std::cout << maxLen << std::endl;

    return 0;

}