# File Name: cwb1.py



import datetime
import os


def DISPLAYSTAFF():
    ''' Module which will read the data from text file STAFF.DAT and
        output staff details.'''
    try:
        # checking if STAFF.DAT exists
        if not os.path.exists("STAFF.DAT"):
            print("Text file STAFF.DAT does not exist.")

        # if file exists
        else:
            # open STAFF.DAT for reading
            StaffFile = open("STAFF.DAT", "r")

            # get LastUpdateDate and number of records (first line)
            FirstLine = StaffFile.readline()
            LastUpdateDate = datetime.datetime.strptime(FirstLine[0:10], "%d-%m-%Y")
            LastUpdateDate = LastUpdateDate.strftime("%y%m%d")
            NumberOfRecords = FirstLine[10:-1]

            # output LastUpdateDate and number of records
            print("Last update: " + LastUpdateDate)
            print("#Records:    " + NumberOfRecords)

            # output heading
            print("{0:10s}{1:36s}{2:15s}".format("StaffID", "Name", "Employee Type"))
            print("-" * 60)

            # for each record in STAFF.DAT
            for record in StaffFile.readlines():
                StaffID = record[0:5]
                Name = record[5:40]
                EmployeeType = record[40:41]
                if record[40:41] == "S":
                    EmployeeType = "Support"
                else:
                    EmployeeType = "Teacher"

                # output record details
                print("{0:10s}{1:36s}{2:15s}".format(StaffID, Name, EmployeeType))

            # close file
            StaffFile.close()
            
    # handle file input errors
    except IOError:
        print("Error reading from file.")



# main
if __name__ == "__main__":
    DISPLAYSTAFF()
