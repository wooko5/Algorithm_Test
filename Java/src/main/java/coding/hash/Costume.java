package coding.hash;

import java.util.HashMap;
import java.util.Map;

/**
 * level 2
 * 2종류 안경, 1종류의 바지의 모든 조합의 수는 (2+1) * (1+1)이다.
 * 왜냐하면 입지 않는 경우 1가지를 항상 모든 의상 종류마다 더해줘서 곱해야하기 때문
 * 그리고 모든 의상을 입지않은 1가지를 전체 경우의 수에서 빼면 정답이 나옴
 */
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

        for (int number : map.values()) {
            answer *= (number + 1);
        }
        return answer - 1;

//        Arrays.asList(map).forEach(System.out::println);
    }
}
