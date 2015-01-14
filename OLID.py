import OpenDental
import time
import sys


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


print "OpenDental Login Identity Deceptor (OLID) - By: Will Cipriano"
print "Attempting to connect to database... Please Wait"
if (OpenDental.DatabaseConnection()):
    print "Connection Successful"
else:
        print "database connection failed"
        time.sleep(60)
        sys.exit(False)

print "What would you like to do today?"
print "1: Create User"
selected = False
while (selected == False):
    selection = raw_input('?:')
    print selection
    if (selection == '1'):
        createuser()
        selected = True
    else:
        print "invalid input!"
