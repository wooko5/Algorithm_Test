package test;

/* 2021.12.29 '로또의 최고 순위와 최저 순위'라는 프로그래머스 레벨1 구현 문제 */
class TheHighestAndLowestRanksOfTheLottery {

    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int count = 0;
        int zero = 0;
        for (int lotto : lottos) {
            if (lotto == 0) {
                zero += 1;
                continue;
            }
            for (int win_num : win_nums) {
                if (lotto == win_num) {
                    count += 1;
                    break;
                }
            }
        }
        answer[0] = calculate(count + zero);
        answer[1] = calculate(count);
        return answer;
    }

    private static int calculate(int number) {
        if (number == 6) {
            return 1;
        }
        if (number == 5) {
            return 2;
        }
        if (number == 4) {
            return 3;
        }
        if (number == 3) {
            return 4;
        }
        if (number == 2) {
            return 5;
        } else {
            return 6;
        }
    }
}
