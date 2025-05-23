import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> triplets = new HashSet<>();
        int N = nums.length;

        for (int i = 0;i < N; i++){
            Set<Integer> hashset = new HashSet<>();
            for (int j = i+1 ; j < N; j++){
                int third = - (nums[i]+nums[j]);
                if(hashset.contains(third)){
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[j]);
                    temp.add(third);

                    Collections.sort(temp);
                    triplets.add(temp);
                }
                hashset.add(nums[j]);
            }
        }

        List<List<Integer>> ans = new ArrayList<>(triplets);
        return ans;
    }
}