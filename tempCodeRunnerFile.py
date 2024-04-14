for _ in range(1):
#     # Increment the page number in the URL
#     url = "https://app.apollo.io/#/people?finderViewId=5b6dfc5a73f47568b2e5f11c&personTitles[]=ceo&personTitles[]=manager&page={}&personLocations[]=United%20States&sortByField=person_name.raw&sortAscending=false".format(_+1)

#     # Open the URL
#     driver.get(url)

#     # Wait for the checkbox to be visible and click it
#     checkbox = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "zp_fwjCX"))
#     )
#     checkbox.click()
#     time.sleep(random_number)
#     # Wait for the "Apply Selection" button to be visible and click it
#     apply_selection = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "zp_vXSNN"))
#     )
#     apply_selection.click()

#     # Wait for the "Save" button to be visible and click it
#     save = WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "zp_Yeidq"))
#     )
#     save.click()
#     time.sleep(random_number)
#     # Wait for the "Confirm" button to be visible and click it
#     confirm_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="confirm"]'))
#     )
#     confirm_button.click()

#     # Continue with your Selenium script...
#     time.sleep(10)  # Adjust the time as needed
#     print("Page", _+1, "processed.")  # Print page number for tracking progress