class Solution {
    int maxArea = 0;
    int areaCount = 0;
    
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length;
        int columns = grid[0].length;
        boolean [][]isVisited = new boolean [rows][columns];
        int numOfIslands = 0;

        for (int i = 0; i < rows; i++) {
            for(int j = 0; j < columns; j++) {
                if (grid[i][j] == 1 && !isVisited[i][j]) {
                    numOfIslands += 1;
                    areaCount = 0;
                    dfs(grid,i, j, isVisited);
                    maxArea = Math.max(areaCount, maxArea);

                }
            }
        }
        return maxArea;
    }
    
    public void dfs(int[][] grid,int row, int column, boolean [][] isVisited) {
        if (row < 0 || row > grid.length-1 || column < 0 || column > grid[0].length-1 || grid[row][column] == 0 || 
            isVisited[row][column] == true ) 
            { 
                return; 
            }
        
        grid[row][column] = 0;
        isVisited[row][column] = true;
        areaCount+=1;
        dfs(grid, row, column+1, isVisited);
        dfs(grid, row+1, column, isVisited);
        dfs(grid, row, column-1, isVisited);
        dfs(grid, row-1, column, isVisited);
        
    }
}
