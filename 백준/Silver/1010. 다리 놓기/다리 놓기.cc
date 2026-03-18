#include <stdio.h>

// N <= M

long long combination(int n, int r) {
    if (r > n - r) {
        r = n - r;
    }
    long long result = 1;
    for (int i = 0; i < r; i++) {
        result = result * (n - i) / (i + 1);
    }
    return result;
}

int main() {
    int testcase;
    scanf("%d", &testcase);
    for(int i = 0; i< testcase; i++) {
        int N, M;
        scanf("%d %d", &N, &M);
        long long result = combination(M, N);
        printf("%lld\n", result);
    }
}

// n! / r!(n-r)!