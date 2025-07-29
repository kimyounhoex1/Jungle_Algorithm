#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int diff_add(int a, int b) {
    return abs(a - b);
}

int calc(const vector<int>& arr) {
    int sum = 0;
    for (int i = 0; i < arr.size() - 1; i++) {
        sum += diff_add(arr[i], arr[i + 1]);
    }
    return sum;
}

int dfs(int depth, vector<int>& now_matrix, const vector<int>& matrix, vector<bool>& visited) {
    if (depth == now_matrix.size()) {
        return calc(now_matrix);
    }

    int maxVal = INT32_MIN;
    for (int i = 0; i < matrix.size(); i++) {
        if (!visited[i]) {
            visited[i] = true;
            now_matrix[depth] = matrix[i];
            maxVal = max(maxVal, dfs(depth + 1, now_matrix, matrix, visited));
            visited[i] = false;
        }
    }

    return maxVal;
}

int main() {
    int testcase;
    cin >> testcase;

    vector<int> matrix(testcase);
    vector<int> now_matrix(testcase);
    vector<bool> visited(testcase, false);

    for (int i = 0; i < testcase; i++) {
        cin >> matrix[i];
    }

    int result = dfs(0, now_matrix, matrix, visited);
    cout << result << endl;

    return 0;
}