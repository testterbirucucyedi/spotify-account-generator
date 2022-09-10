import requests, string, random, argparse, sys
from colorama import Fore, init
init(autoreset=False)

print(Fore.LIGHTCYAN_EX + """
 ____       _ _           _ _______________
/ ___|  ___| (_)_ __ ___ / |___ /___ /___  |
\___ \ / _ \ | | '_ ` _ \| | |_ \ |_ \  / /
 ___) |  __/ | | | | | | | |___) |__) |/ /
|____/ \___|_|_|_| |_| |_|_|____/____//_/
    """)

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def generate():
    nick = getRandomText(8)
    passw = getRandomString(12)
    email = nick+"@"+getRandomText(5)+".com"

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.72",
             "X-Client-Id": getRandomString(32)}
    
    payload = {"creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nick,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code==200:
        if r.json()['status']==1:
            return (True, nick+":"+r.json()["username"]+":"+email+":"+passw)
        else:
            #Details available in r.json()["errors"]
            #print(r.json()["errors"])
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False, "Could not load the page. Response code: "+ str(r.status_code))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="how many accounts to generate, default is 1", type=lambda x: (int(x) > 0) and int(x) or sys.exit("Invalid number: minimum amount is 1"))
    parser.add_argument("-o", "--output", help="output file, default prints to the console")
    args = parser.parse_args()

    N = args.number if args.number else 1
    file = open(args.output, "a") if args.output else sys.stdout

    print(Fore.LIGHTGREEN_EX + "Generating accounts in the following format:", file=sys.stdout)
    print(Fore.LIGHTGREEN_EX + "NICKNAME:USERNAME:EMAIL:PASSWORD", file=sys.stdout)
    print(Fore.LIGHTRED_EX + "--------------------------------------------\n", file=sys.stdout)
    for i in range(N):
        result = generate()
        if result[0]:
            print(Fore.LIGHTWHITE_EX + result[1], file=file)
            if file is not sys.stdout:
                print(Fore.LIGHTWHITE_EX + result[1], file=sys.stdout)
        else:
            print(Fore.LIGHTWHITE_EX + str(i+1)+"/"+str(N)+": "+result[1], file=sys.stdout)

    if file is not sys.stdout: file.close()