class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int candidate = 0;
        int N = nums.length;


        for (int i=0; i<N; i++){
            if (count == 0){
                candidate = nums[i];
                count = 1;
            }else if(candidate == nums[i]){
                count += 1;
            }else{
                count -= 1;
            }
        }

        int count1 = 0;
        for (int i = 0; i< N; i++){
            if (nums[i] == candidate){
                count1++;
            }
        }

        if(count1 > (N/2)){
            return candidate;
        }

        return -1;
    }
}