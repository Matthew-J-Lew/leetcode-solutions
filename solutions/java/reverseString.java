class Solution {
    public void reverseString(char[] s) {
        
        int left = 0;
        int right = s.length - 1;
        char temp = 'a';

        while(left < right){

            temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            left = left + 1;
            right = right - 1;

        }

    }
}