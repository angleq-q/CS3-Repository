class Club:
    def __init__(self, name, adviser):
        self.name = name
        self.adviser = adviser
        self.members = []

    def add_member(self, member):
        self.members.append(member)

class Member:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level

    def attend_meeting(self, meeting):
        print(f"{self.name} attended {meeting}")

class Meeting:
    def __init__(self, date, venue):
        self.date =  date
        self.venue = venue
        self.attendees = []

    def record_attendance(self, members):
        self.attendees.append(members)

club1 =  Club("NeonGreen", "Mr.Ramos")
member1 = Member("Sebastian", "G9")
member2 = Member("Yohann", "G9")
member3 = Member("Jarabelo", "G9")

meeting1 = Meeting("September 16, 2026", "CS Lab 3")
club1.add_member(member1)
club1.add_member(member2)
club1.add_member(member3)

print(club1.members[0].name)
print(club1.members[0].attend_meeting(meeting1))