"""
Helper file for our task
"""

class Helper:
    """
    Class that processes input data
    """
    def __init__(self):
        self.levels = {}

    def parseData(self):
        """
        Method that parses input data
        """
        file_path = "input.txt"
        with open(file_path, "r") as file:
            key = 0
            for level in file:
                level = level.replace(' ', ',')
                digits = []
                number = ""
                for digit in level:
                    if digit != ',':
                        number += digit
                    else:
                        digits.append(int(number))
                        number = ""
                digits.append(int(number))
                self.levels[key] = digits
                key += 1

    def getData(self):
        """
        Method that gets processed input data
        """
        self.parseData()
        return self.levels
    
if __name__ == "__main__":
    print(f"result={Helper().parseData()}")

