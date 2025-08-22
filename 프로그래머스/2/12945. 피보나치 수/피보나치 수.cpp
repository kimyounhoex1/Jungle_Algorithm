#include <string>
#include <vector>

using namespace std;

vector<int> fiboArr;

void initFiboArr(int n){
    fiboArr.resize(n+1,-1);
    fiboArr[0] = 0;
    fiboArr[1] = 1;
}

int fibo(int n) {
    if(fiboArr[n] != -1)
        return fiboArr[n];
    fiboArr[n] = (fibo(n-1) + fibo(n-2)) %1234567;
    return fiboArr[n];
    
}

int solution(int n) {
    initFiboArr(n);
    return fibo(n);
}