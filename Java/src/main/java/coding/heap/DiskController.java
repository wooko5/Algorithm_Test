package coding.heap;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * level 3 디스크컨트롤러
 *
 */
public class DiskController {
    public static void main(String[] args) {
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        System.out.println(solution(jobs));
    }

    private static int solution(int[][] jobs) {
        int result = 0;
        int time = 0;
        Arrays.sort(jobs, (j1, j2) -> j1[1] - j2[1]); //'작업의 소요시간'을 기준으로 오름차순 정렬

        List<Pair> sortedDisk = new ArrayList<>();
        for (int[] job : jobs) {
            sortedDisk.add(new Pair(job[0], job[1]));
        }

        while (!sortedDisk.isEmpty()) {
            for (int i = 0; i < sortedDisk.size(); i++) {

                if (time >= sortedDisk.get(i).getTime()) { //현재시간(time)이 현재 요청작업 시점과 같거나 과거인 경우
                    time += sortedDisk.get(i).getWorktime(); //현재시간은 '작업의 소요시간'을 더하고
                    result += time - sortedDisk.get(i).getTime(); //총 작업시간(result)에 실제 소요된 시간을 더하고
                    sortedDisk.remove(i); //작업이 완료됐으니 해당 작업은 디스크에서 제거
                    break;
                }

                if (i == sortedDisk.size() - 1) { //디스크의 마지막 작업까지 왔다면 시간을 1초 증가
                    time += 1;
                }
            }
        }
        return result / jobs.length;
    }

    static class Pair {
        private int time;
        private int worktime;

        public int getTime() {
            return this.time;
        }

        public int getWorktime() {
            return this.worktime;
        }

        public Pair(int time, int worktime) {
            this.time = time;
            this.worktime = worktime;
        }
    }
}
