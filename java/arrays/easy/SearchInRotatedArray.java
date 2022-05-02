class Solution {
    public int search(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length-1;
        
        int pivot = findPivot(nums, lo, hi);
        
        if (pivot == -1)
            return binarySearch(nums, lo, hi, target);
            
        
        if (nums[pivot] == target)
            return pivot;
        
        if (target < nums[lo])
            return binarySearch(nums,(pivot+1), hi, target);
            
        else
            return binarySearch(nums, lo, (pivot - 1), target);
    }
    
    public int findPivot(int[]nums, int lo, int hi) {
        
        if(hi < lo)
            return -1;
        if(hi == lo)
            return lo;
        
        int mid = lo + (hi - lo) / 2;
        
        if (mid < hi && nums[mid] > nums[mid + 1])
            return mid;
        if (mid > lo && nums[mid] < nums[mid - 1])
            return mid - 1;
        if (nums[lo] >= nums[mid])
            return findPivot(nums, lo, (mid-1));
        return findPivot(nums, (mid+1), hi);
    }
    
    public int binarySearch(int[]nums, int lo, int hi, int target) {
        
        if(hi < lo)
            return -1;
        
        int mid = lo + (hi - lo) / 2;
        
        if (nums[mid] == target)
            return mid;
        if (nums[mid] < target)
            return binarySearch(nums,(mid+1), hi, target);
        if (nums[mid] > target)
            return binarySearch(nums, lo, (mid-1), target);
        return -1;
    }
}
