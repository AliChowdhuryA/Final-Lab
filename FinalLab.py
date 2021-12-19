import json
#start with a list, and append dictionaries provided by the user

#the function needs:
    # employee ID: 7 digit or less long, Req                                int
    # employee name: upper and lower class, Req                             string
    # email address: cannot contain !"'#$%^&*()=+,<>/?;:[]{}\). Req         string
    # employee address: cannot contain !"'@$%^&*_=+<>?;:[]{}), optional     string
    # employee salary: float variable between 18 and 27, req                float
#function will keep asking for employee information until
#user says they no longer wish to enter more users
#Also when a user enters improper data, the program
# must ask the user to re-enter it before continuing

#add "IT Department" to each name in the list
#update salary to be 30% higher

#print out list of updated information




illegalCharEmail = '!"#$%^&*()=+,<>/?;:[]{}\)'
illegalCharAddress = '!"\'@$%^&*_=+<>?;:[]{}),'

def IDcheck(strings):
    bool = False #initializes bool as our repeat condition
    while bool == False: #while bool is false, this code will keep running
        if len(strings) <=7 and strings.isnumeric(): #win condition
            bool = True #get closure on the function
            return strings
        else:
            #repeat process until conditions are met >:(
            strings = input("Please input an integer that has less than 7 digits: ")

def FullName(): # asks user for first and last name then returns first + last
    string1 = input("Input First Name: ")
    string2 = input("Input Last Name: ")
    return string1 + ' ' + string2

def HourlyWages(John): #John is float variable and will be checked if it is 18 < x < 27
    bool = False
    while bool == False:
        if John > 18.00 and John < 27.00:
            return float(John)
        else:
            John = float(input("Please input a float that is between 18 and 27: "))


def EmailCheck(eString):
    #check if illegal characters are not in eString
    bool = False
    while bool == False: #loop condition
        for i in eString: 
            if i in illegalCharEmail: #repeats loop if illegal character found
                eString = input("Please input an email address: ")

        return eString

def ITdept(futureITworker):
    return futureITworker + "," + " IT Department"

def AddressCheck(aString):
    if aString == "skip":
        return
    bool = False
    while bool == False: #loop condition
        for i in aString:       
            if i in illegalCharAddress: #repeats loop if illegal character found
                aString = input("Please input an email address: ")
            else: 
                return aString

def moneyRaise(oldmoney): #function to boost salary by 30%
    return oldmoney * 1.3

def appendDict():
    Employee_Dict = {"Empl_ID":[],"Empl_Name":[], "Employee_Email":[], "Employee_Address": [], "Employee_Salary": []}
    
    #initialize string variable and use IDcheck to get a number that is
    #less than 7 digits and is numeric
    strings= IDcheck(input("Input an integer that has less than 7 digits: "))  
    Employee_Dict["Empl_ID"] = int(strings) # put the strings in the dict

    strings = FullName()
    #adds strings to Dictionary
    Employee_Dict["Empl_Name"] = strings
    
    #adds words IT department to EmplName
    Employee_Dict["Empl_Name"] = ITdept(Employee_Dict["Empl_Name"])


    #takes input from user and calls HourlyWages function
    Employee_Dict["Employee_Salary"] = HourlyWages(float(input("Input a float that is between 18 and 27: ")))

    #takes the EmployeeSalary and multiplies by 1.3
    Employee_Dict["Employee_Salary"] = moneyRaise(Employee_Dict["Employee_Salary"])

     # email address: cannot contain !"'#$%^&*()=+,<>/?;:[]{}\). Req         string
    Employee_Dict["Employee_Email"] = EmailCheck(input("Input an email address: "))

    #address: cannot contain !"'@$%^&*_=+<>?;:[]{}), optional                string
    Employee_Dict["Employee_Address"] = AddressCheck(input("Input a street address (To skip this step, type \"skip\"): "))

    return Employee_Dict


def Choices():
    print(""" 
    1. Append dictionary to list
    2. print list
    n. stop
    """)

def printEmployees(EmplDicts):
    json_underPaid = json.dumps(EmplDicts, indent = 4)
    print(json_underPaid)

def main():

    input1 = '1'
    print("input your employees. ")
    EmployeeDictList= [] #List that holds employee dictionaries
    while input1 != 'n':
        Choices()
        input1 = input("1 to continue, n to stop: ")
        if input1 == "1":
           EmployeeDictList.append(appendDict())
        elif input1 == "2":
            printEmployees(EmployeeDictList)
        else:
            print("You chose to quit. Have a great day. Here is the list of current employees: ")
            break
        printEmployees(EmployeeDictList)

        
    

main()