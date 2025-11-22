#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> arr;

void solution(int k) {
  if(k == M) {
    for(int i = 0; i<M; i++) {
      cout << arr[i] << " ";
    }
    cout << "\n";
    return;
  }

  for(int i = 1; i <= N; i++) {
    arr[k] = i;
    solution(k+1);
  }
}

int main() {
  cin >> N >> M;
  arr.resize(N);
  
  solution(0);
}