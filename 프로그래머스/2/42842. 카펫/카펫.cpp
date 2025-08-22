#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    for(int i = 3; i<brown/2; i++){
        answer.clear();
        int a = i;
        int b = (brown - (a-2)*2)/2;
        
        if((a-2) * (b-2) == yellow){
            answer.push_back(b);
            answer.push_back(a);
            break;
        }
    }
    
    return answer;
}