package JumpGameII;

public class Solution {
    public static void main(String[] args) {
        int[] arr = {2, 3, 1, 1, 4};
        int stpes = jump(arr);
        System.out.println(stpes);
    }

    public static int jump(int[] nums) {

        int now_posi = 0;
        int farest_posi = 0;
        int steps = 0;
        int dst = nums.length - 1;
        int end = 0;
        while (end < dst) {
            farest_posi = Math.max(farest_posi, nums[now_posi]+now_posi);
            if (now_posi == end) {
                end = farest_posi;
                steps++;
            }
            now_posi++;
        }
        return steps;
    }

}
