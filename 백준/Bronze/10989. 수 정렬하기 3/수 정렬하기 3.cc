#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
    
  int arr[10001] = {};

  int total;
  cin >> total;

  for(int i = 0; i<total; i++){
    int number;
    cin >> number;
    arr[number]++;
  }

  for(int i = 0; i<10001; i++){
    if(arr[i] > 0){
      for(int j = 0; j<arr[i]; j++){
        cout << i << '\n';
      }
    }
  }
}