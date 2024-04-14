# Innput User ID And User Password
email = "ebad@executives.elitechain.co"
password = "executive@ebad999"


# Here things are setup
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random
import pygame
import json
import os
from selenium.common.exceptions import TimeoutException
import logging
logging.basicConfig(level=logging.DEBUG)
def play_audio(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

# Generate a random integer between 4 and 7
random_number = random.randint(4, 7)

current_directory = os.path.dirname(os.path.realpath(__file__))

# Path to your extension folder
extension_path = os.path.join(current_directory, 'Elitechian Data Finder')

extension_id = "ofaokhiedipichpaobibbnahnkdoiiah"


# Create ChromeOptions object
chrome_options = Options()

# Add extension path to ChromeOptions
chrome_options.add_argument('--load-extension=' + extension_path)

# Initialize the WebDriver (assuming Chrome here)
driver = webdriver.Chrome(options=chrome_options)

# Here Real Codes Start

# Open a webpage
driver.get("https://app.apollo.io/#/login?redirectTo=https%3A%2F%2Fapp.apollo.io%2F%23%2F")



# Wait for the email input field to be visible (maximum wait time: 10 seconds)
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "email"))
)

password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
# Send keys to the email input field
email_input.send_keys(email)
time.sleep(random_number)
password_input.send_keys(password)


login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "zp_H_wRH"))
)
login_button.click()


time.sleep(8)
for _ in range(2):
    # Increment the page number in the URL
    url = "https://app.apollo.io/#/people?finderViewId=5b6dfc5a73f47568b2e5f11c&personTitles[]=ceo&personTitles[]=manager&page={}&personLocations[]=United%20States&sortByField=person_name.raw&sortAscending=false".format(_+1)

    # Open the URL
    driver.get(url)

    # Wait for the checkbox to be visible and click it
    checkbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "zp_fwjCX"))
    )
    checkbox.click()
    time.sleep(random_number)
    # Wait for the "Apply Selection" button to be visible and click it
    apply_selection = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "zp_vXSNN"))
    )
    apply_selection.click()

    # Wait for the "Save" button to be visible and click it
    save = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "zp_Yeidq"))
    )
    save.click()
    time.sleep(random_number)
    # Wait for the "Confirm" button to be visible and click it
    confirm_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="confirm"]'))
    )
    confirm_button.click()

    # Continue with your Selenium script...
    time.sleep(10)  # Adjust the time as needed
    print("Page", _+1, "processed.")  # Print page number for tracking progress

driver.get("https://app.apollo.io/#/people?finderViewId=5b6dfc5a73f47568b2e5f11c&prospectedByCurrentTeam[]=yes&page=1")
time.sleep(10)  # Wait for 10 seconds

# Click on the table layout button
table_layout_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-cy="table-layouts-dropdown"]'))
)
table_layout_button.click()
time.sleep(5)  # Wait for 5 seconds

# Click on the new layout button
new_layout_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.zp_J2fES button.zp_zUY3r'))
)

new_layout_button.click()
time.sleep(10)  # Wait for 10 seconds

# Type "email" in the search columns input field
search_columns_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.zp_bWS5y.zp_J0MYa.zp_VWlZL'))
)
search_columns_input.send_keys("email")
time.sleep(10)  # Wait for 10 seconds

# Click on the next button
next_button = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//button[.//div[@data-elem="button-label" and text()="Next"]]'))
)
next_button.click()
time.sleep(10)  # Wait for 10 seconds

# Type "switching" in the layout name input field
layout_name_input = WebDriverWait(driver, 5).until(
     EC.visibility_of_element_located((By.NAME, "name"))
)
layout_name_input.send_keys("switching2")
time.sleep(10)  # Wait for 10 seconds

# Click on the create new layout button
table_element = driver.find_element(By.XPATH, '//table')

# Get the HTML content of the table
table_html = table_element.get_attribute("outerHTML")

# Parse the HTML table using BeautifulSoup
soup = BeautifulSoup(table_html, "html.parser")

# Extract data from the HTML table
data = []
rows = soup.find_all("tr")
for row in rows:
    cols = row.find_all(["th", "td"])
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Define the path for the CSV file
csv_file_path = "table_data.csv"

# Write the extracted data to a CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)


file_name = "voice.mp3"
file_path = os.path.join(current_directory, file_name)
play_audio(file_path)
time.sleep(5)


time.sleep(6)
driver.quit()
