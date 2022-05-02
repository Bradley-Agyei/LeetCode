class Solution {
    public void rotate(int[] nums, int k) {
        int[]temp = new int[nums.length];
        int index = k % nums.length;
        
        if (nums.length < 2) {
            return;
        }
        
        for (int i = 0; i< nums.length; i++) {
            if (index > nums.length-1) {
                index = index / nums.length-1;
            } 
            
            temp[index] = nums[i];
            index++;
            
        }
        
        for(int i = 0; i < nums.length; i++) {
            nums[i] = temp[i];
        }
        
    }
}
