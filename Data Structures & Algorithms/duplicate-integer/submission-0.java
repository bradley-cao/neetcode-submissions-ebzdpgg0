class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> ints = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (ints.contains(nums[i])) {
                return true;
            }
            ints.add(nums[i]);
        }
        return false;
    }
}
