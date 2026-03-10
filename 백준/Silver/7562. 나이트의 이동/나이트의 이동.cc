#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <tuple>

std::pair<int, int> move[8] = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};

int main() {
    int testcase;
    std::cin >> testcase;

    for(int i = 0; i< testcase; i++) {
        int l;
        std::pair<int, int> now_pos;
        std::pair<int, int> target_pos;
        std::cin >> l;
        std::cin >> now_pos.first >> now_pos.second;
        std::cin >> target_pos.first >> target_pos.second;

        std::deque<std::tuple<int, int, int>> que;
        que.push_back({now_pos.first, now_pos.second, 0});

        bool matrix[l][l];
        for(int i = 0; i < l; i++) {
            for(int j = 0; j < l; j++) {
                matrix[i][j] = false;
            }
        }
        matrix[now_pos.first][now_pos.second] = true;
        std::tuple<int, int, int> now;
        int answer;
        
        while(!que.empty()) {
            std::tuple<int, int, int> now = que.front();
            que.pop_front();

            if(std::get<0>(now) == target_pos.first && std::get<1>(now) == target_pos.second) {
                answer = std::get<2>(now);
                break;
            }
            
            for(int i = 0; i<8; i++) {
                int nx = std::get<0>(now) + move[i].first;
                int ny = std::get<1>(now) + move[i].second;
                if(nx >= 0 && nx < l && ny >= 0 && ny < l && !matrix[nx][ny]) {
                    matrix[nx][ny] = true;
                    que.push_back({nx,ny, std::get<2>(now)+1});
                }
            }
        }
        std::cout << answer << std::endl;
    }

    return 0;
}