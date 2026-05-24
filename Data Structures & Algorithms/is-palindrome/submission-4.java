class Solution {
    public boolean isPalindrome(String s) {
        String n = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        for(int i=0; i<n.length()/2; i++) {
            if(n.charAt(i) != n.charAt(n.length() - i - 1)) {
                return false;
            }
        }
        return true; 
    }
}
