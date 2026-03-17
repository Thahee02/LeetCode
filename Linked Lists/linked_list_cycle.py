class Solution(object):
    def hasCycle(self, head):
        list_slow = head
        list_fast = head

        while list_fast and list_fast.next:
            list_slow = list_slow.next
            list_fast = list_fast.next.next

            if list_slow == list_fast:
                return True
        
        return False