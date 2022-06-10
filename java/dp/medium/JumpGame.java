class Solution {
    public boolean canJump(int[] nums) {
//         int[] memo = new int[nums.length];
//         Arrays.fill(memo, -1);
        
        
//         return canJumpRec(0, nums, memo);
        int lastPos = nums.length-1;
        for(int i = nums.length-1; i >= 0; i--) {
            if(i + nums[i] >= lastPos) {
                lastPos = i;
            }
        }
        
        return lastPos == 0;
        
    }
    
//     public static boolean canJumpRec(int index, int[] nums, int[] memo) {
        
//         if(index == nums.length - 1) {return true;}
        
//         if(memo[index] != -1) {
//             return memo[index] == 1;
//         }
        
//         int longestJump = Math.min(index + nums[index], nums.length-1);
//         for(int nextPos = index + 1; nextPos <= longestJump; nextPos++) {
//             if(canJumpRec(nextPos,nums, memo)) {
//                 memo[index] = 1;
//                 return true;
//             }
            
//         }
//         memo[index] = 0;
//         return false;
//     }
}
