package coding.stackAndQueue;

import java.util.Arrays;
import java.util.Stack;

/**
 * level 2 뒤에 있는 큰 수 찾기
 */
public class FindTheBextBigNumber {

    public static void main(String[] args) {
        int[] numbers = {2, 3, 3, 5};
        System.out.println(Arrays.toString(solution(numbers)));
    }

    private static int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);
        Stack<Integer> stack = new Stack<>(); //index만 넣어두는 스택

        for (int i = 0; i < numbers.length; i++) {
            while (!stack.empty() && numbers[i] > numbers[stack.peek()]) { //현재값(numbers[i])이 스택의 index가 가리키는 값보다 클 때
                answer[stack.pop()] = numbers[i];
            }
            stack.push(i);
        }

        return answer;
    }
}
