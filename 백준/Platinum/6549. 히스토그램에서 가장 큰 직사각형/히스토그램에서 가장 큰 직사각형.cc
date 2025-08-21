#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

long long getMaxArea(vector<long long>& arr, int left, int right){
	if(left == right){
		return arr[left];
	}
	
	int mid = (left + right) / 2;

	long long leftArea = getMaxArea(arr, left, mid);
	long long rightArea = getMaxArea(arr, mid+1, right);

	long long lp = mid;
  long long rp = mid + 1;
  long long height = min(arr[lp], arr[rp]);
  long long midArea = height * 2;

	while(left < lp || rp < right){
		if(rp < right && (lp == left || arr[lp - 1] < arr[rp + 1])){
			rp ++;
			height = min(height, arr[rp]);
		} else {
				lp --;
				height = min(height, arr[lp]);
		}			
		midArea = max(midArea, (long long)(height * (rp - lp + 1)));
	}
	return max(max(leftArea, midArea), rightArea);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	while(true) {
		long long number;
		cin >> number;
		if(number == 0){
			return 0;
		}

		vector<long long> arr;
		for(int i = 0; i<number; i++){
			int input;
			cin >> input;
			arr.push_back(input);
		}

		cout << getMaxArea(arr, 0, number-1) << "\n";
	}
	return 0;
}