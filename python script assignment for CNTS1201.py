def main():
    import os
    import pathlib

    def GetState():
        name = input("What is your state's name? :  ")
        return name;


    def FormatState(userState):
        if len(userState) < 8:
            newState = userState.ljust(8, '*')
            return newState;
        else:
            return userState;
    
    print()
    print("Here is the list of avalible tasks: ")
    print("1. Get information and display to screen" )
    print("2. Call user created functions" )
    print("3. Write list of files to file" )
    print("4. Read specified file" )
    print()
    menuitem=input("Enter the number of the task you want to do: ")
    if menuitem == "1" :
        companyName = "Dunwoody College"
        programName = "Computer Networking"
        uName = os.environ['USERNAME']
        classFirst=input("Enter the name of you first class: ")
        classSecond=input("Enter the name if you second class: ")
        print("Logged on as",uName, "at",companyName, "in department: ",programName)

    elif menuitem == "2" :
        state = GetState()
        newState = FormatState(state)
        print("The old state is " + state + " and the new state is " + newState)

    elif menuitem == "3" :
        filename = input("Enther the name of file to save to  ")
        fList = []
        for p in pathlib.Path('.').iterdir():
            if p.is_file():
                fList.append(p)
        with open(filename, "w") as myFileWrite:
            myFileWrite.write("These are my files:\n")
            for f in fList:
                myFileWrite.write(f.name)
                myFileWrite.write("\n")
    elif menuitem == "4" :
        filename = input("Name a file to read  ")
        with open(filename, "r+") as myFileRead:
            print(myFileRead.read())
