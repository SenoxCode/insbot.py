from InstagramAPI import InstagramAPI
import time

##########
##########

name = "name"   #Change the name in the quotation marks to your Instagram name
password = "password" #Change the password in the quotation marks to your Instagram password

##########
##########




time.sleep(0.3)
print("\ninsbot.py 1.0 by Senox")
time.sleep(0.3)
print("https://github.com/SenoxCode\n\n\n")
time.sleep(0.3)
print("Trying to login...")


api = InstagramAPI(name, password)
api.login()
print("\n\n\n\n\n\nLogged in as " + name + "\n")



popularaccounts = [6860189, 325734299, 305701719, 451573056, 5823711452, 787132, 11830955, 247944034, 232192182, 7719696, 25025320, 9365072543, 217338092, 13336763,187619120, 1574083, 182196805,748381723,19077223,  22686243]
def followpop():

    while True:
        for x in popularaccounts:
            api.follow(x)
            xstring = str(x)
            print("Following UserID " + xstring + "...")
            time.sleep(4)
        print("\nWaiting 60 seconds...\n")
        time.sleep(60)
        for x in popularaccounts:
            api.unfollow(x)
            xstring = str(x)
            print("Unfollowing UserID " + xstring + "...")
            time.sleep(4)
        print("\nWaiting 60 seconds...\n")
        time.sleep(60)


followpop()

