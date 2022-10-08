accounts = ("Test" : "Test1", "Test2" : "password")
loading = True
fails = 0
failsLeft = 5 
timewait = 10
lockedOut = 0

while loading: 
    username = input("please enter your username: ")
    paaword = input("please enter the password for " + username + ": ")

    if (accounts.get(username) == password):
        print("login succesful")
        test = input(".") #this is just so the program doesn't shut down as you get the username and password correct 
    else:
      print("login failed")
      fails = fails + 1 
      failsLeft = failsLeft - 1
      print("you have" + str(failsLeft) + "until being lock out for " str(timewait))

    if failsLeft == 0:
        print("Sorry you have been locked out for" + str(timewait) + "seconds.")
        lockedOut = lockedOut + 1
        failsLeft = failsLeft + 5

    if lockedOut == 3:
        print("Sorry you have been permantly locked out.")
        loading = False 


    
    
