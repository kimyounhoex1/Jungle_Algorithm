#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
  vector<int> arr;
  vector<int> stk;
  int input;
  cin >> input;

  for (int i = 0; i < input; i++)
  {
    int number;
    cin >> number;

    arr.push_back(number);
  }

  int max, max_temp = *max_element(arr.begin(), arr.end());
  int max_idx = max_element(arr.begin(), arr.end()) - arr.begin();

  // cout << "max value: " << max << " max_idx: " << max_idx << "\n";

  int count = 1; // 꼭 1부터 시작해야 함

  vector<char> result;
  for (int i = 0; i < input; i++)
  {
    int target = arr[i];

    // target이 될 때까지 push
    while (count <= target)
    {
      stk.push_back(count++);
      result.push_back('+');
    }

    // top이 target이면 pop
    if (!stk.empty() && stk.back() == target)
    {
      stk.pop_back();
      result.push_back('-');
    } else {
      cout << "NO";
      return 0;
    }
  }

  for(char c : result){
    cout << c << "\n";
  }
  return 0;
}