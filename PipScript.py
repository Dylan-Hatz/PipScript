from pip._internal import main as pipmain
import pip
import sys

def boolcheck(message):
    while True:
        value = input(message+'\n').lower()
        if value in ['y','yes']:
            return True
        elif value in ['n','no']:
            return False
        else:
            print('Please enter a valid choice(y, yes, n, or no)')
            continue

#upgrading pip
upgrade=boolcheck('Would you like to upgrade pip?')
if upgrade:
    modchoice = []
    if boolcheck('Would you like to add any modifiers?'):
        while True:
            modchoice.append(input('What modifier would you like?\n'))
            if not boolcheck('Would you like to add more modifiers?'):
                break
    piplist = ['install','pip','--upgrade']
    for item in modchoice:
        piplist.append(item)
    pipmain(piplist)
    print('\nPlease restart the script to continue')
    sys.exit()

#Custom download
while True:
    customchoice = input('Would you like guided install or custom?(type "g" or "c")\n').lower()
    if customchoice == 'g':
        break
    elif customchoice == "c":
        customcommand = input('Please type the pip command you would like to run\n')
        commandlist=customcommand.lower().split()
        print(commandlist)
        print(repr(commandlist[1]))
        while True:
            if commandlist[0] in ['python','python3','-m',]:
                print('bitch tits')
                commandlist.pop(0)
                continue
            elif commandlist[0] == 'pip':
                commandlist.pop(0)
                break
            else:
                break
        pipmain(commandlist)
        sys.exit()

while True:
    modulechoice = input('What module would you like to download?\n')
    confirmation = boolcheck('Is '+modulechoice+' the module that you wish to download?')
    if confirmation == True:
        break
#Condition desire check
exconfirm=boolcheck('Would you like to modify the installation?')
first = True
while exconfirm:
    if not first:
        exconfirm=boolcheck('Are there any other conditions to add?')
    ex = []
    #Modifier Requesting
    if exconfirm:
        ex.append(input('What modifier would you like to add?\n'))
        first = False
    else:
        break

#installing module
piplist = ['install',modulechoice]
for item in ex:
    piplist.append(item)
pipmain(piplist)
