package test;

public class ChuseokTraffic {
    private StringBuffer sbForResponseTime;
    private StringBuffer sbForTime;

    public int solution(String[] lines) {
        if (lines.length == 1) {
            return 1;
        }

        int answer = 0;

        for (String line : lines) {
            sbForResponseTime = new StringBuffer();
            sbForTime = new StringBuffer();
            int index = 0;

            for (int j = 11; j < line.length(); j++) {
                if (line.charAt(j) == ' ') {
                    index = j + 1;
                    break;
                }
                sbForResponseTime.append(line.charAt(j));
            }

            for (int j = index; j < line.length() - 1; j++) {
                sbForTime.append(line.charAt(j));
            }

            System.out.println(sbForResponseTime); // 01:00:04.001
            System.out.println(sbForTime); // 2.0
        }


        return answer;
    }

    public static void main(String[] args) {
        ChuseokTraffic chuseokTraffic = new ChuseokTraffic();
        String[] lines = {"2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"};
        System.out.println(chuseokTraffic.solution(lines));
    }
}
