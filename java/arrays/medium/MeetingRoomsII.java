class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Comparator<Integer> c = (a, b) -> { 
            return a - b;
        };
        
        Queue<Integer> minHeap = new PriorityQueue<>(intervals.length,c );
        
        Arrays.sort(intervals, (a,b)->a[0] - b[0]);
        
       minHeap.add(intervals[0][1]);
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= minHeap.peek()) {
                minHeap.poll();
            }
            
            minHeap.add(intervals[i][1]);
        }
        
        return minHeap.size();
        
    }
}
