Input_text = ''

def ChmodCalculator(text):
    try:
        string_text = str(text)
        splited_text = string_text.split(',')
        #print(len(splited_text))

        if not len(splited_text)==3:
            print("\n<__please Enter valid input__>")
            return

    except:
        print("\n<<__please Enter valid input__>>\n\n")


while(Input_text.lower()!='exit'):
    print("----------------------------------------------------------")
    print("__Welcome to chmod_calculator__\n--> This simple CLI program help you to calculater linux chmod values easily")
    print("--> if you want to exit type \'Exit\' \n")
    print("--> Please enter the access fortmat \'rwx\' for \'Owner\',\'Group\',\'Other\'")
    print("Ex:- rwx,rw_,r__")
    print("--> make sure you have the write order: Owner, Group, other")
    print("Enter:-",end='')
    Input_text=input()

    ChmodCalculator(Input_text.lower())
