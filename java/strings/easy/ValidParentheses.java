class Solution {
    public static final Map<Character, Character> map = Map.of('(',')',
                                                               '{','}',
                                                               '[',']');
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for(char c : s.toCharArray()) {
            if(map.containsKey(c)) {
                stack.push(c);
            } else {
                if(stack.isEmpty()) {
                    return false;
                }
                char open = stack.pop();
                if(c != map.get(open)) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}
