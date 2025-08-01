class Solution {
    private void generate(int open, int close, int n, String cur, List<String> res) {
        if(open == close && open + close == 2*n){
            res.add(cur);
            return;
        }

        if(open < n){
            generate(open + 1, close, n, cur+'(', res);
        }

        if(close < open){
            generate(open, close + 1, n, cur+')', res);
        }
    }
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        generate(0, 0, n, "", res);
        return res;
    }
}