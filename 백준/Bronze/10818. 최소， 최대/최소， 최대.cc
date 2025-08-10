#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  
  int testcase;
  cin >> testcase;
  vector<int> arr(testcase);
  for(int i = 0; i<testcase; i++){
    cin >> arr[i];
  }

  int min_val = *min_element(arr.begin(), arr.end());
  int max_val = *max_element(arr.begin(), arr.end());

  cout << min_val << " " << max_val;
}