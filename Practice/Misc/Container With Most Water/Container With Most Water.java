class Solution {
    public int maxArea(int[] height) {
        /*
            2 pointer approach
            start from start and end and keep checking the area of the container 
            if greater than current found replace it 
            move the ptr which has lesser value
        */

        int answer = 0;
        int n = height.length;

        int i=0,j = n-1;

        while(i < j) {
            int len = Math.min(height[i], height[j]);
            int width = j-i;
            answer = Math.max(answer, len*width);

            if(height[i] <= height[j]) {
                i++;
            } else {
                j--;
            }
        }

        return answer;
    }
}