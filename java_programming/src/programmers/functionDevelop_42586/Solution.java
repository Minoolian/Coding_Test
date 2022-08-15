package programmers.functionDevelop_42586;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public static int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();

        // 첫번째 요소의 남은 작업 일수
        double wait_days = Math.ceil((100 - progresses[0]) / (double) speeds[0]);
        // 한번에 반환하는 작업 개수
        int work=1;
        // 두번째 요소부터 작업을 확인한다.
        for (int i = 1; i < progresses.length; i++) {
            //남은 작업 일수
            double days = Math.ceil((100 - progresses[i]) / (float) speeds[i]);

            // 가장 오래걸리는 작업 일수(wait_days)와 현재 작업의 작업 일수 비교
            // 가장 오래걸리는 작업보다 더 오래 걸리면
            if (days > wait_days) {
                // 가장 오래 걸리는 작업을 현재 작업으로 변경
                wait_days = days;
                // 현재까지의 작업 개수를 리스트에 추가
                answer.add(work);
                // 작업 개수를 1개로 초기화
                work=1;
                continue;
            }

            // 가장 오래걸리는 작업보다 덜 걸리면 기다려야 하므로 작업 개수 추가
            work++;
        }
        
        // 가장 마지막에 남은 작업 개수를 리스트에 추가
        answer.add(work);

        return answer.stream().mapToInt(i->i).toArray();
    }
}