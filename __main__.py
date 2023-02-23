from Admin import *
from datetime import datetime 
import sys

x = User()

# For Admin  Functionily Enter User Name as Admin and Password as Password


print("------------------------------------------->>>>  Welcome to India's No. 1 Flower Shoping App   <<<-------------------------------")
while True:
    print("*"*55)
    print("1. For Admin Functionilty")
    print("2. For User Functionilty")
    print("3. For Exit")
    print("*"*55)
    choise = input("Enter Your Choise Here :")

    if choise =="1":       
        while True:
            if x.admin_login()==True:
                print("-------------------------->>>>> Welcome to Admin Functionilty \n")
                print("+="*55)
                print("1. For Add New Flower ")
                print("2. For View Available Flower Stock")
                print("3. For View Availabe Flower Price")
                print("4. For Update Flower , Price or Stock ")
                print("0  For Exit ")
                print("+="*55)
                admin_sel = input("Select Your Choise :")

                if admin_sel =="1":
                    print(x.Add_New_flower())
                    break
                
                if admin_sel =="2":
                    print(x.Available_stock_flower())
                    break

                if admin_sel =="3":
                    print(x.view_flower_price())
                    break

                if admin_sel =="4":
                    print(x.Update_Flowers())
                                    
                else:
                    break
    
    elif choise =="2":
        while True:
            print("------------------------->>>>Welcome To User Funtionlity <<<--------------------------\n")
            print("+="*55)
            print("1. For User Login ")
            print("2. For User Registertion")
            print("3. For Buy Flower")
            print("4. For Profile Update")
            print("0. For Exit")
            print("+="*55)

            user_choise = input("Enter Your Selection :")

            if user_choise =="1":
                print(x.login())
            
            if user_choise =="2":
                print(x.Signing_into_app())
            
            if user_choise =="3":
                print(x.buy_flowre())
            
            if user_choise =="4":
                print(x.profile_update())
            
            else:
                break
    
    elif choise =="3":
        print()
        print("                         ⭐ ⭐ Thank For Using ⭐⭐                     ")
        sys.exit()
        

                


