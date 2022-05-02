class Solution {
    public int maxSubArray(int[] nums) {
        int result = nums[0];
        int sum = nums[0];
 
        for (int i = 1; i< nums.length; i++) {
            if (sum + nums[i] > nums[i]) {
                sum = sum + nums[i];
            } else {
                sum = nums[i];
            }
            result = Math.max(result, sum);
        }

        return result;
        
    }
}
