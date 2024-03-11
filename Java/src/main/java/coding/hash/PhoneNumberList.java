package coding.hash;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PhoneNumberList {
    public static void main(String[] args) {
        String[] phone_book = {"119", "97674223", "1195524421"};
//        System.out.println(solutionV1(phone_book));
        System.out.println(solutionV2(phone_book));
    }

    //정렬과 반복문을 이용한 풀이
    public static boolean solutionV1(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);

        for (int i = 0; i < phone_book.length - 1; i++) {
            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }

        return answer;
    }

    public static boolean solutionV2(String[] phone_book) {
        boolean answer = true;
        Map<String, Integer> hashMap = new HashMap<>();

        for (int index = 0; index < phone_book.length; index++) {
            hashMap.put(phone_book[index], index);
        }

        for (String phone : phone_book) {
            for (int j = 1; j < phone.length(); j++) {
                if (hashMap.containsKey(phone.substring(0, j))) {
                    return false;
                }
            }
        }
        return answer;
    }
}
