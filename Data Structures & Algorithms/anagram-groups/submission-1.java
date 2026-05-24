
class Solution {
    public boolean checkAnagram(String string1, String string2) {
        if(string1.length()!=string2.length()) {
            return false;
        }

        int[] characters = new int[26];
        for(int i=0; i<string1.length(); i++) {
            characters[string1.charAt(i) - 'a']++;
            characters[string2.charAt(i) - 'a']--;
        }
        for(int i=0; i<characters.length; i++) {
            if(characters[i]!=0) {
                return false;
            }
        }
        return true;
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> map = new HashMap<>();
        for(int i=0; i<strs.length; i++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);

            if(!map.containsKey(sorted)) {
                map.put(sorted, new ArrayList<>());
            }

            map.get(sorted).add(strs[i]);
        }
        return new ArrayList<>(map.values());
    }
}
