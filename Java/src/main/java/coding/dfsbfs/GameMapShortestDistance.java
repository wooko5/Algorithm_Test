package coding.dfsbfs;

import java.util.LinkedList;
import java.util.Queue;

public class GameMapShortestDistance {
//    private int answer = Integer.MAX_VALUE;

    public static void main(String[] args) {
        int[][] maps = {{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 0, 1}, {0, 0, 0, 0, 1}};
        System.out.println(new GameMapShortestDistance().solution(maps));
    }

//    public int solution(int[][] maps) {
//
//        //도착지를 갈 수 없는 경우
//        if (maps[maps.length - 2][maps[0].length - 1] == 0 && maps[maps.length - 1][maps[0].length - 2] == 0) {
//            return -1;
//        }
//
//        //도착지를 갈 수 있는 경우
//        boolean[][] visited = new boolean[maps.length][maps[0].length];
//        explore(visited, maps, 0, 0, 1); //count가 1인 이유: 항상 시작점(0,0)에서 시작하기 때문에 해당 칸도 포함하기 때문
//        if (!visited[maps.length - 1][maps[0].length - 1]) {
//            return -1;
//        }
//        return answer;
//    }
//
//    public void explore(boolean[][] visited, int[][] maps, int x, int y, int count) {
//
//        visited[x][y] = true;
//        int[][] direction = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
//
//        if (x == maps.length - 1 && y == maps[0].length - 1) {
//            answer = Math.min(answer, count);
//            return;
//        }
//
//        for (int[] way : direction) {
//            int currentX = x + way[0];
//            int currentY = y + way[1];
//
//            if (currentX < 0 || currentX > maps.length - 1 || currentY < 0 || currentY > maps[0].length - 1) {
//                continue; //지도를 벗어난 경우 스킵하기
//            }
//
//            if (!visited[currentX][currentY] && maps[currentX][currentY] == 1) {
//                explore(visited, maps, currentX, currentY, count + 1);
//                System.out.println("currentX == " + currentX + " currentY == " + currentY + " count == " + count);
//            }
//        }
//    }

    private int answer = -1;
    private int[][] direction = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    public int solution(int[][] maps) {

        //도착지를 갈 수 있는 경우
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        bfs(maps, visited);

        return answer;
    }

    public void bfs(int[][] maps, boolean[][] visited) {
        visited[0][0] = true;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1});


        while (!queue.isEmpty()) {

            int[] position = queue.poll();
            int x = position[0];
            int y = position[1];
            int count = position[2];

            if (x == maps.length - 1 && y == maps[0].length - 1) {
                answer = count;
                break;
            }

            for (int[] way : direction) { 
                int currentX = x + way[0];
                int currentY = y + way[1];

                if (currentX < 0 || currentX > maps.length - 1 || currentY < 0 || currentY > maps[0].length - 1) {
                    continue; //지도를 벗어난 경우 스킵하기
                }

                if (!visited[currentX][currentY] && maps[currentX][currentY] == 1) {
                    visited[currentX][currentY] = true;
                    queue.add(new int[]{currentX, currentY, count + 1});
                }
            }
        }
    }
}
