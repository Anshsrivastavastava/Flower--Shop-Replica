import sys
import json

class Admin:
    def __init__(self) :
        self.category = {}
        self.flowers = {}
        self.cate_len = len(self.category)+1
        self.flower_len = len(self.flowers)+1



    def Add_New_flower(self):
        print()
        nos_cag = input("Enter How Many Flowers You Want to Add :")
        for i in range(1,int(nos_cag)+1):
            print()
            flower_name = input(f"Enter Your {i} Flower Name Here:")
            Prices = input(f"Enter Your \per {flower_name} Flower Price  Here :")
            Stock_left = int(input(f"Enter How Many Stocks Are Having for {flower_name} flowers :"))
            d = {"Flower Name":flower_name,"Prices":Prices,"Available Stocks":Stock_left}
            self.category[self.cate_len] = d
            self.cate_len = len(self.category)+1
        with open("Flowers.json","w") as f:
            json.dump(self.category,f,indent=4)
        return "Your Flower Got Added Sucess Fully"

    def view_flower_price(self):
        with open("Flowers.json","r")as f:
            self.temp = json.load(f)
            print()
            print("----------------------------------------------->>>>>    Flowers and His Price    <<<---------------------------------------------------\n")
        i = 1
        for  j  in self.temp.values():
            print({i},j["Flower Name"],"                                   :                                  ",j["Prices"])
            i+=1
        return ""
    
    def admin_login(self):
        user_name = input("Enter Your User Name :")
        passw = input("Enter Your Password :")
        if user_name =="Admin":
            if passw =="Password":
                return True
            return "Invalid Password"
        return "Invalid User Name"

    def Available_stock_flower(self):
        with open("Flowers.json","r")as f:
            temp = json.load(f)
            print()
            print("----------------------------------------------->>>>>    Flowers and  His Available Stocks Are    <<<---------------------------------------\n")
        i = 1
        for  j  in temp.values():
            print({i},j["Flower Name"],"                                   :                                  ",str(j["Available Stocks"])+" pices")
            i+=1
        return ""
    
    def Update_Flowers(self):
        with open("Flowers.json","r")as f:
            temp = json.load(f)
        while True:
            print("+="*15)
            print("Press  1 for Updation ")
            print("+="*15)
            choise = input("Select Your Choise :")
            if choise == "1":           
                print()
                print("----------------------------------------------->>>>>    Flowers    <<<---------------------------------------------------\n")
                print(f" Id's We Are Having :{[i for i in temp.keys()]}")
                print()
                key = input("Enter ID of Flower Which Want You Want to Edit :")
                for i , r in temp[key].items():
                    print(f"{i}            :         {r}")
                field = input("Enter Which Thing You Want to Edit Flower :")
                update = input(f"Enter Your Update {field} :")
                temp[key][field] = update
                with open("Flowers.json","w")as f:
                    json.dump(temp,f,indent=4)
                print(f"Your {field} Got Updated Sucessfully ")
            else:
                print("            Thank You             ")
                sys.exit()


class User(Admin):
    def __init__(self):
        super().__init__()
        self.registered = {}
        self.l = []
        

    def Signing_into_app(self):
        name = input("Enter Your Name Here :")
        age = input("Enter Your Age Here :")
        mobile = input("Enter Your Mobile Number Here :")
        email  = input("Enter Your Email Here :")
        password = input("Enter Your Password Here :")
        self.registered ={"Name":name,"Age":age,
                        "Mobile Number":mobile,"Email Id":email,
                        "Password":password}
        with open("Registerted.json",'w') as f:
            json.dump(self.registered,f,indent=4)
        return "Your Registertion Got Completed"
    
    def login(self):
        with open("Registerted.json",'r') as f:
            temp = json.load(f)
        email = input("Enter Your Email Here :")
        password = input("Enter Your Password Here :")
        if email == temp["Email Id"]:
            if password == temp["Password"]:
                print("              ⭐Login Sucessfully ⭐             ")
                return True
            return "Invalid Password Try Again"
        else:
            return "         Invalid Login ID          " 

    def buy_flowre(self):
        with open("Flowers.json","r") as f:
            self.temp = json.load(f)
        self.rs = 0
        while True:
            print("------------------------>>>>>>Welcome to Shoping Aera")
            print("+="*55)
            print("1. for Buy Flower ")
            print("2. End Your Shoping")
            print("+="*55)
            seltion = input("Select Your Choise :")
            if seltion =="1":
                print(self.view_flower_price())
                choise = input("select a flower which you want to buy :")
                self.qyt = input("Select Your Quentity :")
                self.l.append([self.temp[choise]["Flower Name"],{"Quentity":self.qyt}])
                self.rs+=int(self.temp[choise]["Prices"])
                print( "Your Total Bill is :" +str(int((self.rs)*int(self.qyt))))
            else:
                print({self.rs:{"Flowers":self.l}})
                return ""

    def profile_update(self):
        with open("Registerted.json",'r') as f:
            temp = json.load(f)
        print("-------------------->>>>> User Profile <<<<-------------------\n")
        for i, v in temp.items():
            print(f"{i}   :  {v}")
        filed = input("Enter Which Thing You Want to Update :")
        update_val = input("Ente Your Update Value :")
        temp[filed]=update_val
        with open("Registerted.json",'r') as f:
                json.dump(temp,f,indent= 4)
        return "Your Profile Got Update"




            



        
