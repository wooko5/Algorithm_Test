package programmers;


public class CaesarCipher {
    private String lowAlphabet;
    private String highAlphabet;
    private int index;

    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();
        lowAlphabet = "abcdefghijklmnopqrstuvwxyz";
        highAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isSpaceChar(c)) {
                answer.append(" ");
            } else {
                if (Character.isUpperCase(c)) {
                    index = highAlphabet.indexOf(c);
                    index = (index + n) % 26;
                    answer.append(highAlphabet.charAt(index));
                } else if (Character.isLowerCase(c)) {
                    index = lowAlphabet.indexOf(c);
                    index = (index + n) % 26;
                    answer.append(lowAlphabet.charAt(index));
                }
            }
        }
        return answer.toString();
    }

    public static void main(String[] args) {
        CaesarCipher c = new CaesarCipher();
        System.out.println("s는 'a B z', n은 4인 경우: " + c.solution("a B z", 4));
    }
}
