class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head_node = ListNode(0)
        next_node = head_node
        while list1 and list2:
            if list1.val <= list2.val:
                next_node.next = list1
                list1 = list1.next
            else:
                next_node.next = list2
                list2 = list2.next
            next_node = next_node.next

        if list1:
            next_node.next = list1
        else:
            next_node.next = list2

        return head_node.next