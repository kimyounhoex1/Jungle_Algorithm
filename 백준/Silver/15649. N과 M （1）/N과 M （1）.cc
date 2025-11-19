#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<int> arr;
vector<bool> visited;

void func(int k) {
  if(k == m) {
    for(int i = 0; i< m; i++){
      cout << arr[i] << " ";
    }
    cout << "\n";
    return;
  }

  for(int i = 1; i<=n; i++) {
    if(!visited[i-1]) {
      arr[k] = i;
      visited[i-1] = true;
      func(k+1);
      visited[i-1] = false;
    }
  }
}

int main() {
  cin >> n >> m;

  arr.resize(n);
  visited.resize(n);

  func(0);
}