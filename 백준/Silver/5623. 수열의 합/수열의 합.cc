#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int testcase;
  cin >> testcase;

  vector<vector<int> > v = vector<vector<int> >(testcase);

  for(int i = 0; i<testcase; i++){
    for(int j = 0; j<testcase; j++){
    int number;
    cin >> number;
    v.at(i).push_back(number);
    }
  }
  vector<int> diff;

  if(testcase == 2){
    int number = (v.at(0).at(1)) / 2;
    diff.push_back(number);
    diff.push_back(number);

    for(auto it = diff.begin(); it != diff.end(); it++){
     cout << *it << " ";
    }
    return 0;
  }

  int first_value = (v.at(0).at(1) + v.at(0).at(2) - v.at(1).at(2))/2;
  diff.push_back(first_value);

  for(int i = 1; i<testcase; i++){
    diff.push_back(v.at(0).at(i) - diff.at(0));
  }
  for(auto it = diff.begin(); it != diff.end(); it++){
    cout << *it << " ";
  }  

  return 0;
}