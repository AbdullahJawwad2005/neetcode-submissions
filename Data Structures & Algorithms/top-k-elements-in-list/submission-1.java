class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            Integer value = 1 + map.getOrDefault(nums[i], 0); // checks if occurence and if no then zero
            map.put(nums[i], value); // adds value + 1 to the number-frequency pair
        } 
        List<Integer> keys = new ArrayList<>(map.keySet());
        keys.sort((a,b) -> map.get(b) - map.get(a));
        keys = keys.subList(0, k);
        int[] keysint = new int[k];
        for(int i=0; i<k; i++) {
            keysint[i] = keys.get(i);
        }
        return keysint;
    }
}
