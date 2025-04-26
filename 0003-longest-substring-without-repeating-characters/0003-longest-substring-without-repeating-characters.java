class Solution {
    public int lengthOfLongestSubstring(String s) {
        int N = s.length();
        int maxLen = 0;

        for(int i=0;i<N;i++){
            int[] hash = new int[256];
            Arrays.fill(hash, 0);
            for(int j =i;j<N;j++){
                if(hash[s.charAt(j)] == 1) break;
                hash[s.charAt(j)] = 1;
                int len = j - i + 1;
                maxLen = Math.max(maxLen, len);
            }
        }
        return maxLen;
    }
}