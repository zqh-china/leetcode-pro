package medianofTwoSortedArrays;

import java.util.Arrays;

class Solution {
    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};
        double r = findMedianSortedArrays(nums1, nums2);
        System.out.println(r);
    }


    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        double[] nums = new double[m + n];
        int medianIndex = (m + n) / 2;
        int currA = 0;
        int currB = 0;
        for (int i = 0; i <= medianIndex; i++) {
            if (currA < nums1.length && currB < nums2.length) {
                if (nums1[currA] > nums2[currB]) {
                    nums[i] = nums2[currB];
                    currB++;
                } else {
                    nums[i] = nums1[currA];
                    currA++;
                }
            }else if(currA < nums1.length && currB == nums2.length){
                nums[i] = nums1[currA];
                currA++;
            } else if (currA == nums1.length && currB < nums2.length){
                nums[i] = nums2[currB];
                currB++;
            }
            else{
                break;
            }
        }
        if ((m + n) % 2 != 0) {
            return nums[medianIndex];
        } else {
            return (nums[medianIndex] + nums[medianIndex - 1]) / 2;
        }
    }
}