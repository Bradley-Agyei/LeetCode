class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[]temp = new int [nums1.length];
        int leftStart = 0;
        int leftEnd = m-1;
        int rightStart = 0;
        int rightEnd = n-1;
        int index = leftStart;
        int left = leftStart;
        int right = rightStart;
        
        while (left <= leftEnd && right <= rightEnd) {
            if (nums1[left] <= nums2[right]) {
                temp[index] = nums1[left];
                left++;
            } else {
                temp[index] = nums2[right];
                right++;
            }
            
            index++;
        }

        
        while (left <= leftEnd) {
            temp[index++] = nums1[left++];

        }
        
        while (right <= rightEnd) {
            temp[index++] = nums2[right++];
        }
        

        System.arraycopy(temp,leftStart, nums1, leftStart, nums1.length);
        
        
    }
}
