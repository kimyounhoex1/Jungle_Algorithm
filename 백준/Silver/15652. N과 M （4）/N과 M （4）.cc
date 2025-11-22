#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> arr;

void solution(int k, int start) {
  if(k == M) {
    for(int i = 0; i<M; i++) {
      cout << arr[i] << " ";
    }
    cout << "\n";
    return;
  }

  for(int i = start; i<=N; i++) {
    arr[k] = i;
    solution(k+1, i);
  }
}

int main() {
  cin >> N >> M;
  arr.resize(M);

  solution(0, 1);
}