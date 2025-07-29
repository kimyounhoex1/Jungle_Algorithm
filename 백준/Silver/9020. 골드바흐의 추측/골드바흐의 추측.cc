#include <iostream>

using namespace std;

int prime_num[] = {
  2, 3, 5, 7, 11, 
  13, 17, 19, 23, 
  29, 31, 37, 41, 
  43, 47, 53, 59, 
  61, 67, 71, 73, 
  79, 83, 89, 97};

bool isPrime(int number){
  for(int i = 0; i<25; i++){
    if (number == prime_num[i]) continue;
    if(number%prime_num[i] == 0){
      return false;
    }
  }
  return true;
}

void goldbar(int number){
  int down_num = number/2;
  int up_num = number/2;
  
  while(true){
    while(!isPrime(down_num))
      down_num--;
    while(!isPrime(up_num))
      up_num++;
  
    if((down_num+up_num)>number)
      down_num--;
    else if((down_num+up_num)<number)
      up_num++;
    else
      break;
    // cout << "down_num = " << down_num << "up_num = " << up_num << '\n';
  }
  cout << down_num << " " << up_num << '\n';
}

int main(){
  int testcase;
  cin >> testcase;

  for(int i = 0; i<testcase; i++){
    int number;
    cin >> number;
    goldbar(number);
  }
}