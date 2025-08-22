#include <string>
#include <vector>
#include <bitset>

using namespace std;

int countOne(int n){
    int count = 0;
    bitset<32> number(n);
    string str = number.to_string();
    for(int i = 0; i<str.size(); i++){
        if(str.at(i) == '1'){
            count++;
        }
    }
    
    return count;
}

bool isSameOne(int numA, int numB){
    if(countOne(numA) == countOne(numB)){
        return true;
    }
    return false;
}

int solution(int n) {
    int answer = n+1;
    
    while(true){
        if(isSameOne(answer, n)){
            return answer;
        }
        answer++;
    }
}