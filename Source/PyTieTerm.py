import os

termon = True

os.system('clear')
print("   |\---/| \n   | ,_, |\n    \_w_/-..----.\n ___/ `   ' ,""+ \  BC\n(__...'   __\    |`.___.';\n  (_,...'(_,.`__)/'.....+\n\n Welcome to PyTie_TERMON Nya~ \n PyTie_TERMON, Better known as TERMON is a use friendly command prompt powered terminal, made in python\n by a guy with no coding expirience in python...\n Im BoxCat the terminals mascot. i like to run things around here \n Type help for help NOTE: TERMON is CASE SENSITIVE meaning commands need to be the exact capitalization as displayed!\n\n")

def CBP(reason):
        BSODerror = reason
        print("\n \nCALLBACKPING")
        print("  ,-.       _,---._ __  / \ \n /  )    .-'       `./ /   \ \n(  (   ,'            `/    /|                         \n  `.              ,  \ \ /  | \n   /`.          ,'-`----Y   | \n  (            ;        |   ' \n  |  ,-.    ,-'         |  / \n  |  | (   |    oops... | / \n  )  |  \  `.___________|/ \n  `--'   `--') \n \n Apparently, the terminal ran into a problem... thats not good\n this would be where we would collect data. but we dont at the moment, see reason for crash below \n \n")
        print("🠇🠇🠇 Reason 🠇🠇🠇\n")
        print(BSODerror)
        print("\n🠅🠅🠅 Reason 🠅🠅🠅")
        exit()

while True:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cmd = input("C:/user/PyTie.exe : ")
    if cmd == "help":
        print("TERMON_PyTie is CASE SENSITIVE!!!!!!!! \n \n help - Displays all commands \n")
    
    elif cmd == "dir":
        print("Displaying directorys and files...\n \n")
        directory = dir_path
        directorys = os.path.dirname
        for root, dirs, files in os.walk(directory):
            for subFile in files:
                print (os.path.join(root, subFile, directorys))

    elif cmd == "cd ..":
        CBP("ERR_KEEP_UP")

    elif cmd == "mkfile":
        print("This feature is currently in development, please wait for it to be released \n")
        CBP("ERR_KEEP_UP")
#        print("This feature is currently in development, please wait for it to be released")
#        print("Welcome to MKFile (make file) function which makes a text file. \n \n lets make a new file. first select a name")
#        Filename = "/workspaces/PieTie_Python_Terminal/Source/text.txt".join((input("Enter a name: ")))
#        Content = input("now lets insert some data. type it here: ")
#        filemake = open(Filename, "x")
#        filething = open(Filename)
#        filemake.write(Content)
#        f = open(Filename, "r")
#        print(f.read())

        # Method 1
#f = open("Path/To/Your/File.txt", "w")   # 'r' for reading and 'w' for writing
#f.write("Hello World from " + f.name)    # Write inside file 
#f.close()                                # Close file 

# Method 2
#with open("Path/To/Your/File.txt", "w") as f:   # Opens file and casts as f 
#    f.write("Hello World form " + f.name)       # Writing
    # File closed automatically


    elif cmd == "readfile":
        
        fileopen = open(input("File.. with dir eg /workspaces/PieTie_Python_Terminal/Source/File.txt   : "), "r")
        print(fileopen.read())

    elif cmd == "Cls":
        print("Clearing screen...")
        os.system('clear')

    elif cmd == "callbackping":
        CBP(input("Reason: "))

    elif cmd == "errdisplay":
        print("ERR_KEEP_UP\n   This error means that this feature is either depricated, or not finished.\n to stop any errors out of development we use a CBP to replace the function to make sure the TERMINAL isnt effected.")

    elif cmd == "":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")
    elif cmd == "":
        print("")