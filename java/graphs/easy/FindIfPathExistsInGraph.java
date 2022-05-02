class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        
        if (source == destination)
            return true;
        
        if (edges.length == 0)
            return false;
        
        ArrayList<Integer>[] adj = new ArrayList[n];
        
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }
        
        return BFS(source, destination, adj);
        
    }
    
    public boolean BFS (int source, int destination, ArrayList<Integer>[] graph) {
                
        boolean [] isVisited = new boolean [graph.length];
        Queue <Integer> queue = new LinkedList<>();
        queue.add(source);
        isVisited[source] = true;
        
        while(!queue.isEmpty()) {
            int vertex = queue.remove();
            
            if (vertex == destination) {
                return true;
            }
            
            for (int i : graph[vertex]) {
                if (!isVisited[i]) {
                    isVisited[i] = true;
                    queue.add(i);
                }
            }
        }
        
        return false;
    }
}
