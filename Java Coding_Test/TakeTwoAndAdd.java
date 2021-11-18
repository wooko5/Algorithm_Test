package programmers;
import java.util.*;

/*프로그래머스 '두 개 뽑아 더하기' 문제, 레벨 1, 2021.11.16*/
public class TakeTwoAndAdd {
    public int[] solution(int[] numbers) {
        int[] answer;
        int number;
        HashSet<Integer> hashSet = new HashSet<>();
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                number = numbers[i] + numbers[j];
                hashSet.add(number);
            }
        }

        Integer[] array = hashSet.toArray(new Integer[0]); // SET을 Integer[]로 변환
        answer = Arrays.stream(array).mapToInt(Integer::intValue).toArray(); // Integer[]을 int[]로 변환
        Arrays.sort(answer); // 오름차순 배열 정렬
        return answer;
    }
}
