package coding.exhaustive;

/**
 * level1 최소 사각형
 */
public class MinimumRectangle {
    public static void main(String[] args) {
        int[][] sizes = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
        System.out.println(solution(sizes));
    }

    public static int solution(int[][] sizes) {
//        Arrays.sort(sizes, (o1, o2) -> o1[0]!=o2[0] ? o1[0]-o2[0] : o2[1]-o1[1]); //다차원 배열에서 다중조건 정렬(0열 오름차순, 만약 같으면 1열 내림차순)
        int max = 0;
        int min = 0;

        for (int[] size : sizes) {
            if (max < Math.max(size[0], size[1])) {
                max = Math.max(size[0], size[1]);
            }

            if (min < Math.min(size[0], size[1])) {
                min = Math.min(size[0], size[1]);
            }
        }

        return max * min;
    }
}
