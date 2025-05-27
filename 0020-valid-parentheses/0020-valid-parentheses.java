class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')','(');
        mapping.put('}','{');
        mapping.put(']','[');

        for (char ch: s.toCharArray()){
            if (mapping.containsKey(ch)){
                char top = stack.isEmpty() ? '#' : stack.pop();
                if (top != mapping.get(ch)){
                    return false;
                }
            }else{
                stack.push(ch);
            }
        }
        return stack.isEmpty();
    }
}