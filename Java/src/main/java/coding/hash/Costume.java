package coding.hash;

import java.util.HashMap;
import java.util.Map;

public class Costume {
    public static void main(String[] args) {
        String[][] clothes = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};

        System.out.println(solution(clothes));
    }

    public static int solution(String[][] clothes) {
        int answer = 1;

        Map<String, Integer> map = new HashMap<>();

        for (String[] clothe : clothes) {
            if (map.containsKey(clothe[1])) {
                int value = map.get(clothe[1]);
                value += 1;
                map.put(clothe[1], value);
            } else {
                map.put(clothe[1], 1);
            }

        }

        if (map.keySet().size() > 1) {
            for (int num : map.values()) {
                answer *= num;
            }
            return answer + clothes.length;
        }
        return clothes.length;

//        Arrays.asList(map).forEach(System.out::println);
    }
}
