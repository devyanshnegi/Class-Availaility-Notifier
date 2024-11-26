
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run(driver, class_number):
    driver.get(f'https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=A&honors=F&classNbr={class_number}&promod=F&searchType=all&term=2251')

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="class-results"]/div/div[2]/div[1]'))
    )

    try:
        seats = driver.find_element(By.XPATH, '//*[@id="class-results"]/div/div[2]/div[13]/div')
    except:
        seats = driver.find_element(By.XPATH, '//*[@id="class-results"]/div/div[2]/div[14]/div')
    if not seats.text:
        seats = driver.find_element(By.XPATH, '//*[@id="class-results"]/div/div[2]/div[12]/div')

    try:
        open_seats = int(seats.text.split(" ")[0])
    except ValueError:
        seats = driver.find_element(By.XPATH, '//*[@id="class-results"]/div/div[2]/div[12]/div')
        open_seats = int(seats.text.split(" ")[0])


    return open_seats
    