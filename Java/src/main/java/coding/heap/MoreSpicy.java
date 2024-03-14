package coding.heap;

import java.util.PriorityQueue;

/**
 * level 2 더 맵게
 */
public class MoreSpicy {
    public static void main(String[] args) {
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;
        System.out.println(solution(scoville, K));
    }

    private static int solution(int[] scoville, int K) {
        int answer = 0;
        boolean check = false;
        int scovilleFlavor;
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        for (int sco : scoville) {
            priorityQueue.add(sco);
        }

        if (priorityQueue.peek() >= K && !priorityQueue.isEmpty()) { //해당 체크를 못 해서 TC18을 계속 틀렸음
            return answer;
        }

        while (priorityQueue.size() > 1) {
            int firstNotSpicy = priorityQueue.poll();
            int secondNotSpicy = priorityQueue.poll();
            scovilleFlavor = firstNotSpicy + (secondNotSpicy * 2);
            priorityQueue.add(scovilleFlavor);
            answer += 1;

            if (priorityQueue.peek() >= K) {
                check = true;
                break;
            }
        }
        return check ? answer : -1;
    }
}
