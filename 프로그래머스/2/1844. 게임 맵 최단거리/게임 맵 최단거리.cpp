#include<vector>
#include <queue>
using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    
    int n = maps.size();
    int m = maps.at(0).size();
    
    vector<vector<bool> > visited(n, vector<bool>(m, false));
    
    queue<pair<int, int> > q;
    q.push({0, 0});
    visited[0][0] = true;
    
    while(!q.empty()){
        auto [x, y] = q.front();
        q.pop();
        
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx >= 0 && ny >= 0 && nx < n && ny < m){
                if(maps[nx][ny] == 1 && !visited[nx][ny]){
                    visited[nx][ny] = true;
                    maps[nx][ny] = maps[x][y] + 1;
                    q.push({nx, ny});
                }
            }
        }
    }
    if(visited[n-1][m-1]){
        answer = maps[n-1][m-1];
    }
    
    return answer;
}

// int dfs(vector<vector<int> > maps, int a, int b){
//     if(a == maps.size() - 1 && b == maps.at(0).size() -1 ){
//         return 1;
//     }
        
//     if(maps.at(a+1).at(b) == 1){
//         return 1 + dfs(maps, a+1, b);
//     } else if(maps.at(a).at(b+1) == 1) {
//         return 1 + dfs(maps, a, b+1);
//     }
// }