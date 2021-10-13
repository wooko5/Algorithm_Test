package com.programmers.java;

/*
* 단순한 구현문제였다 확실히 자바가 이중배열 초기화가 파이썬에 비해 복잡하지만 index를 잘 활용한다면 어렵지 않았다.
* 대신 오늘 같은 문제는 '구현'유형으로 보이는데 회전을 순서를 잡고 해야함을 안다면 어렵지 않은 문제였지만
* 자바이기에 열심히 준비해야겠다.
* 프로그래머스 '행렬 테투리 회전하기' 문제, 레벨 2, 2021.10.12*/

public class RotateMatrixBorders {
    private int[][] matrix;

    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        matrix = new int[rows][columns];
        int r1, r2, c1, c2;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = (i * columns) + (j + 1);
            }
        }

        for (int index = 0; index < queries.length; index++) {
            r1 = queries[index][0] - 1;
            c1 = queries[index][1] - 1;
            r2 = queries[index][2] - 1;
            c2 = queries[index][3] - 1;
            answer[index] = rotateMatrix(r1, c1, r2, c2);
            System.out.println(answer[index]);
        }
        return answer;
    }

    public int rotateMatrix(int r1, int c1, int r2, int c2) {

        int startPoint = this.matrix[r1][c1];
        int minResult = startPoint;

        for (int i = r1; i < r2; i++) { // 회전의 1번 UP
            this.matrix[i][c1] = this.matrix[i + 1][c1];
            if (minResult > this.matrix[i][c1]) minResult = this.matrix[i][c1];
        }

        for (int i = c1; i < c2; i++) { // 회전의 2번 LEFT
            this.matrix[r2][i] = this.matrix[r2][i + 1];
            if (minResult > this.matrix[r2][i]) minResult = this.matrix[r2][i];
        }

        for (int i = r2; i > r1; i--) { // 회전의 3번 DOWN
            this.matrix[i][c2] = this.matrix[i - 1][c2];
            if (minResult > this.matrix[i][c2]) minResult = this.matrix[i][c2];
        }

        for (int i = c2; i > c1; i--) { // 회전의 4번 RIGHT
            this.matrix[r1][i] = this.matrix[r1][i - 1];
            if (minResult > this.matrix[r1][i]) minResult = this.matrix[r1][i];
        }

        this.matrix[r1][c1 + 1] = startPoint;
        return minResult;
    }

    public static void main(String[] args) {
        RotateMatrixBorders rotateMatrixBorders = new RotateMatrixBorders();
        int rows = 6;
        int columns = 6;
        int[][] queries = {{1, 1, 2, 2}, {1, 2, 2, 3}, {2, 1, 3, 2}, {2, 2, 3, 3}};
        rotateMatrixBorders.solution(rows, columns, queries);
    }
}
