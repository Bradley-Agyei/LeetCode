class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return intersect(nums2, nums1);
        }
        
        Map<Integer, Integer> hm = new HashMap<>();
        
        for (int i : nums1) {
            hm.put(i, hm.getOrDefault(i, 0) + 1);
        }
        
        int k = 0;
        
        for ( int j : nums2) {
            if (hm.getOrDefault(j, 0) > 0) {
                nums1[k++] = j;
                hm.put(j, hm.getOrDefault(j, 0) - 1);
            }
        }
        
        return Arrays.copyOfRange(nums1, 0, k);
        
    }
}
