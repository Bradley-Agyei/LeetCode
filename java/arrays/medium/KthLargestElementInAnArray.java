class Solution {
    public int findKthLargest(int[] nums, int k) {
//         // [1,2,3,4,5,6]
//         // first largest is 6
//         //second largest is 5
        
//         //[1,2,2,3,3,4,5,5,6]
//         int n = nums.length;
//         Arrays.sort(nums);
        
//         int index = n - k;
            
//         return nums[index];
               // init heap 'the smallest element first'
        PriorityQueue<Integer> heap =
            new PriorityQueue<Integer>();

        // keep k largest elements in the heap
        for (int n: nums) {
          heap.add(n);
          if (heap.size() > k)
            heap.poll();
        }

        // output
        return heap.poll();
        
        
    }
}
