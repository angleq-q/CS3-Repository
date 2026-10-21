class Students:

    def __init__(self, name, section, score):
        self.name = name
        self.section = section
        self.score = score

    def display_info(self):
        print("Name: ",self.name)
        print("Section: ",self.section)
        print("Score: ",self.score)
        print("Pass/Fail", self.check_status())

    def check_status(self):
        if self.score >= 50:
            return "passed"
        else:
            return "failed"

