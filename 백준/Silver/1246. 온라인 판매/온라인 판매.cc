#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  int N, M;
  cin >> N >> M;

  int arr[M];

  for(int i = 0; i<M; i++){
    cin >> arr[i];
  }

  sort(arr, arr+M);
  int result;
  int price;
  if(N > M){
    result = arr[0]*M;
    price = arr[0];
    for(int i = 1; i<M; i++){
      if(result < arr[i]*(M-i)){
        price = arr[i];
        result = arr[i]*(M-i);
      }
    }
  } else {
    price = arr[M-N];
    result = price*N;
    for(int i = M-N; i<M; i++){
      if(result < arr[i]*(M-i)){
        price = arr[i];
        result = price*(M-i);
      }
    }
  }

  cout << price << " " <<result;
  return 0;
}