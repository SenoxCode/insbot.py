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
version = 1.3


time.sleep(0.3)
ascii_banner = pyfiglet.figlet_format(pythonname + " " +  str(version))
print(ascii_banner)
time.sleep(1)
print("\n" + pythonname + " "  + str(version) + " by Senox")
time.sleep(0.3)
print("https://github.com/SenoxCode\n\n\n")
time.sleep(0.3)
print("Trying to login...")


api = InstagramAPI(name, password)
api.login()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("\n\n\n\n\n\nLogged in as " + name + "\n")

germanaccounts = [165018, 601139763, 186926265, 266967359, 8826539, 631071319, 206446910, 340527886, 44451138, 49261384, 51577692, 192998906, 310056264, 446305980, 50326174, 378496191, 211563622, 483590318, 299374274, 733718680]
popularaccounts = [6860189, 325734299, 305701719, 451573056, 5823711452, 787132, 11830955, 247944034, 232192182, 7719696, 25025320, 9365072543, 217338092, 13336763,187619120, 1574083, 182196805,748381723,19077223,  22686243]

def followbot(accountlist):
    print("\n\n\nThis bot will follow & unfollow popular accounts to get more followers on your account.")
    time.sleep(5)
    print("\nStarting bot...")
    print("Press CTRL+C to stop\n")
    time.sleep(3)
    while True:
        account = 1
        for x in accountlist:
            api.follow(x)
            xstring = str(x)
            print("Following UserID " + xstring + "..." + " [" +  str(account) +  "/20]")
            time.sleep(5)


            if account < 20:
                account += 1
            else:
                account = 1




        print("\nWaiting 120 seconds...\n")
        time.sleep(120)

        for x in accountlist:
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
    print("\n\n\nThis bot will like other pictures to get you more likes.")
    time.sleep(5)
    print("\nStarting bot...")
    print("Press CTRL+C to stop\n")
    time.sleep(3)
    while True:
        api.getHashtagFeed("like4like", '')
        tmp = api.LastJson
        for item in tmp["items"]:
            api.like(item["id"])
            print("Liked MediaID " + item["id"])
            time.sleep(5)

def likeandunlikebot():
    print("\n\n\nThis bot will like & unlike pictures to get more likes on your account.")
    time.sleep(5)
    print("\nStarting bot...")
    print("Press CTRL+C to stop\n")
    time.sleep(3)
    while True:
        loop = 0
        likedpictures = []
        api.getHashtagFeed("like4like", '')
        tmp = api.LastJson
        for item in tmp["items"]:
            api.like(item["id"])
            print("Liked MediaID " + item["id"])
            loop = loop + 1
            time.sleep(5)
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
    print("\nChoose an option:\n[0] EXIT\n[1] International account list \n[2] German account list")
    optionlist = raw_input()
    if optionlist == "0":
        print("Exiting...")
        time.sleep(3)
    elif optionlist == "1":
        followbot(popularaccounts)
    elif optionlist == "2":
        followbot(germanaccounts)
    else:
        print("Unknown option...")
        time.sleep(2)
elif option == "2":
    likebot()
elif option == "3":
    likeandunlikebot()

else:
    print("ERROR: INVALID NUMBER...")
    time.sleep(3)

