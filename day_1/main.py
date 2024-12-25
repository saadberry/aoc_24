"""
--- Day 1: Historian Hysteria ---
"""
from helper import Helper 

class ReconcileLists:
    """
    Class that reconciles lists for the historians 
    """
    def reconcile(self):
        """
        Flow:
            - Sort lists
            - Compute difference of respective elements in both lists
            - Add that value to sum
            - Return sum of elements
        """
        lists = Helper().get_lists()
        left, right = lists["left"], lists["right"]
        left.sort()
        right.sort()
        sum = 0
        i = 0
        while i < len(right):
            sum += abs(left[i] - right[i])
            i += 1
        return sum

if __name__ == "__main__":
    print(f"total distance = {ReconcileLists().reconcile()}")