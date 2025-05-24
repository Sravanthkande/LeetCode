import java.util.*;

class Solution {
    public int maxSubArray(int[] nums) {
        long maxSum = Long.MIN_VALUE;
        long curSum = 0;

        for(int i = 0; i< nums.length; i++){
            curSum += nums[i];

            if(curSum > maxSum){
                maxSum = curSum;
            }

            if (curSum < 0){
                curSum = 0;
            }
        }
        return (int)maxSum;
    }
}