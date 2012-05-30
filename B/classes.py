# File Name: classes.py


class Staff:
    ''' super class Staff '''

    def __init__(self, newStaffID, newName, newEmployeeType):
        ''' constructor for Staff '''
        self.__StaffID      = newStaffID
        self.__Name         = newName
        self.__EmployeeType = newEmployeeType

    def getStaffID(self):
        ''' accessor for StaffID '''
        return self.__StaffID

    def getName(self):
        ''' accessor for Name '''
        return self.__Name

    def getEmployeeType(self):
        ''' accessor for EmployeeType '''
        return self.__EmployeeType

    def setName(self, newName):
        ''' modifier for name '''
        self.__Name = newName

    def setEmployeeType(self, newEmployeeType):
        ''' modifier for EmployeeType '''
        self.__EmployeeType = newEmployeeType

    def display(self):
        ''' helper for displaying Staff info '''
        print("StaffID: " + str(self.__StaffID))
        print("Name: " + str(self.__Name))
        print("Employee Type: " + str(self.__EmployeeType))
        print()

        
class TeachingStaff(Staff):
    ''' subclass of staff: teachingstaff '''
    
    def __init__(self, newStaffID, newName, newEmployeeType, newCourseCode1, newCourseCode2, newCourseCode3):
        ''' constructor for TeachingStaff '''
        super().__init__(newStaffID, newName, newEmployeeType)
        self.__CourseCode1 = newCourseCode1
        self.__CourseCode2 = newCourseCode2
        self.__CourseCode3 = newCourseCode3

    def getCourseCode1(self):
        ''' accessor for CourseCode1 '''
        return self.__CourseCode1

    def getCourseCode2(self):
        ''' accessor for CourseCode2 '''
        return self.__CourseCode2

    def getCourseCode3(self):
        ''' accessor for CourseCode3 '''
        return self.__CourseCode3

    def setCourseCode1(self, newCourseCode1):
        ''' modifier for CourseCode2 '''
        self.__CourseCode1 = newCourseCode1

    def setCourseCode2(self, newCourseCode2):
        ''' modifier for CourseCode2 '''
        self.__CourseCode2 = newCourseCode2

    def setCourseCode3(self, newCourseCode3):
        ''' modifier for CourseCode3 '''
        self.__CourseCode3 = newCourseCode3

    def display(self):
        ''' helper for displaying TeachingStaff info '''
        super().display()
        print("Course code 1: " + str(self.__CourseCode1))
        print("Course code 2: " + str(self.__CourseCode2))
        print("Course code 3: " + str(self.__CourseCode3))
        print()



class SupportStaff(Staff):
    ''' subclass of staff: SupportStaff '''
    
    def __init__(self, newStaffID, newName, newEmployeeType, newCourseCode1, newCourseCode2, newSubjectArea):
        ''' constructor for SupportStaff '''
        super().__init__(newStaffID, newName, newEmployeeType)
        self.__CourseCode1 = newCourseCode1
        self.__CourseCode2 = newCourseCode2
        self.__SubjectArea = newSubjectArea

    def getCourseCode1(self):
        ''' accessor for CourseCode1 '''
        return self.__CourseCode1

    def getCourseCode2(self):
        ''' accessor for CourseCode2 '''
        return self.__CourseCode2

    def getSubjectArea(self):
        ''' accessor for SubjectArea '''
        return self.__SubjectArea

    def setCourseCode1(self, newCourseCode1):
        ''' modifier for CourseCode1 '''
        self.__CourseCode1 = newCourseCode1

    def setCourseCode2(self, newCourseCode2):
        ''' modifier for CourseCode2 '''
        self.__CourseCode2 = newCourseCode2

    def setSubjectArea(self, newSubjectArea):
        ''' modifier for SubjectArea '''
        self.__SubjectArea = newSubjectArea

    def display(self):
        ''' helper for displaying SupportStaff info '''
        super().display()
        print("Course code 1: " + str(self.__CourseCode1))
        print("Course code 2: " + str(self.__CourseCode2))
        print("Subject area: " + str(self.__SubjectArea))
        print()

