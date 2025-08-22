#include <string>
#include <sstream>
#include <vector>

using namespace std;

// vector<string> abstractSentence(string s){
//     vector<string> result;
//     stringstream ss(s);
//     string word;
    
//     while(ss >> word) {
//         result.push_back(word);
//     }
    
//     return result;
// }

string solution(string s) {
    bool newWord = true;
    
    for(int i = 0; i<s.size(); i++){
        char charAt = s.at(i);
        if(charAt == ' '){
            newWord = true;
        } else {
            if(newWord && (charAt >= 'a' && charAt <= 'z')){
                s.at(i) = s.at(i) - ('a' - 'A');
            }
            else if (!newWord && (charAt >='A' && charAt <= 'Z')){
                s.at(i) = s.at(i) + ('a' - 'A');
            }
            newWord = false;
        }
    }
    
    return s;
}