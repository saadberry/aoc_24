"""
File containing input for day 1
"""

class Helper:
    """
    Helper class for the question
    """

    def __init__(self):
        self.left, self.right = [], []

    def process_input(self):
        """
        Method that process input file
        """
        file_path = "input.txt"
        # Read the file
        with open(file_path, "r") as file:
            for line in file:
                if line.strip():
                    left, right = map(int, line.split())
                    self.left.append(left)
                    self.right.append(right)

    def get_lists(self):
        """
        Method that returns processed input data
        Returns:
            - <dict>: Dict of left and right lists
        """
        self.process_input()
        return {'left':self.left, 'right': self.right}



if __name__ == "__main__":
    helper = Helper()
    result = helper.process_input()
    output = helper.get_lists()
