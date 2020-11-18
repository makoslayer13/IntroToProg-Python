# -------------------------------------------------- #
# Title: Listing 9
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Timothy Quintana>,<11/15/2020>,Changed rows from lists to dictionaries
# -------------------------------------------------- #

# Declare my variables
strChoice = '' # User input
list_dic = []  # list of data
strFile = 'HomeInventory.txt'  # data storage file
objFile = None  # file handle

# Get user Input
while(True):
    print("Write or Read file data, then type 'Exit' to quit!")
    strChoice = input("Choose to [W]rite or [R]ead data: ")

    # Process the data
    if (strChoice.lower() == 'exit'): break
    elif (strChoice.lower() == 'w'):
        # List to File
        objFile = open(strFile, "w")
        list_dic = {"item": "Lamp", "value": "$30"}
        objFile.write(list_dic["item"] + "," + list_dic["value"] + "\n")
        list_dic = {"item": "End Table", "value": "$60"}
        objFile.write(list_dic["item"] + "," + list_dic["value"] + "\n")
        objFile.close()
    elif (strChoice.lower() == 'r'):
        # File to List
        objFile = open(strFile, "r")
        for row in objFile:
            listrow = row.split(",")
            list_dic = {"item": listrow[0], "value": listrow[1].strip()}
            print(list_dic)
        objFile.close()
    else:
        print('Please choose either W or R!')
