class Solution {
    public int numIslands(char[][] grid) {
        int islandNum = 0;
        boolean[][] isVisited = new boolean[grid.length][grid[0].length];
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == '1' && !isVisited[i][j]) {
                    islandNum += 1;
                    dfs(grid, i, j, isVisited);
                }
            }
        }
        
        return islandNum;
    }
    
    public void dfs(char[][] grid, int row, int col, boolean[][]isVisited) {
        if(row < 0 || row > grid.length - 1 || col < 0 || col > grid[0].length - 1 || grid[row][col] == '0' || isVisited[row][col] == true) {return;}
        
        grid[row][col] = '0';
        isVisited[row][col] = true;
        dfs(grid, row, col + 1, isVisited);
        dfs(grid, row + 1, col, isVisited);
        dfs(grid, row, col - 1, isVisited);
        dfs(grid, row - 1, col, isVisited);
    }
}

