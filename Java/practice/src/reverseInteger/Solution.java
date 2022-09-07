package reverseInteger;

import java.lang.Math;

public class Solution {
    public static void main(String[] args) {
        int x = 1534236469;
        int r = reverse(x);
        System.out.println(r);
    }

    public static int reverse(int x) {
        if (x > -10 && x < 10) {
            return x;
        }
        int p = x / Math.abs(x);
        x = Math.abs(x);
        int num = x;
        int count = 0;
        while (num > 0) {
            count++;
            num /= 10;
        }

        int sum = 0;
        int i = 0;
        while (i < count) {
            sum += x % 10 * Math.pow(10, count - i - 1);
            i++;
            x /= 10;
            if (sum == Integer.MAX_VALUE) {
                return 0;
            }
        }
        return sum * p;
    }
}
