package com.programmers.java;
/*파이썬으로 풀 때는 알파벳과 숫자를 조합한 해시 자료구조를 이용해서 풀었는데
* 자바로 풀 때는 replaceAll이라는 라이브러리를 이용할 수 있음을 알게 되었다.
* 앞으로 구현을 파이썬만큼 쉽게 할 수 있도록 자주 문제를 풀어야겠다*/
// 프로그래머스 '숫자 문자열과 영단어' 문제, 레벨 1, 2021.10.07, 2일차
public class NumericStringsAndEnglishWords {
    public int solution(String s) {
        String answer = "";
        String[] alphabet = {"zero", "one", "two", "three", "four", "five", "six","seven", "eight", "nine"};
        String[] number = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

        for(int i = 0; i < alphabet.length; i++){
            // s에 있는 "one4seveneight"을 alphabet[]에 있는 영어단어와 비교하면서 매칭되는 숫자 문자열로 바꾸기
            s = s.replaceAll(alphabet[i], number[i]);
        }

        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        String s = "one4seveneight";
        NumericStringsAndEnglishWords problem = new NumericStringsAndEnglishWords();
        System.out.println(problem.solution(s));
    }
}
