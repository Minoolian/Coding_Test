package Target_Number;

class Solution {
    int answer = 0;

    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        
        return answer;
    }

    void dfs(int[] numbers, int target, int i, int result){
        if(i==numbers.length){
            if(target==result){
                answer++;
            }
            return;
        }

        dfs(numbers, target, i+1, result+numbers[i]);
        dfs(numbers, target, i+1, result-numbers[i]);

    }
}