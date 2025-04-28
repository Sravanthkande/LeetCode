class Solution {
    public int longestOnes(int[] nums, int k) {
        int N = nums.length;
        int left = 0, right = 0;
        int zeros = 0, maxLen = 0;

        while(right < N){
            if(nums[right] == 0){
                zeros++;
            }
            while(zeros > k){
                if(nums[left] == 0){
                    zeros--;
                }
                left++;
            }
            int length = right - left + 1;
            maxLen = Math.max(maxLen, length);
            right ++;
        }
        return maxLen;
    }
}