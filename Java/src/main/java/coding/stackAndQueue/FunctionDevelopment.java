package coding.stackAndQueue;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * level 2 기능개발
 * 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
 * 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
 * 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
 * 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가
 * 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
 */
public class FunctionDevelopment {
    public static void main(String[] args) {
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};
        System.out.println(solution(progresses, speeds));
    }

    private static int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        int remaining;
        int count = 1;

        for (int i = 0; i < progresses.length; i++) {
            remaining = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
            queue.add(remaining);
        }

        int maxNumber = !queue.isEmpty() ? queue.poll() : 0;
        while (!queue.isEmpty()) {

            if (maxNumber < queue.peek()) {
                answer.add(count);
                maxNumber = queue.poll();
                count = 1;
            } else {
                queue.poll();
                count += 1;
            }
        }

        answer.add(count);
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
