class Solution {
    public int findJudge(int n, int[][] trust) {
        
        if (trust.length < n - 1) {
            return -1;
        }
        
        int [] indegrees = new int [n+1];
        int [] outdegrees = new int [n+1];
        
        for (int[]relations : trust) {
            outdegrees[relations[0]]++;
            indegrees[relations[1]]++;
        }
        
        for (int i = 1; i <= n; i++) {
            if(indegrees[i] == n - 1 && outdegrees[i] == 0) {
                return i;
            }
        }
        
        return -1;
        
    }
}
