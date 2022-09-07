package searchInsertPosition;

class Solution {
    public int searchInsert(int[] nums, int target) {
        if (target <= nums[0]){
            return 0;
        }
        if (target >= nums[nums.length-1]){
            return nums.length;
        }
        int left = 0;
        int ans = nums.length;
        int right = ans - 1;

        while (left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid] < target){
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
}