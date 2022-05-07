class Solution {
    public int characterReplacement(String s, int k) {
        int n = s.length();
        int left = 0;
        int max_length = 0;
        int max_count = 0;
        int[]chars = new int[26];
        
        for (int right = 0; right < n; right++){
            chars[s.charAt(right)-'A']++;
            int current_char_count = chars[s.charAt(right)-'A'];
            max_count = Math.max(max_count,current_char_count);
            
            while (right - left - max_count + 1 > k) {
                chars[s.charAt(left)-'A']--;
                left++;
            }
            
            max_length = Math.max(max_length, right - left + 1);
        }
        
        return max_length;
        
    }
}
