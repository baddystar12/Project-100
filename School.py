class School: 
    rooms = 100
    teachers = 30
    def updateTeachers(self):
        self.teachers+=10
        return self.teachers
    
    def updateRooms(self):
        self.rooms+=20
        return self.rooms
    
    def __init__(self, rooms, school_name):
       self.rooms = rooms
       self.school_name = school_name

    def Intro(self):
       print("Welcome to the {}".format(self.school_name))

school1 = School(100, "School of California")
school2 = School(150, "All Indian School")

school1.Intro()
school2.Intro()

teachers.updateTeachers()
rooms.updateRooms()
