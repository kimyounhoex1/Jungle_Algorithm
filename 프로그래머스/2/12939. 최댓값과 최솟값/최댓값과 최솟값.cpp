#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <climits> 

using namespace std;

vector<string> splitStr(string &s){
    vector<string> str;
    stringstream ss(s);
    string word;
    
    while(ss >> word) {
        str.push_back(word);
    }
    
    return str;
}
string solution(string s) {
    string answer = "";
    vector<string> words = splitStr(s);
    
    int min = INT_MAX;
    int max = INT_MIN;
    
    while(!words.empty()) {
        int target = stoi(words.back());
        if(min > target){
            min = target;
        }
        if(max < target){
            max = target;
        }
        words.pop_back();
    }
    answer.append(to_string(min)).append(" ").append(to_string(max));
    return answer;
}

