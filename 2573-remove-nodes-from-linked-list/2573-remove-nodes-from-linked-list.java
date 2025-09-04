/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNodes(ListNode head) {
        Stack<ListNode> stack = new Stack<>();
        ListNode curr = head;

        while(curr != null){
            while(!stack.isEmpty() && stack.peek().val < curr.val){
                stack.pop();
            }

            stack.push(curr);
            curr = curr.next;
        }

        ListNode newHead = null;
        if(!stack.isEmpty()){
            newHead = stack.firstElement();
        }

        for(int i = 0; i < stack.size() -1; i++){
            stack.get(i).next = stack.get(i+1);
        }
        stack.peek().next = null;

        return newHead;
    }
}