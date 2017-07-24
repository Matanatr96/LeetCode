class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        cur, carry = head, 0
        while l1 or l2:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            temp, carry = temp % 10, temp / 10
            cur.next = ListNode(temp)
            cur = cur.next
            
        if carry == 1:
            cur.next = ListNode(1)
        return head.next