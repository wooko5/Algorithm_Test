package programmers;

import java.util.*;
/*그래프 문제 중에 처음으로 플로이드-워셜 알고리즘을 구현해서 풀었다. 그래서 인터넷의 코드를 참조해서 풀 수 있었다.
플로이드-워셜 알고리즘은 한 번 실행하여 모든 노드 간 최단 경로를 구할 수 있다. 이를 이용해서 모든 선수(n)들의 경기 결과를 토대로
순위를 알 수 있다 즉 특정 노드로 가는 경로가 n-1 이라면 순위를 알 수 있다.
이를 구하기 위해 모든 노드의 모든 경로가 필요하므로 플로이드-워셜 알고리즘을 사용한다
* 프로그래머스 '순위' 문제, 레벨 3, 2021.10.13*/
class RankingByFloydWarshall {
    int INF = 987654321; //방문불가

    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] scores = new int[n + 1][n + 1];
        int win, lose;

        //배열 전체 INF로 초기화
        for (int[] score : scores) {
            Arrays.fill(score, INF);
        }

        //대각선을 0으로 초기화 (자기 자신에게 가는 그래프가 아니므로)
        for (int i = 0; i < scores.length; i++) {
            for (int j = 0; j < scores.length; j++) {
                if (i == j) scores[i][j] = 0;
            }
        }

        // 단방향 그래프 win -> lose (양방향 그래프가 아니다!)
        for (int[] result : results) {
            win = result[0];
            lose = result[1];
            scores[win][lose] = 1;
        }

        // scores[i][j]로 가는 최단경로 저장하기
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (scores[i][j] > scores[i][k] + scores[k][j]) {
                        scores[i][j] = scores[i][k] + scores[k][j];
                    }
                }
            }
        }

        // 선수들이 게임을 한 적이 있는지 확인하기
        boolean[] flag = new boolean[n + 1];
        Arrays.fill(flag, false);
        for (int i = 1; i <= n; i++) { // 사람 i 기준
            for (int j = 1; j <= n; j++) { // 나머지 j 선수들과 게임한적 있는지 체크
                if (i == j) {
                    continue; // 자신과 게임하는 것은 무시하기
                }
                if (scores[i][j] == INF && scores[j][i] == INF) { // 경로가 존재하지 않으면 (i와 j가 게임하지 않았다면)
                    flag[i] = true;
                    break; // 모두와 게임을 해야하므로
                }
            }
        }

        for (int i = 1; i < flag.length; i++) {
            if (!flag[i]) {
                answer += 1;
            }
        }
        return answer;
    }
}


class Node {
    int win;
    int lose;
}

class RankingByBFS {
    static ArrayList<Integer>[] adj;
    static Node[] nodes;
    static int N;

    public int solution(int n, int[][] results) {
        adj = new ArrayList[n + 1];
        nodes = new Node[n + 1];
        N = n;

        for (int i = 0; i < N + 1; i++) {
            adj[i] = new ArrayList<>();
            nodes[i] = new Node();
        }

        for (int[] result : results) {
            int winner = result[0];
            int loser = result[1];
            adj[winner].add(loser);
        }

        nodeUpdate();
        return hasRank();
    }

    private void nodeUpdate() {
        for (int i = 1; i < N + 1; i++) {
            Queue<Integer> queue = new LinkedList<>();
            boolean[] visited = new boolean[N + 1];

            visited[i] = true;
            queue.offer(i);

            while (!queue.isEmpty()) {
                int winner = queue.poll();

                for (int loser : adj[winner]) {
                    if (visited[loser]) {
                        continue;
                    }
                    visited[loser] = true;
                    queue.offer(loser);
                    nodes[i].win++;
                    nodes[loser].lose++;
                }
            }
        }
    }

    private int hasRank() {
        int count = 0;
        for (Node node : nodes) {
            if (node.win + node.lose == N - 1) {
                count++;
            }
        }
        return count;
    }
}