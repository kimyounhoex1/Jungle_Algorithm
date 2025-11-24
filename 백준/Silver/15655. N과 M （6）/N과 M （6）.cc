#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int N, M;
vector<int> sol;
vector<int> arr;
vector<int> visited;

void solution(int k, int start) {
  if(k == M) {
    for(int i = 0; i<M; i++) {
      cout << sol[i] << " ";
    }
    cout << "\n";
    return;
  }

  for(int i = start; i< N; i++) {
    if(!visited[i]){
      sol[k] = arr[i];
      visited[i] = true;
      solution(k+1, i);
      visited[i] = false;
    }
  }
}

int main() {
  cin >> N >> M;
  arr.resize(N);
  for(int i = 0; i<N; i++) {
    cin >> arr[i];
  }
  visited.resize(N);
  sol.resize(M);

  sort(arr.begin(), arr.end());
  
  solution(0, 0);
}