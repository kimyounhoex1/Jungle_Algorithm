#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int dfs(vector<int> numbers, int target, int idx, int curr) {
    if(idx == numbers.size())
        if(target == curr){
            // cout << "upup";
            return 1;
        } else {
            return 0;
        }
    // cout << "idx = " << idx << " || curr = " << curr << "\n";
    int plus = dfs(numbers, target, idx+1, curr + numbers[idx]);
    int minus = dfs(numbers, target, idx+1, curr - numbers[idx]);
    
    return plus + minus;
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers, target, 0, 0);
}