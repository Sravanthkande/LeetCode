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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null){
            return null;
        }

        int count = 0;
        ListNode temp = head;

        while(temp != null){
            count += 1;
            temp = temp.next;
        }

        if(count == n){
            return head.next;
        }

        int res = count - n;
        temp = head;

        while(res > 1){
            res -= 1;
            temp = temp.next;
        }

        temp.next = temp.next.next;
        return head;
    }
}