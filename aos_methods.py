#
#  Lab_03. AOS:
#  Python project structure setup, local Git/GitHub repos.
#  Create New User, Log Out, Log In.
# ------------------------------------------------------------------------------------------------------------
#   Included following tasks:
#   Project Structure for AOS app automation with Python and Selenium;
#   Initiated local Git Repository and created remote GitHub project for it.
#   Created functions for AOS setUp, tearDown, Create New User, Logout and Login
#   In PyCharm app, opened existing Python Selenium project - python_cctb
#   Added new PyCharm directory - aos [in python_cctb project]
#   in aos directory added 3 new python files:
#   - aos_locators.py
#   - aos_methods.py
#   - aos_tests.py
#   ----------------------------------------------------------------------------------------------------------
#   in aos_methods.py script, WebDriver imported, initializations included;
#   Python functions setUp() and tearDown() defined
#   ----------------------------------------------------------------------------------------------------------
#   setUp() function includes:
#   - printed test's start and end time;
#   - browser window maximized after start;
#   - implicitly wait set to 30 seconds
#   - application URL:https://advantageonlineshopping.com/#/ (added to aos_locators.py, imported as variable)
#   - checked/compared the [driver.current_url] and [driver.title] with expected values in one conditional statement
#     user-friendly messages printed to confirm result of comparison. print({driver.title)}is used to show actual title
#     of the AOS home page
#   - closed browser and session quited
#   -------------------------------------------------------------------------------------------------------------
#   tearDown() function includes:
#   - check if driver is working and not None
#   - test end day/time printed
#   - closed browser and quit from session
#   -------------------------------------------------------------------------------------------------------------
#   aos_locators.py file contain variables for fake data generated with Faker library
#   -------------------------------------------------------------------------------------------------------------
#   aos_tests.py contain Unittest test class
#   -------------------------------------------------------------------------------------------------------------
#   new public repository called aos created in GitHub
#   initialized local .git repository in the aos folder (inside PyCharm)
#   Git push used to transfer these three files into aos repository
#   -------------------------------------------------------------------------------------------------------------
#Lab_04
#
#   ==============================================================================================================
import datetime
from time import sleep
#  import button as button
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import aos_locators as locators

# Using Selenium WebDriver, open the web browser.
s = Service(executable_path='C:/Tools/chromedriver.exe')
driver: WebDriver = webdriver.Chrome (service=s)

# using Fixture method - to open web browser:
def set_up():
    print(f'--------------------------------------------* Test Start Day/Time *---------------------------------------')
    print(f'Test Started at: {datetime.datetime.now()}')
    print(f'-------------------------------------* Website url,Current url, tTitle  *---------------------------------')
    driver.maximize_window()    #  maximize the browser window
    driver.implicitly_wait(30)   # time how long website will be displayed(30s)
    driver.get(locators.aos_url)    #  navigating to the "advantage shopping" website
    print(f'aos url: --{locators.aos_url}')
    print(f'Current page url: --{driver.current_url}')
    print(f'Current page Title: --{locators.aos_title}')
    # URL and home page title are as expected {confirmed} or is not {else}
    print(f'Home page url is: -- {locators.aos_url}')
    print(f'Home page title is: -- {driver.title}')
    print(f'------------------------------------* Login information *-------------------------------------------------')
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'We\' are at "Advantage Shopping" web page:-- {driver.current_url}')
        print(f'Thank you for coming today at the website of  -- {driver.title}')
    else:
        print(f'We\'re not at the "Advantage Shopping" home page. Please try again!')
        sleep(5)

# ==============================================================================================================##
#Creating New Account - using Faker library fake data
def create_user():
        driver.find_element(By.ID, 'menuUser').click()
        sleep(5)
        driver.find_element(By.XPATH, '/html/body/login-modal/div/div/div[3]').is_displayed()
        sleep(5)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(5)
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
        sleep(5)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(5)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
        sleep(5)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
        sleep(5)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(5)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(5)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
        sleep(5)
        driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
        sleep(5)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(5)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
        sleep(5)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state_province_region)
        sleep(3)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(3)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(5)
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(5)
        print(f' ---new user created "{locators.full_name}"---test passed')
        sleep(5)
        driver.close()
        sleep(5)
        driver.quit()
        sleep(5)


