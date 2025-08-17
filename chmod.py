Input_text = ''

#main menu
print("----------------------------------------------------------")
print("__Welcome to chmod_calculator__\n--> This simple CLI program help you to calculater linux chmod values easily")
print("--> Please enter the access fortmat \'rwx\' for \'Owner\',\'Group\',\'Other\'")
print("----------------------------------------------------------\n")

#calculation and validating function
def ChmodCalculator(text):
    try:
        string_text = str(text)
        splited_text = string_text.split(',')
        #print(len(splited_text))

        if not len(splited_text)==3:
            print("\n<<__please Enter valid input__>>\n")
            return
        
        chmod = [0,0,0]
        chmod_index = 0

        #calculation process
        for item in splited_text:
            for charecter in item:
                if 'r' in charecter:
                    chmod[chmod_index]+=4
                if 'w' in charecter:
                    chmod[chmod_index]+=2
                if 'x' in charecter:
                    chmod[chmod_index]+=1
            chmod_index+= 1
        
        for item in chmod:
            if item > 7:
                print("\n<__Something went wrong, Enter valid access permission__>\n")
                return
        
        print(f"\n<<__chmod value for \'{Input_text}\' is : {''.join( str(x) for x in chmod)} __>>")
        print(''.join( str(x) for x in chmod)+'\n')
        return

    except:
        print("\n<<__please Enter valid input__>>\n\n")


while(Input_text.lower()!='exit'):
    print("--> if you want to exit type \'Exit\'")
    print("--> make sure you have the write order: Owner, Group, other")
    print("Ex:- rwx,rw_,r__")
    print("Enter:-",end='')
    Input_text=input()

    chmod_value = ChmodCalculator(Input_text.lower())
