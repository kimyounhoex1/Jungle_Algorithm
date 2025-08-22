#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B)
{
    sort(A.begin(), A.end());
    sort(B.rbegin(), B.rend());
    
    int result = 0;
    
    while(!A.empty()){
        result += A.back() * B.back();
        A.pop_back();
        B.pop_back();
    }
    
    return result;
}