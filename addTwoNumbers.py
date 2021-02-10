class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):

    carry = 0
    dummy = ListNode(0)
    p = dummy

    while l1 or l2:
        p.next = ListNode((l1.val+l2.val+carry)%10)
        carry = ((l1.val+l2.val)//10)
        l1 = l1.next
        l2 = l2.next
        p = p.next

    return dummy.next


a = [2,4,3]
b = [5,6,4]
print(addTwoNumbers(a,b))