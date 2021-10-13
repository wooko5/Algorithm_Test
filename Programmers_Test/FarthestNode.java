package com.programmers.java;
import java.util.LinkedList;
import java.util.Queue;

/*
* 노드1에서 다른 노드까지의 거리를 구하고, 구한 거리를 배열(distance)에 저장해서 가장 큰 거리를 구하고
* 가장 큰 거리값이 배열에서 몇 개 있는지 세기만 하면 끝나는 간단한 문제였지만 자바로 bfs(큐 이용)를 해보질 못 해서
* 인터넷의 힌트를 참조할 수 밖에 없었다. dfs와 bfs 같은 기존에 배운 개념을 자바로 다시 푸는 연습을 많이 해야겠다
* 프로그래머스 '가장 먼 노드' 문제, 레벨 3, 2021.10.12*/

class FarthestNode {
    public int solution(int n, int[][] edge) {
        int[] distance = new int[n + 1];
        boolean[][] matrix = new boolean[n + 1][n + 1]; // int[][]로 선언하면 메모리 초과나옴
        int r1, r2, r3, c2;

        for (int[] e : edge) {
            matrix[e[0]][e[1]] = matrix[e[1]][e[0]] = true;
        }

        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(1);

        // BFS 탐색
        int maxDistance = 0;
        while (!queue.isEmpty()) {
            int i = queue.poll(); // 큐의 가장 앞에 있는 원소 빼내기 pop(0)

            for (int j = 2; j <= n; j++) {
                if (distance[j] == 0 && matrix[i][j]) {
                    distance[j] = distance[i] + 1;
                    queue.add(j);
                    maxDistance = Math.max(maxDistance, distance[j]);
                }
            }
        }

        // 가장 멀리 있는 노드가 몇 개인지 계산
        int count = 0;
        for (int dist : distance) {
            if (maxDistance == dist)
                count += 1;
        }
        return count;
    }

    public static void main(String[] args) {
        FarthestNode farthestNode = new FarthestNode();
        int n = 6;
        int[][] edge = {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}};
        System.out.println(farthestNode.solution(n, edge));
    }
}
