package coding.stackAndQueue;

import java.util.*;

public class Process {

    public static void main(String[] args) {
//        int[] priorities = {2, 1, 3, 2};
//        int location = 2;
        int[] priorities = {1, 1, 9, 1, 1, 1};
        int location = 0;
        System.out.println(solution(priorities, location));
    }

    private static int solution(int[] priorities, int location) {
        int max = Arrays.stream(priorities).max().orElse(0);
        Queue<Integer> indexQueue = new LinkedList<>();

        List<Integer> result = new ArrayList<>();
        Integer[] boxedArray = Arrays.stream(priorities).boxed().toArray(Integer[]::new);
        Queue<Integer> queue = new LinkedList<>(Arrays.asList(boxedArray));


        for (int i = 0; i < priorities.length; i++) {
            indexQueue.add(i);
        }

        while (!queue.isEmpty()) {
            int poll = queue.poll();
            int index = indexQueue.poll();

            if (max > poll) {
                queue.add(poll);
                indexQueue.add(index);
            } else {
                max = Arrays.stream(queue.stream().mapToInt(i -> i).toArray()).max().orElse(0);
                result.add(index);
            }
        }

        return result.indexOf(location) + 1;
    }
}
