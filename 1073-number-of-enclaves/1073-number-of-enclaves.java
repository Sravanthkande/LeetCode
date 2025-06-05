import java.util.*;

class Solution {
    private int[] delRow = {-1, 0, 1, 0};
    private int[] delCol = {0, 1, 0, -1};

    private boolean isValid(int i, int j, int N, int M){
        if(i < 0 || i >= N) return false;
        if(j < 0 || j >= M) return false;

        return true;
    }

    private void BFS(int[][] grid, Queue<int[]> que, boolean[][] vis){
        int N = grid.length;
        int M = grid[0].length;

        while(!que.isEmpty()){
            int[] cell = que.poll();

            int row = cell[0];
            int col = cell[1];

            for(int i=0;i< 4;i++){
                int nRow = row + delRow[i];
                int nCol = col + delCol[i];

                if(isValid(nRow, nCol, N, M) &&
                   grid[nRow][nCol] == 1 
                   && vis[nRow][nCol] == false){
                    vis[nRow][nCol] = true;
                    que.add(new int[]{nRow, nCol});
                   }
            }
        }
    }
    public int numEnclaves(int[][] grid) {
        int N = grid.length;
        int M = grid[0].length;

        Queue<int[]> que = new LinkedList<>();

        boolean[][] vis = new boolean[N][M];

        for(int i=0;i < N; i++){
            for(int j=0; j< M; j++){

                if((i==0 || i == N -1 ||
                    j==0 || j == M -1) &&
                    grid[i][j] == 1){
                        vis[i][j] = true;
                        que.add(new int[]{i, j});
                    }
            }
        }
        BFS(grid, que, vis);

        int count = 0;

        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(grid[i][j] == 1 && vis[i][j] == false){
                    count++;
                }
            }
        }
        return count;
    }
}