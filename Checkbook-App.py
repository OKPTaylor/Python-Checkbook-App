import json
import datetime



with open("user_data_timestamp.json", 'r') as f:  
    userBalance = json.load(f)


def currentBalance(userBalance):
   print(f"\nYour current balance is: ${round(sum(list(userBalance.values())) , 2)}")

def history(userBalance):
    with open("user_data_timestamp.json" , 'w') as f:
        json.dump(userBalance,f) 

    print(f"\nThis is your transaction history for your last {len(userBalance)} transactions.\n")
    for a, b in userBalance.items():
        print(f"{a} ${b}")   

def withdraw(userBalance):
    userInput = ""
    x = datetime.datetime.now()
    while userInput != userInput.isdigit():
        userInput=input("How much would you like to withdraw? $") 
        if userInput.isalpha():
            print("\nSorry you must enter numbers only.\n")
            
        else:
            userInput=-1*float(userInput)
            userBalance.update({x.strftime("%b-" "%d-" "%Y" " %I:" "%M:" "%S" " %p"): userInput})
            break  

          
    print(f"\nYour new blance is: ${round(sum(list(userBalance.values())) , 2)}")
    
    with open("user_data_timestamp.json", 'w') as f:
        json.dump(userBalance,f)      
        
        

def deposit(userBalance):
    userInput = ""
    x = datetime.datetime.now()
    while userInput != userInput.isdigit():
        
        userInput=input("How much would you like to deposit? $") 
        if userInput.isalpha():

            print("\nSorry, you must enter numbers only.\n")
            
        else:
            userInput=float(userInput)
            userBalance.update({x.strftime("%b-" "%d-" "%Y" " %I:" "%M:" "%S" " %p"): userInput})
            break   
              
    print(f"\nYour new blance is: ${round(sum(list(userBalance.values())) , 2)}")

    with open("user_data_timestamp.json", 'w') as f:
        json.dump(userBalance,f)      
        

userReply = ""
while userReply != "5":
    print("""\n~~~ Welcome to your terminal checkbook! ~~~\n
    What would you like to do?
    
    1) view current balance 
    2) record a debit (withdraw) 
    3) record a credit (depost) 
    4) transaction history
    5) exit\n""") 

    userReply = input("Your choice? ")

    if userReply == "1":
        currentBalance(userBalance)
    elif userReply == "2":
        withdraw(userBalance)
    elif userReply == "3":
        deposit(userBalance)
    elif userReply == "4":
        history(userBalance)        
    elif userReply == "5":
        print("\nHave a nice day.\n")  
    else:
        print("\nSorry invalid choice.") 