#   ==============================================================================================================
# Validating New Account created:
def validate_account():
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'--------------------------* Validation - New User account *------------------------------------')
        if driver.find_element (By.ID, 'menuUserLink').is_displayed ():
            print (f'--- User with the name {locators.full_name} is added successfully. Test Passed ---')
            print(f'---------------------------------------------------------------------------------------------')
            print(f'New Account confirmed -  username: {locators.new_username}')
            print(f'New Account fullname is: {locators.full_name}')
            print(f'New Account address is: {locators.address}')
            print(f'---------------------------------------------------------------------------------------------')
        else:
            print(f'New Account not created successfully. You are at {driver.current_url}')
            print(f'Please verify required fields(*). Make sure they are correct data type.')
            print(f'---------------------------------------------------------------------------------------------')
            driver.close()
            sleep(5)
            driver.quit()
            sleep(5)

#   ==============================================================================================================
# Logout:
def log_out():
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(5)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
        sleep(5)
        print(f'---------------------------------* Logout Information *-----------------------------------------------')
        print(f'Log out successfully at: {datetime.datetime.now()}')
        print(f'------------------------------------------------------------------------------------------------------')
        print(f'User --{locators.full_name} logged out from website: ')
        print(f'Email: {locators.email}\nUsername: {locators.new_username}\nPassword: {locators.new_password}\nfull_name: {locators.full_name}')
        print(f'---------------- --------------------* Thank you *-----------------------------------------------------')
        print(f'Thank you {locators.full_name} for visiting www.advantageonlineshopping.com today!')
        print("We are looking forward to see you soon shopping at https://advantageonlineshopping.com again.")
        print("Have a great day!")
        driver.close()
        sleep(5)
        driver.quit()
        sleep(5)

#  ==============================================================================================================
#  Login
def log_in(username, password):
    print(f'--------------------------------* User Login Information *------------------------------------------------')
    if driver.current_url == locators.aos_url:
        print(driver.current_url)
        sleep(5)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(5)
        driver.find_element (By.NAME, 'username').send_keys(username)
        sleep(5)
        driver.find_element(By.NAME, 'password').send_keys(password)
        sleep(5)
        driver.find_element(By.NAME, 'remember_me').click()
        sleep(5)
        driver.find_element(By.ID, ('sign_in_btnundefined')).click()
        sleep(5)
        print(f'Client is login to --{locators.aos_url} website.')
        print(f'Username: {locators.new_username}\nPassword: {locators.new_password}\nfull_name: {locators.full_name}')

#  ##################################################################################################################

def delete_user():
    driver.find_element(By.XPATH, f'//a[@id="menuUserLink"]/span[contains(.,{locators.new_username})]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    if driver.find_element(By.XPATH, f'//*[contains(., "{locators.full_name}")]').is_displayed():
        print({locators.full_name}, 'is different from ', {locators.new_username})
        driver.find_element(By.XPATH, '//button/div[contains(., "Delete Account")]').click()
        sleep(5)
        driver.find_element(By.XPATH, '//div[@class="deletePopupBtn deleteRed"]').click()
        print(f'--------------* Account Deleted: Information *------------------------------------------------')
        print('The user account was deleted successfully')
        driver.close()
        sleep(2)
        driver.quit()

#  ##################################################################################################################

#  Close the browser and display user-friendly messages:
def tearDown():
    print(f'---------------------* Thank you for visiting advantage online shopping website  *------------------------')
    if driver is not None:
       print (f'Test Completed at: {datetime.datetime.now()}')
       print(f'------------------------------------------------------------------------------------------------------')
       driver.close()
       sleep (5)
       driver.quit()
########################################################################################################################
set_up()   #  open the browser
#create_user()   #creating NEW user
# #validate_account()  #validating NEW account
#log_out()   # log out from the browser
# log_in(locators.aos_username, locators.aos_password)     # log in the existing account
# log_out()   #   log out from the newly created account
delete_user()   #delete current user
tearDown()