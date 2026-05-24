class Solution {

    public String encode(List<String> strs) {
        String str = "";
        for(int i=0; i<strs.size(); i++) {
            String num = String.valueOf(strs.get(i).length());
            if(i==strs.size()-1) {
                str = str + num + "#" + strs.get(i);
            }
            else {
                str = str + num + "#" + strs.get(i);
            }
        }
        return str;
    }

public List<String> decode(String str) {
    List<String> result = new ArrayList<>();
    int i = 0;
    while (i < str.length()) {
        int j = i;
        while (str.charAt(j) != '#') j++;
        int len = Integer.parseInt(str.substring(i, j));
        result.add(str.substring(j + 1, j + 1 + len));
        i = j + 1 + len;
    }
    return result;
}
        
}
