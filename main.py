from notification import msg_telegram
from run_selenium import run
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

wait_time = int(input("Enter the Interval between loops in minutes\n"))*60

service = Service(executable_path='chromedriver.exe')
options = ChromeOptions()
options.add_argument("--headless=chrome")
options.add_argument("--log-level=3")

class_ids = []
class_names = []
class_numbers = []
class_profs = []


with open("Classes.txt", 'r') as f:
    classes = f.readlines()
    for i in range(0,len(classes),4):        
        class_ids.append(classes[i].strip('\n'))
        class_names.append(classes[i+1].strip('\n'))
        class_numbers.append(int(classes[i+2].strip("\n")))
        class_profs.append(classes[i+3].strip('\n'))

loop_count = 0

driver = None
while True:
    try:
        print("Driver is starting...")
        driver = webdriver.Chrome(service=service, options=options)        
        for i in range(len(class_numbers)):
            print(f"{class_ids[i]} by {class_profs[i]} is being checked")
            open_seats = run(driver, class_numbers[i])
            print("Available Seats: ",open_seats)
            print()
            if open_seats > 0:
                print(msg_telegram(f"{class_ids[i]}\n{class_names[i]}\nby {class_profs[i]}\n\nOpen Seats: {open_seats}"))
        loop_count += 1
        print("All checks completed. Driver is closing...")
        driver.close()
        print("The loop has been run: ", loop_count)
        print("Wait Time: ", wait_time)
        time.sleep(wait_time)
    except KeyboardInterrupt:
        print("\nScript stopped by user")
        driver.quit()
        break
    except Exception as e:
        print (f"An error occurred: {repr(e)}")
        driver.quit()
        break
