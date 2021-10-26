package programmers;

import java.util.*;

public class KthNumber {

    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            List<Integer> arrayList = new ArrayList<>();
            for (int start = commands[i][0] - 1; start < commands[i][1]; start++) {
                arrayList.add(array[start]);
            }
            arrayList.sort(Comparator.naturalOrder());
            answer[i] = arrayList.get(commands[i][2] - 1);
        }
        return answer;
    }
}
