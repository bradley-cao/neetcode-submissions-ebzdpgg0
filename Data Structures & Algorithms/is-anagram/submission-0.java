class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> sFreq = new HashMap<Character, Integer>();
        HashMap<Character, Integer> tFreq = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);
            if (sFreq.containsKey(letter)) {
                sFreq.put(letter, sFreq.get(letter) + 1);
            } else {
                sFreq.put(letter, 1);
            }
            letter = t.charAt(i);
            if (tFreq.containsKey(letter)) {
                tFreq.put(letter, tFreq.get(letter) + 1);
            } else {
                tFreq.put(letter, 1);
            }
        }
        for (Character letter : sFreq.keySet()) {
            if (!tFreq.containsKey(letter)) {
                return false;
            } else if (sFreq.get(letter) != tFreq.get(letter)) {
                return false;
            }
        }
        return true;
    }
}
