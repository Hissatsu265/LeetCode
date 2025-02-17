import heapq

# Định nghĩa danh sách liên kết đơn
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        
        # Đưa các node đầu tiên của mỗi danh sách vào heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))  # Sử dụng tuple để tránh lỗi so sánh

        dummy = ListNode(0)  # Node giả để bắt đầu danh sách kết quả
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)  # Lấy node nhỏ nhất
            current.next = node
            current = node
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))  # Thêm node tiếp theo vào heap

        return dummy.next  # Trả về danh sách kết quả
