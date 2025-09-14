import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        /**
         * for each element calculate the prefix and suffix value
         * finally traverse return the val as pre * suffix
         */

        Map<Integer, Integer> prefixMap = new HashMap<>();
        Map<Integer, Integer> suffixMap = new HashMap<>();
        int n = nums.length;

        int currentProduct = 1;

        // calculating prefix products for each element
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                prefixMap.put(0, 1);
            } else {
                prefixMap.put(i, currentProduct);
            }
            currentProduct *= nums[i];
        }

        // calculating the suffix product for each element
        currentProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1) {
                suffixMap.put(n - 1, 1);

            } else {
                suffixMap.put(i, currentProduct);
            }
            currentProduct *= nums[i];
        }

        // final answer
        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {
            answer[i] = prefixMap.get(i) * suffixMap.get(i);
        }

        return answer;
    }
}