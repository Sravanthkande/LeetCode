class Solution {
    public boolean isValid(String word) {
        if(word.length() < 3){
            return false;
        }

        int vowels = 0;
        int consonants = 0;
        String vowelSet = "aeiouAEIOU";

        for(char c : word.toCharArray()) {
            if (Character.isAlphabetic(c)){
                if(vowelSet.indexOf(c) != -1){
                    vowels++;
                }else{
                    consonants++;
                }
            }else if(!Character.isDigit(c)){
                return false;
            }
        }

        return vowels >= 1 && consonants >= 1;
    }
}