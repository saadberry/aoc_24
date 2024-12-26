"""
--- Day 1: Historian Hysteria ---
"""
from helper import Helper 

class Day1:
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
    
    def ComputeSimilarityScore(self):
        """
        Class that computes similarity scores
        Flow:
            - Fill a hash map of second list as: {'element': frequency}
            - Iterate through the first list, multiply the elements by their key in the hash map
            - Add that value to similarity_score
            - Return similarity_score
        """
        lists = Helper().get_lists()
        left, right = lists["left"], lists["right"]

        similarity_score = 0
        # Populating hash map
        h_map = {}
        for element in range(len(right)):
            if right[element] not in h_map:
                h_map[right[element]] = 1
            else:
                h_map[right[element]] += 1
        # Iterating first list
        for element in range(len(left)):
            # Add result of product of element with their key in the hash map
            similarity_score += left[element] * (h_map[left[element]] if left[element] in h_map else 0)
        return similarity_score
