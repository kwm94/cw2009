# File Name: cwa1a.py


import datetime
import re
import os

def CREATESTAFF():
    ''' module allowing for entry of new staff,
        and writes staff data to text file STAFF.DAT'''
    
    try:
        # if STAFF.DAT exists then it will be created.
        if os.path.exists("STAFF.DAT"):
            print("STAFF.DAT exists. It will be overwritten.")
            StaffFile = open("STAFF.DAT","w")
        else:
            StaffFile = open("STAFF.DAT","w")
            print("Text file STAFF.DAT created.")
        

        # get LastUpdateDate from system
        LastUpdateDate = datetime.datetime.today().strftime("%d-%m-%Y")

        # get and validate NumberOfRecords
        ValidNumberOfRecords = False
        while not ValidNumberOfRecords:
            NumberOfRecords = input("Enter number of records: ")
            if not NumberOfRecords.isdigit():
                print("Number of records must be in digits.")
            else:
                ValidNumberOfRecords = True

        # write first line (LastUpdateDate and NumberOfRecords) to file STAFF.DAT
        StaffFile.write(LastUpdateDate + str(NumberOfRecords) + "\n")

        # loop for each record to be added
        for i in range(0, int(NumberOfRecords)):
            
            # get and validate StaffID
            ValidStaffID = False
            while not ValidStaffID:
                StaffID = input("Enter Staff ID: ")
                   
                # presence check
                if len(StaffID) == 0:
                    print("Empty input.")
                
                # Implement length check for StaffID.
                elif len(StaffID) != 5: 
                    print("StaffID must be exactly 5 characters")

                # Implement type check
                elif not StaffID.isdigit():
                    print("StaffID should be in all digits.")

                # Implement gender check for StaffID.
                elif not (StaffID[0:1] == "1" or StaffID[0:1] == "2"):
                    print("Invalid gender. 1st character should be 1 (Male) or 2 (Female)") 

                # Implement range of staff number for StaffID
                elif not 0 < int(StaffID[3:5]) < 100:
                    print("Invalid staff number. Last 2 numbers should be between 1 and 99 inclusive")

                else:
                    # Implement year of starting college for StaffID.
                    YearStart = int(StaffID[1:3])
                    YearCurrent = int(datetime.datetime.today().strftime("%y"))
                    
                    if not 8 <= YearStart <= YearCurrent:
                        print("Year should be within year 2008 and the current year.")
                    else:
                        ValidStaffID = True

            # Give the regular expression to validate Name.
            NamePattern = re.compile("[.a-zA-Z ]")
            ValidName = False
            while not ValidName:
                Name = input("Enter name: ")
                if len(Name) == 0:
                    print("Empty input.")
                elif not len(Name) < 35:
                    print("Name is maximum 35 characters long")
                elif not NamePattern.match(Name):
                    print("Name can only consist of letters and spaces.")
                else:
                    ValidName = True

            # Give the regular expression to validate EmployeeType.
            EmployeeTypePattern = re.compile("[stST]")
            ValidEmployeeType = False
            while not ValidEmployeeType:
                EmployeeType = input("Enter Employee Type: ")
                if len(EmployeeType) == 0:
                    print("Empty input.")
                elif len(EmployeeType) != 1:
                    print("Employee type should be exactly 1 character.")
                elif not EmployeeTypePattern.match(EmployeeType):
                    print("Employee type should only be T (Teaching Staff) or S (Support Staff).")
                else:
                    ValidEmployeeType = True
                    EmployeeType = EmployeeType.upper()

            # write record to STAFF.DAT
            StaffFile.write("{0:5s}{1:35s}{2:1s}\n".format(str(StaffID), str(Name), str(EmployeeType)))

        # close file.
        StaffFile.close()

    # handling file input/output errors
    except IOError:
        print("Error reading from / writing to file")




# main
if __name__ == "__main__":
    CREATESTAFF()











