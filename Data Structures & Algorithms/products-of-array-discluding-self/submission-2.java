class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        int[] output = new int[nums.length];

        prefix[0] = nums[0];
        for(int i=1; i< nums.length; i++) {
            prefix[i] = prefix[i-1]*nums[i];
        }
        suffix[nums.length - 1] = nums[nums.length - 1];
        for(int i=nums.length-2; i>=0; i--) {
            suffix[i] = suffix[i+1]*nums[i];
        }

        for(int i=0; i<nums.length; i++) {
            if(i==0) {
                output[i] = suffix[1];
            }
            else if(i==nums.length - 1) {
                output[i] = prefix[nums.length - 2];
            }
            else {
                output[i] = prefix[i-1]*suffix[i+1];
            }
        }

        return output;
    }
}  
