#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int N, M;
vector<int> arr;
vector<int> inputArr;
vector<bool> visited;

void solution(int k, int start) {
  if(k == M) {
    for(int i = 0; i<M; i++) {
      cout << arr[i] << " ";
    }
    cout << "\n";
    return;
  }

  for(int i = 0; i<N; i++) {
    if(!visited[i]) {
      arr[k] = inputArr[i];
      visited[i] = true;
      solution(k+1, i+1);
      visited[i] = false;
    }
  }
}

int main() {
  cin >> N >> M;
  inputArr.resize(N);
  for(int i = 0; i<N; i++) {
    cin >> inputArr[i];
  }
  sort(inputArr.begin(), inputArr.end());

  arr.resize(M);
  visited.resize(M);

  solution(0, 1);
}