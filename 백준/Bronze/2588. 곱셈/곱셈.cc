#include <iostream>
#include <cmath>

using namespace std;
int size(int number){
  int size = 1;
  while(number/10){
    size++;
    number = number/10;
  }
  return size;
}

int main(){
  int num1, num2;
  // if(num1 == 0 || num2 == 0){
  //   cout << "0";
  //   return 0;
  // }
  cin >> num1 >> num2;
  int num2_size = size(num2);
  int total = 0;
  // cout << "num2_size = " << num2_size << '\n';
  for(int i = 0; i < num2_size; i++){
    
    int remain = num2%10;
    num2 = num2/10;
    int temp = num1 * remain;
    cout << temp << '\n';
    total += temp*pow(10, i);
    // cout << "total = " << total << '\n';
  }

  cout << total;
}