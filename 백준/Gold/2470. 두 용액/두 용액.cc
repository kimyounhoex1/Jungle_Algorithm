#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int plus_value(int number){
  if(number < 0){
    return number * -1;
  }
  return number;
}

int main(){
  int testcase;
  cin >> testcase;

  vector<int> arr;

  for(int i = 0; i<testcase; i++){
    int liquid;
    cin >> liquid;
    arr.push_back(liquid);
  }
  sort(arr.begin(), arr.end());

  int p1 = 0;
  int p2 = testcase-1;

  int real_p1 = p1;
  int real_p2 = p2;
  
  int minValue = 2000000000;
  while(p1 < p2) {
    int targetValue = arr.at(p1) + arr.at(p2);

    // cout << "pointer: " << arr.at(p1) << " " << arr.at(p2) << "\n";
    // cout << "real_pointer: "<< arr.at(real_p1) << " " << arr.at(real_p2) << "\n";
    // cout << targetValue << "\n";
    // cout << "-----------------\n";

    if (plus_value(targetValue) < minValue) {
      minValue = plus_value(targetValue);
      real_p1 = p1;
      real_p2 = p2;
      // cout << "change\n";
    }

    if(targetValue > 0){
      --p2;
    }
    else {
      ++p1;
    }
  }

  cout << arr.at(real_p1) << " " << arr.at(real_p2);
}