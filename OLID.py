import OpenDental
import time
import sys

def manual():

    def yorn(data):
        if data == 'Y' or data == 'y':
            return True
        elif data == 'N' or data == 'n':
            return False
        else:
            print 'Invalid Input!'
            return False

    print "Attempt to load previously saved configuration?"
    check = raw_input('Y/N?')
    if yorn(check):
        if OpenDental.DatabaseConnection():
            return True


    def write(host, username, password, database, path):
        try:
            f = open(path, 'w')
            f.write('Host = ' + host + '\nUsername = ' + username + '\nPassword = ' + password + '\nDatabase = ' + database)
            f.close()
            return True
        except Exception as ex:
            return False

    print "Please enter OpenDental database details."
    host = raw_input('Host?:')
    username = raw_input('Username?')
    password = raw_input('Password?')
    database = raw_input('Database?')
    print "Save this configuration?"
    save = raw_input('Y/N?')
    if yorn(save):
        import os
        path = os.path.dirname(__file__).replace('\\library.zip', "")
        path += '\OpenDentalDatabaseConfig.ini'
        if os.path.isfile(path):
            print "configuration already exists! Overwrite?"
            overwrite = raw_input('Y/N?')
            if yorn(overwrite):
                if write(host ,username ,password ,database, path):
                    print "Parameters updated successfully."
                else:
                    print "Save failed."
        else:
            if write(host ,username ,password ,database, path):
                print "Data saved."
            else:
                print "Save failed"

    else:
        print "Data not saved."


    print 'Attempting to connect to database'
    if OpenDental.DefineDatabase(host, username, password, database):
        print "connection successful"
        return True
    else:
        print "connection failed!"
        return False


def createuser():
    print "New User Wizard"
    username = raw_input('Username:')
    usernum = int(raw_input('Number (must be unique):'))
    usergroup = int(raw_input('User group (normally 1 for Admin):'))
    useremp = int(raw_input('Employee number (0 for none):'))
    userclinic = int(raw_input('Clinic number:'))
    userprovider = int(raw_input('Provider number:'))
    userishidden = int(raw_input('Is user hidden?(0 = no, 1 = yes):'))
    userpopups = int(raw_input('Show popups?(0 = no, 1 = yes):'))
    userpassword = int(raw_input('Password Strength(0 = weak, 1 = strong):'))
    userclinicrestrictions = int(raw_input('User is restricted to own clinic(0 = no, 1 = yes):'))
    print "Creating User"
    x = OpenDental.CreateUser(number=usernum,name=username,group=usergroup,employee=useremp,clinic=userclinic,provider=userprovider,hidden=userishidden,popups=userpopups,password=userpassword,restricted=userclinicrestrictions)
    if (x):
        print "user created successfully"
        time.sleep(10)
        sys.exit(True)
    else:
        print "user failed to be created!"
        time.sleep(60)
        sys.exit(False)

def deleteattachedclaims():
    print "Claim Delete Wizard"
    procedurenumber = raw_input('Procedure Number:')
    confirm = raw_input('Are you sure you want to delete all claims attached to ' + str(procedurenumber) + '? Y/N')
    if (confirm == 'Y' or confirm == 'y'):
        if (OpenDental.deleteattachedclaims(procedurenumber)):
            print "claim deleted."
        else:
            print "claim deletion failed."

def patientsearch():
    x = True
    while x:
        search = raw_input("Patient Search: ")
        patients = OpenDental.patientnamesearch(search)
        if patients == False:
            print 'Patient not found!'
        else:
            Y = 0
            while Y < len(patients):
                patientdata = OpenDental.GetPatientDetails(patients[Y]['PatNum'])
                if patientdata['LastName'] == False:
                    patientdata['LastName'] = 'None'
                if patientdata['FirstName'] == False:
                    patientdata['FirstName'] = 'None'
                try:
                    print str(patients[Y]['PatNum']) + ": " + str(patientdata['FirstName']) + " " + str(patientdata['LastName'])
                except Exception as ex:
                    print ex
                Y += 1



manual()
print "What would you like to do today?"
print "1: Create User"
print "2: Delete Attached Claims"
print "3: Patient Search"
selected = False
while (selected == False):
    selection = raw_input('?:')
    print selection
    if (selection == '1'):
        createuser()
        selected = True
    elif (selection == '2'):
        deleteattachedclaims()
        selected = True
    elif (selection == '3'):
        patientsearch()
        selected = True
    else:
        print "invalid input!"
