package coding.exhaustive;

import java.util.ArrayList;
import java.util.List;

/**
 * level 2 카펫
 */
public class Carpet {

    public int[] solution(int brown, int yellow) {
        int size = brown + yellow;
        List<Integer> width = new ArrayList<>();
        List<Integer> height = new ArrayList<>();

        for (int i = 1; i <= Math.sqrt(size); i++) {
            if (size % i == 0) {
                if (size > i) {
                    width.add(size / i);
                    height.add(i);
                } else {
                    width.add(i);
                    height.add(size / i);
                }
            }
        }

        for (int i = 0; i < width.size(); i++) {
            System.out.println("listForWidth == " + width.get(i) + " listForHeight == " + height.get(i));
        }

        return new int[]{width.get(width.size() - 1), height.get(height.size() - 1)};
    }

    public int[] solutionV2(int brown, int yellow) {
        int[] answer = new int[2];
        int size = brown + yellow;
        int width = 0;
        int height = Integer.MAX_VALUE;

        for (int i = 3; i <= Math.sqrt(size); i++) {
            int j = size / i;
            if (size % i == 0 && j >= 3) {
                width = Math.max(i, j);
                height = Math.min(i, j);

                // System.out.println("w == " + width + " h == " + height);

                if (((width - 2) * (height - 2)) == yellow) {
                    answer[0] = width;
                    answer[1] = height;
                    return answer;
                }
            }
        }

        return new int[]{width, height};
    }
}
