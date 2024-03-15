package coding.exhaustive;

import java.util.ArrayList;
import java.util.List;

/**
 * level 2 모의고사
 */
public class MockExam {
    public static void main(String[] args) {
        int[] answers = {1, 2, 3, 4, 5};
        System.out.println(solutionV2(answers));
    }

    public int[] solutionV1(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        // 1, 2, 3, 4, 5 == 5개
        // 2, 1, 2, 3, 2, 4, 2, 5 == 8개
        // 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 == 10개

        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int countFirst = 0;
        int countSecond = 0;
        int countThird = 0;

        for (int i = 0; i < answers.length; i++) {
            if (first[i % 5] == answers[i]) {
                countFirst += 1;
            }
            if (second[i % 8] == answers[i]) {
                countSecond += 1;
            }
            if (third[i % 10] == answers[i]) {
                countThird += 1;
            }
        }


        int[] result = {countFirst, countSecond, countThird};
        int max = Math.max(countFirst, Math.max(countSecond, countThird));

        for (int i = 0; i < result.length; i++) {
            if (max == result[i]) {
                answer.add(i + 1);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    public static int[] solutionV2(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int[] score = {0, 0, 0};
        // 1, 2, 3, 4, 5 == 5개
        // 2, 1, 2, 3, 2, 4, 2, 5 == 8개
        // 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 == 10개

        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        for (int i = 0; i < answers.length; i++) {
            if (first[i % 5] == answers[i]) {
                score[0] += 1;
            }
            if (second[i % 8] == answers[i]) {
                score[1] += 1;
            }
            if (third[i % 10] == answers[i]) {
                score[2] += 1;
            }
        }

        int max = Math.max(score[0], Math.max(score[1], score[2]));

        for (int i = 0; i < score.length; i++) {
            if (max == score[i]) {
                answer.add(i + 1);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}
