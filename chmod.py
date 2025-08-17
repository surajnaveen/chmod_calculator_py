Input_text = ''

def ChmodCalculator(text):
    try:
        string_text = str(text)
        splited_text = string_text.split(',')
        #print(len(splited_text))

        if len(splited_text)<=1:
            print("\n<__please Enter valid input__>")
    
    except:
        print("\n<__please Enter valid input__>")


while(Input_text.lower()!='exit'):
    print("\n__Welcome to chmod_calculator__\n\n--> This simple command line interface program help you to calculater linux chmod values easily")
    print("--> if you want to exit type \'Exit\' \n\n")
    print("--> Please enter the access fortmat \'rwx\' for \'Owner\',\'Group\',\'Other\'")
    print("Ex:- rwx,rw,r")
    print("--> make sure you have the write order: Owner, Group, other")
    print("Enter:-",end='')
    Input_text=input()

    ChmodCalculator(Input_text.lower())
