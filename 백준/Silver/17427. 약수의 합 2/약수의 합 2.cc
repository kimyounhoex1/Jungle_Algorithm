#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
  
  long long result = 0;
  int input;
  cin >> input;

  for(int i = 1; i<= input; i++){
    result += i * (input / i);
  }

  cout << result;
}