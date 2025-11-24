#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int N, M;
vector<int> sol;
vector<int> arr;
vector<bool> visited;

void solution(int k) {
  if(k == M) {
    for(int i = 0; i<M; i++) {
      cout << sol[i] << " ";
    }
    cout << "\n";
    return;
  }

  for(int i = 0; i<N; i++) {
    if(!visited[i]) {
      sol[k] = arr[i];
      visited[i] = true;
      solution(k+1);
      visited[i] = false;
    }
  }
}

int main() {
  cin >> N >> M;
  sol.resize(M);
  arr.resize(N);
  visited.resize(N);

  for(int i = 0; i<N; i++) {
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end());

  solution(0);
}