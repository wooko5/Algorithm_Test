package coding.sorting;

import java.util.Arrays;

/**
 * level 2 가장 큰 수
 * 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
 * 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
 * 이중 가장 큰 수는 6210입니다.
 * 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
 * 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
 */
public class BiggestNumber {
    public static void main(String[] args) {
        int[] numbers = {6, 10, 2};
        System.out.println(solution(numbers));
    }

    private static String solution(int[] numbers) {
        String[] result = new String[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            result[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(result, (v1, v2) -> (v2 + v1).compareTo(v1 + v2));

        if(result[0].equals("0")){
            return "0";
        }

//        List.of(result).forEach(System.out::println);

        StringBuilder stringBuilder = new StringBuilder();

        Arrays.stream(result).forEach(stringBuilder::append);

        return stringBuilder.toString();
    }
}
