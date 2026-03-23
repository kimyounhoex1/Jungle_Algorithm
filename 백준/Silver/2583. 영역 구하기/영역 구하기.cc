#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main() {
    int M, N, K;

    std::cin >> M >> N >> K;

    std::vector<std::vector<bool>> color(M, std::vector<bool>(N, false));
    std::vector<std::vector<bool>> visit(M, std::vector<bool>(N, false));
    for(int i = 0; i<K; i++) {
        std::pair<int, int> start;
        std::pair<int, int> end;
        std::cin >> start.first >> start.second >> end.first >> end.second;

        for(int y = start.second; y < end.second; y++) {
            for(int x = start.first; x < end.first; x++) {
                color[y][x] = true;
            }
        }
    }

    /*
    0 0 0 0 1 1 0 
    0 1 0 0 1 1 0 
    1 1 1 1 0 0 0 
    1 1 1 1 0 0 0 
    0 1 0 0 0 0 0 
    */
    int rec_cnt = 0;
    std::vector<int> result;

    for(int i = 0; i< M; i++) {
        for(int j = 0; j < N; j++) {

            if(!visit[i][j] && color[i][j]==0) {
                std::queue<std::pair<int, int>> que;
                que.push({j, i});
                int pixel = 1;
                rec_cnt++;
                visit[i][j] = true;
                while(!que.empty()) {
                    
                    std::pair<int, int> point = que.front();
                    int x = point.first;
                    int y = point.second;
                    que.pop();

                    for(int i = 0; i< 4; i++) {
                        int nx = x + dx[i];
                        int ny = y + dy[i];

                        if(0 <= nx && nx < N && 0 <= ny && ny < M) {
                            if(!color[ny][nx] && visit[ny][nx] == 0) {
                                que.push({nx, ny});
                                pixel++;
                                visit[ny][nx] = true;
                            }
                        }
                    }
                }
                result.push_back(pixel);
            }
        }   
    }

    std::cout << rec_cnt << std::endl;

    sort(result.begin(), result.end());
    for(int i = 0; i< rec_cnt; i++) {
        std::cout << result.at(i) << " ";
    }

    return 0;
}
/*
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

*/