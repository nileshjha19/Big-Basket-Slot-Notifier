from selenium import webdriver
import chromedriver_autoinstaller
from plyer import notification
import sys
import time
import os

def printTime(msg=""):
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[{}]:{}".format(current_time,msg), end="\n")

def windows10Notifier(title="", msg=""):
    from plyer import notification

    notification.notify(
        title=title,
        message=msg,
        app_name='Big Basket Delivery Slot Notifier'
    )

def get_bb_slot(url):
    # auto-install chromedriver 
    print()
    printTime("Do this on chromeTab:")
    printTime("1) Please LOGIN using OTP using mobile or emailID in newly opened chrome window")
    printTime("2) Choose correct delivery location on web page.") 
    print()
    printTime("IMPORTANT: Keep browser tab open and this command window running")

    time.sleep(5) #added wait to load above msgs
    chromedriver_autoinstaller.install() 

    driver = webdriver.Chrome()
    driver.get(url)
    print("Please login using OTP and then wait for a while.")
    time.sleep(60)


    
    tryCount = 1
    while 1:
        driver.get(url)     
        time.sleep(2)
        flag = 0
       # print("Trying to find a slot!")
        printTime("Trycount#{} Finding a slot!".format(tryCount))
        try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()

            time.sleep(5)  #driver take a few sec to update the new url
            src = driver.page_source
            if "checkout" in driver.current_url and not "Unfortunately, we do not have" in src:
          #      print("Found the slots!")
                printTime("Found the slots!")
                notify("Slots Available!","Please go and choose the slots")
                
                break
          #       for i in range(60):
          # #           notify("Slots Available!", "Please go and choose the slots!")
          #            notify("Big Basket Delivery Slots Available!", "Please go and choose the slots!")
          #            time.sleep(20)
          #            print("Ctrl+c this program once you are done with checkout and payment.")
        except Exception  as e:
          #  print("If this message pops up multiple times, please find the error and create a PR!")
          #  print (e)
            printTime("Please stay on basket's page.")

            print(e)
            pass
        #print("No Slots found. Will retry again.")
        #time.sleep(50)
        printTime("No Slots found, will retry in a minute.")
        tryCount = tryCount+1
        time.sleep(60)

def notify(title, text):
   # if os.name == 'posix':
    if os.name == 'nt':
        windows10Notifier(title, text)
    elif os.name == 'posix':
        os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    elif os.name == 'Linux'
        os.system('spd-say "Slots for delivery available!"')

def main():
    printTime("Prerequisite: You have items added to your bigbasket and correct delivery address")
    get_bb_slot('https://www.bigbasket.com/basket/?ver=1')

if __name__ == '__main__':
    main()
