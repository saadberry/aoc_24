"""
--- Day 2: Red-Nosed Reports ---
"""
from helper import Helper


class RedNosedReports:
    """
    Class that helps the Red-Nosed Reindeer nuclear fusion/fission plant engineers analyze their data
    """
    def __init__(self):
        # self.levels = {
        #     1: [7, 6, 4, 2, 1],
        #     2: [1, 2, 7, 8, 9],
        #     3: [9, 7, 6, 2, 1],
        #     4: [1, 3, 2, 4, 5],
        #     5: [8, 6, 4, 4, 1],
        #     6: [1, 3, 6, 7, 9],
        # }
        # pass
        self.levels = Helper().getData()

    def validateReports(self):
        """
        Method that validates reports
        The following validation is done:
            1. Data should not be neither an increase or decrease
            2. Difference between adjacent levels should not be more than 3
            3. Status of levels should be consistent
        """
        # If delta is neither an increase or decrease
        if self.delta == 0:
            self.flag = 1
        # Compute status for the first two levels
        if not self.status:
            self.status = "increasing" if self.delta < 0 else "decreasing"
        next_status = "increasing" if self.status and  self.delta < 0 else "decreasing"
        # Status of levels should be consistent
        if next_status != self.status:
            self.flag = 1
        # If difference is more than 3
        if abs(self.delta) > 3:
            self.flag = 1

    def AnalyzeReports(self):
        """
        Method that computes how many reports are safe
        Returns:
            - num_safe <int>: Number of levels that are safe
        Flow:
            - Iterate dict (using two pointers?)
            - Compare delta(R,L). If delta > 3 || delta == 0: mark level unsafe
            - To ensure consistent direction of level change (only increase/decrease)
                 * Use a variable "status" and assign it if it is increasing/decreasing, 
                 * For every subsequent level, compute status and assign it to a temp var
                 * Compare temp var with status, if they at any point do not match - mark level unsafe
            - If we have reached the end of iteration, increment num_safe by 1.
        """
        num_safe = 0
        for _, report in self.levels.items():
            self.flag = 0
            self.status = None
            l, r = 0, 1
            c = 0
            while r < len(report):
                self.delta = report[l] - report[r]
                # Validate reports
                self.validateReports()
                r += 1
                l += 1
            if self.flag != 1:
                num_safe += 1

        return num_safe

if __name__ == "__main__":
    rnr = RedNosedReports()
    print(f'result={rnr.AnalyzeReports()}')