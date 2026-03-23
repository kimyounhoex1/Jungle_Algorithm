#include <iostream>
#include <queue>
#include <tuple>

int count = 0;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main() {
    int n, m;

    std::cin >> n >> m;
    std::vector<std::vector<int>> array(n, std::vector<int>(m));
    bool isVisit[n][m];
    for(int i = 0; i< n; i++) {
        for(int j = 0; j < m; j++) {
            std::cin >> array[i][j];
            isVisit[i][j] = false;
        }
    }
    int maxArea = 0;
    int result_count = 0;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(!isVisit[i][j] && array[i][j]) {
                std::queue<std::pair<int, int>> queue;
                queue.push({i, j});
                isVisit[i][j] = true;
                int pixel = 1;
                result_count++;
                while(!queue.empty()) {
                    std::pair<int, int> target = queue.front();
                    int x = queue.front().second;
                    int y = queue.front().first;
                    queue.pop();
                    for(int k = 0; k<4; k++) {
                        int ddx = x + dx[k];
                        int ddy = y + dy[k];
                        if((0 > ddx || ddx >= m) || (0 > ddy || ddy >= n)) {
                            continue;
                        }
                        if(!isVisit[ddy][ddx] && array[ddy][ddx]==1){
                            isVisit[ddy][ddx] = true;
                            queue.push({ddy, ddx});
                            pixel++;
                        }
                    }
                }
                if(pixel > maxArea) { 
                    maxArea = pixel;
                }
            }
        }
    }

    std::cout << result_count << std::endl;
    std::cout << maxArea << std::endl;
    
    return 0;
}