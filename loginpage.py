accounts = ("Test" : "Test1", "Test2" : "password")

username = input("please enter your username: ")
paaword = input("please enter the password for " + username + ": ")
if (accounts.get(username) == password):
    print("login succesful")
    test = input(".") #this is just so the program doesn't shut down as you get the username and password correct 
else:
    print("login failed")
    