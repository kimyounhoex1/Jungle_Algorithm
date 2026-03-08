#include <iostream>
#include <deque>

using namespace std;

int findPosition(deque<int> arr, int target) {
    for(int i = 0; i < arr.size(); i++) {
        if(arr.at(i) == target) { 
            return i;
        }
    }
    return -1;
}

void print(deque<int> arr) {
    for(int i = 0; i< arr.size(); i++) {
        std::cout << arr.at(i) << ", ";
    }
    cout << endl;
}

int main() {
    deque<int> arr;
    
    int N, M;

    cin >> N;
    cin >> M;

    for(int i = 0; i < N; i++) {
        arr.push_back(i+1);
    }

    int values[N];

    for(int i = 0; i <M; i++) {
        cin >> values[i];
    }
    int count = 0;

    for(int i = 0; i < M; i++) {
        int pos = findPosition(arr, values[i]);
        if(arr.size() / 2 < pos) {
            while(arr.at(0) != values[i]){
                // print(arr);
                count++;
                int data = arr.at(arr.size() - 1);
                arr.pop_back();
                arr.push_front(data);
            }
        } else {
            while(arr.at(0) != values[i]){
                // print(arr);
                count++;
                int data = arr.at(0);
                arr.pop_front();
                arr.push_back(data);
            }
        }
        arr.pop_front();
    }
    cout << count << endl;
    return 0;
}
