#include <iostream>

using namespace std;

int comp(string str1, string str2) {
    int size = str1.length();
    if(str1.length() > str2.length()) {
        size = str2.length();
    }

    for(int i = 0; i<size; i++) {
        if(str1.at(i) > str2.at(i)) {
            return true;
        }
        if(str1.at(i) < str2.at(i)) {
            return false;
        }
    }

    if(str1.length() < str2.length()) {
        return false;
    }
    return true;
    
}

int main() {
    int number;
    cin >> number;

    string* str = new string[number];
    for(int i = 0; i < number; i++) {
        cin >> str[i];
    }

    bool result = comp(str[0], str[1]);

    for(int i = 1; i< number-1; i++) {
        if(result != comp(str[i], str[i+1])) {
            cout << "NEITHER" << endl;
            return 0;
        }

    }

    if(result) {
        cout << "DECREASING" << endl;
    } else {
        cout << "INCREASING" << endl;
    }

    return 0;
}