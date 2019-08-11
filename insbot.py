from InstagramAPI import InstagramAPI
import time
import pyfiglet
from pip._vendor.distlib.compat import raw_input

####### I don't take any responsibility for damage on your account ######
####### CODED BY https://github.com/SenoxCode ######

##########
##########

name = "name"   #Change the name in the quotation marks to your Instagram name
password = "password" #Change the password in the quotation marks to your Instagram password

##########
##########



pythonname = "insbot.py"
version = 1.2


time.sleep(0.3)
ascii_banner = pyfiglet.figlet_format(pythonname + " " +  str(version))
print(ascii_banner)
time.sleep(1)
print("\ninsbot.py 1.0 by Senox")
time.sleep(0.3)
print("https://github.com/SenoxCode\n\n\n")
time.sleep(0.3)
print("Trying to login...")


api = InstagramAPI(name, password)
api.login()
print("\n\n\n\n\n\nLogged in as " + name + "\n")

popularaccounts = [6860189, 325734299, 305701719, 451573056, 5823711452, 787132, 11830955, 247944034, 232192182, 7719696, 25025320, 9365072543, 217338092, 13336763,187619120, 1574083, 182196805,748381723,19077223,  22686243]



def followbot():
    while True:
        account = 1
        for x in popularaccounts:
            api.follow(x)
            xstring = str(x)
            print("Following UserID " + xstring + "..." + " [" +  str(account) +  "/20]")
            time.sleep(3)

            if account < 20:
                account += 1
            else:
                account = 1




        print("\nWaiting 120 seconds...\n")
        time.sleep(120)

        for x in popularaccounts:
            api.unfollow(x)
            xstring = str(x)
            print("Unfollowing UserID " + xstring + "..." + " [" +  str(account) +  "/20]")
            time.sleep(3)
            if account < 20:
                account += 1
            else:
                account = 1

        print("\nWaiting 60 seconds...\n")
        time.sleep(60)

def likebot():
    while True:
        api.getHashtagFeed("like4like", '')
        tmp = api.LastJson
        for item in tmp["items"]:
            api.like(item["id"])
            print("Liked MediaID " + item["id"])
            time.sleep(3)

def likeandunlikebot():
    while True:
        loop = 0
        likedpictures = []
        api.getHashtagFeed("like4like", '')
        tmp = api.LastJson
        for item in tmp["items"]:
            api.like(item["id"])
            print("Liked MediaID " + item["id"])
            loop = loop + 1
            time.sleep(4)
            likedpictures.append(item["id"])

            if loop == 25:
                loop = 0
                for i in likedpictures:
                    api.unlike(i)
                    print("Unliked MediaID " + i)
                    time.sleep(3)
                likedpictures.clear()







print("Choose an option:\n[0] EXIT\n[1] FOLLOWER BOT\n[2] LIKE BOT\n[3] LIKE & UNLIKE BOT")
option = raw_input()





if option == "0":
    print("\nExiting...")
    time.sleep(3)
elif option == "1":
    print("\nStarting bot...")
    print("Press CTRL+C to stop\n")
    time.sleep(3)
    followbot()
elif option == "2":
    print("\nStarting bot...")
    print("Press CTRL+C to stop\n")
    time.sleep(3)
    likebot()
elif option == "3":
    print("\nStarting bot...")
    print("Press CTRL+C to stop\n")
    time.sleep(3)
    likeandunlikebot()

else:
    print("ERROR: INVALID NUMBER...")
    time.sleep(3)

