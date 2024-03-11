package coding.hash;

import java.util.HashMap;
import java.util.Map;

/**
 * level 1
 */
public class Ponkenmon {

    public static void main(String[] args) {
        int[] nums = {3, 1, 2, 3};
        int answer = 0;

        Map<Integer, Integer> hashMap = new HashMap<>();

        for (int num : nums) {
            if (hashMap.containsKey(num)) {
                int value = hashMap.get(num);
                value += 1;
                hashMap.put(num, value);
            } else {
                hashMap.put(num, 1);
                answer += 1;
            }
        }

        hashMap.forEach((key, value) -> System.out.println("key == " + key + " " + "value == " + value));

        answer = nums.length / 2 < answer ? nums.length / 2 : answer;
        System.out.println(answer);
    }
}
