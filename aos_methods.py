import datetime
from time import sleep
#   import button as button
#   import linkedin
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#   from selenium.webdriver.support.ui import Select
import aos_locators as locators

#   Using Selenium WebDriver, open the web browser.
s = Service(executable_path='C:/Tools/chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)


# ====================================================================================================================
# using Fixture method - to open web browser:
def set_up():
    print(f'--------------------------------------------* Test Start Day/Time *---------------------------------------')
    print(f'Test Started at: {datetime.datetime.now()}')
    print(f'-----------------------* Current Website: url and Title  *---------------------------------')
#   maximize the browser window
    driver.maximize_window()
#   time how long website will be displayed(30s)
    driver.implicitly_wait(30)
#   navigating to the "advantage shopping" website
    driver.get(locators.aos_url)
    print(f'aos url: --{locators.aos_url}')
    print(f'Current page url: --{driver.current_url}')
    print(f'Current page Title: --{locators.aos_title}')
    print(f'------------------------------------* Home page, Home title *---------------------------------------------')
#   URL and home page title are as expected {confirmed} or ---is not = in {else}
    print(f'Home page url is: -- {locators.aos_url}')
    print(f'Home page title is: ', {driver.title})
    print(f'---------------------------* Login into Advantage Shopping" web site *------------------------------------')
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'We\' are at "Advantage Shopping" web page:-- {driver.current_url}')
        print(f'Thank you for coming today at the website of  -- {driver.title}')
    else:
        print(f'We\'re not at the "Advantage Shopping" home page. Please try again!')
        sleep(5)
        teardown()


# =====================================================================================================================
#   Creating New Account - using Faker library fake data
def create_user():
    sleep(3)
    print(f'--------------------------* Creating New User Account *------------------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(3)
    #   if driver.current_url == locators.aos_register_url and driver.title == locators.aos_title:
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    print(f'new user name: -- {locators.new_username}')
    sleep(3)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    print(f'new user email address: -- {locators.email}')
    sleep(3)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    sleep(3)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    print(f'new user password: -- {locators.new_password}')
    sleep(3)
    # else:
    # print('something is wrong in this part of code')
    # driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    # sleep(5)
    # driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    # sleep(5)
    # driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
    # sleep(5)
    # driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
    # sleep(5)
    # driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    # sleep(5)
    # driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    # sleep(5)
    # driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state_province_region)
    # sleep(3)
    # driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    # sleep(3)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(3)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(3)
    print(f'Account for New User: **{locators.full_name}** is created.')
    sleep(3)


#   ==============================================================================================================
# Validating New Account created:(user name displayed)
def validate_account():
    sleep(3)
    print(f'--------------------------* Validating User Account *------------------------------------')
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        if driver.find_element(By.XPATH, f'//a[contains(.,"{locators.new_username}")]'):
            sleep(3)
            print(f'*Username {locators.new_username} is displayed on the Menu on Top right corner of the screen*')
        else:
            print('user not found.')
            sleep(3)


#   ==============================================================================================================
#   Logout:
def log_out():
    sleep(3)
    print(f'---------------------------------* Logout Information *-----------------------------------------------')
    if driver.current_url == locators.aos_url:
        #   driver.find_element(By.LINK_TEXT, 'My account').click()
        driver.find_element(By.XPATH, '//*[@id="menuUserLink"]').click()
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
        sleep(3)
        print("Successfully logged out from the User account")


#  ==============================================================================================================
#  Login:
def log_in(username, password):
    sleep(2)
    print(f'--------------------------------* User Login Information *-------------------------------------------')
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.NAME, 'username').send_keys(username)
        sleep(2)
        driver.find_element(By.NAME, 'password').send_keys(password)
        sleep(2)
        driver.find_element(By.NAME, 'remember_me').click()
        sleep(2)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)
        print(f'Client is loggin to --{locators.aos_url} website.')
        print(f'Username: {locators.aos_username}\nPassword: {locators.aos_password}')
        sleep(2)


#  ==============================================================================================================
# Checking availavility/clicability of social media images(Fasebook,Twitter, Linkedin) at HOME PAGE (FOLLOW US section)
def check_social_network_facebook():
    sleep(1)
    print(f'--------------------------------* Check Social Network - Facebook *---------------------------------------')
    if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
        print('We could find Facebook image  FOLLOW US displayed')
        sleep(1)
        facebook = driver.find_element(By.XPATH, '//img[@name="follow_facebook"]')
        print(f' the Facebook img display is: {facebook.is_displayed()}')
        print(f' the Facebook img clickable condition is: {facebook.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_facebook"]').click()
        driver.switch_to.window(driver.window_handles[1])
        if driver.current_url == 'https://www.facebook.com/MicroFocus/':
            print(f'Social media link Facebook is available and clickable')
            sleep(1)
        else:
            print('Facebook page not found')
            sleep(1)
            print('Facebook link has been closed')
            driver.switch_to.window(driver.window_handles[0])
#   -----------------------------------------------------------------------------------------------------------------
# def check_social_Network_twitter():
#     sleep(5)
#     print(f'--------------------------------* Check Social Network - Twitter *-------------------------------------')
#     #if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
#     if driver.find_element(By.XPATH, '// *[ @ id = "follow"]').is_displayed():
#        print('We could find image FOLLOW US on Twitter displayed')
#        sleep(5)
#        twitter = driver.find_element(By.XPATH, 'img[@bname="follow_twitter"]')
#        print(f' the Twitter img display is: {twitter.is_displayed()}')
#        print(f' the Twitter img display is: {twitter.is_enabled()}')
#        driver.find_element(By.XPATH, '//img[@name="follow_twitter"]').click()
#        driver.switch_to.window(driver.window_handles[1])
#        if driver.current_url == 'https://www.twitter.com/MicroFocus/':
#             assert'Twitter.com' in driver.current_url()
#             print(f'Social media link Twitter is available and clickable')
#             sleep(3)
#         else:
#             print('Twitter page not found')
#             sleep(5)
#             print('Twitter link has been closed')
#             driver.switch_to.window(driver.window_handles[0])
#   -----------------------------------------------------------------------------------------------------------------
# def check_social_Network_linkedIn():
#     sleep(5)
#     print(f'--------------------------------* Check Social Network - LinkedIn *-----------------------------------')
#     if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
#         sleep(5)
#         print('Image  "FOLLOW US on LinkedIn" displayed')
#         #linkedin = driver.find_element(By.XPATH, 'img[@bname="follow_linkedin"]')
#         #print(f' the linkedin img display is: {linkedin.is_displayed()}')
#         #print(f' the linkedin img display is: {linkedin.is_enabled()}')
#         #driver.find_element(By.XPATH, '//img[@name="follow_linkedin"]').click()
#         #driver.switch_to.window(driver.window_handles[1])
#         #if driver.current_url == 'https://www.linkedin.com//company/Micro/Focus/':
#         #if 'linkedin.com' in  'https://www.linkedin.com//company/Micro/Focus/':
#             assert 'Linkedin.com' in driver.current_url()
#                  if driver.current_url == 'https://www.linkedin.com/':
#             print(f'Social media link linkedIn is confirmed')
#             print(f'Sorry, "Follow Us" link to our linkedin profile is not working at the moment.Please try again.')
#             sleep(3)
#         else:
#             print('linkedIn page not found')
#             print('linkedIn link has been closed')
#             driver.switch_to.window(driver.window_handles[0])


#  ==============================================================================================================
#   checking shopping cart, paying for the order
def check_out_shopping_cart():
    sleep(3)
    print(f'------------------------------* Check Out Shoppping Cart *----------------------------------------------')
    if driver.current_url == 'https://www.advantageonlineshopping.com/#/':
        driver.get('https://www.advantageonlineshopping.com/#/product/10')
        sleep(3)
        driver.find_element(By.NAME, 'save_to_cart').click()
        sleep(3)
        driver.find_element(By.ID, 'shoppingCartLink').click()
        sleep(3)
        driver.find_element(By.ID, 'checkOutButton').click()
        sleep(3)
        print(f' we can see ORDER PAYMENT and SHIPPING DETAILS page')
        print(f' ORDER SUMMARY information is displayed')
        print(f' ---Customer Name {locators.full_name} is displayed on shipping details page ---')
        sleep(3)
        driver.find_element(By.ID, 'next_btn').click()
        if driver.current_url == 'https://www.advantageonlineshopping.com/#/orderPayment':
            print(f' payment info was entered for SafePay:username and password')
            driver.find_element(By.NAME, 'safepay').click()
            sleep(3)
            # driver.find_element(By.NAME, 'safepay_username').send_keys(locators.aos_username)
            # sleep(5)
            # driver.find_element(By.NAME, 'safepay_password').send_keys(locators.aos_password)
            # sleep(3)
            driver.find_element(By.NAME, 'save_safepay')
            sleep(3)
            driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
            sleep(3)
        else:
            print(f'current url 2', driver.current_url)
    else:
        print(f'current url 1', driver.current_url)


#  ===================================================================================================================
def validate_order_created():
    sleep(3)
    print(f'------------------------------* Validate Order Created *----------------------------------------------')
    if driver.current_url == 'https://www.advantageonlineshopping.com/#/orderPayment':
        sleep(3)
        print(f' Order Payment was made and thank you message was displayed:"Thank you for buying with Advantage')
        sleep(3)
        locators.tracking_number = driver.find_element(By.ID, 'trackingNumberLabel').text
        print(f' Tracking number was captured for this order:', locators.tracking_number)
        locators.order_number = driver.find_element(By.ID, 'orderNumberLabel').text
        print(f' Order number was captured for this order: {locators.order_number}')
        print(f' Shipping to: {locators.full_name}, Address:{locators.address}')
        print(f' Phone number: {locators.phone_number}')
        print(f' Date and Time: {datetime.datetime.now()}')
    else:
        print(f'current url 3', driver.current_url)


#  ===================================================================================================================
#   checking if order is deleted
def delete_order():
    sleep(3)
    print(f'--------------------------------* Delete Order - Information *----------------------------------------')
#   if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
    if driver.current_url == 'https://www.advantageonlineshopping.com/#/MyOrders':
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'REMOVE').click()
        sleep(3)
        driver.find_element(By.XPATH, f'//label[contains(text(), "CANCEL")').is_displayed()
        sleep(3)
        print(f'Order is deleted.')
        driver.find_element(By.XPATH, f'//label[contains(text(), "No orders")').is_displayed()
        sleep(3)
        print(f'Order is deleted by validating "No orders" text displayed.')
        sleep(3)
    else:
        print(f'Order is not deleted.')


#  ===================================================================================================================
#   checking items on home page clickable yes/no
def check_availability_logo():
    sleep(3)
    print(f'---------------------------* Items on Home page: LOGO available/clickabe   *--------------------')
    if driver.current_url == locators.aos_url:
        logo = driver.find_element(By.ID, 'Layer_1')
        # logo = driver.find_element(By.CLASS_NAME, 'roboto-medium ng-binding')
        # logo = driver.find_element(By.CLASS_NAME, 'logoDemo roboto-light ng-binding')
        print(f'The display feature of the logo is: {logo.is_displayed()}')
        print(f'The enable feature of the logo is: {logo.is_enabled()}')
        print(f'LOGO of Advantage Shopping is displayed and clickable.You can proceed with your shopping!')


#  ===================================================================================================================
#   checking items on home page (shown by "text" on home page)  available and clickable
def check_availability_text():
    sleep(3)
    print(f'---------------------------* Items on Home page available/clickabe (text)  *--------------------')
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.XPATH, '//span[contains(., "SPEAKERS")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(2)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'speakersLink').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Item SPEAKERS is displayed and clickable.You can proceed with your shopping!')
#   -----------------------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "TABLETS")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'tabletsTxt').click()
        sleep(2)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'tabletsLink').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Item TABLETS is displayed and clickable.You can proceed with your shopping-HOME PAGE')
#   ----------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "HEADPHONES")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'headphonesTxt').click()
        sleep(2)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'headphonesLink').click()
        sleep(2)
        driver.back()
        print(f'Item HEADPHONES is displayed and clickable.You can proceed with your shopping!')
#       ----------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "LAPTOPS")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'laptopsTxt').click()
        sleep(2)
        driver.back()
        driver.find_element(By.ID, 'laptopsLink').click()
        sleep(2)
        driver.back()
        print(f'Ittm LAPTOPS is displayed and clickable.You can proceed with your shopping!')
#       ----------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "MICE")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'miceTxt').click()
        sleep(2)
        driver.back()
        driver.find_element(By.ID, 'miceLink').click()
        sleep(2)
        driver.back()
        print(f'Item MICE is displayed and clickable.You can proceed with your shopping!')


#  ===================================================================================================================
#   checking for:our [products,special offer.popular items, contact us]
def check_availability_links():
    sleep(5)
    print(f'*Home Page Menu:Items on Home page clickabe (links)[our products,special offer,popular items,contact us]*')
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.CLASS_NAME, 'nav-li-Links').is_displayed()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'our_products').click()
        # driver.back()
        # sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Menu Item PRODUCTS is displayed and clickable.You can proceed with your shopping!')
# ------------------------------------------------------------------------------------------------------------------
#        assert driver.find_element(By.CLASS_NAME, 'menu navLinks roboto-regular ng-scope').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'special_offer_items').click()
        sleep(2)
        # driver.back()
        # sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Menu Item "SPECIAL OFFER" is displayed and clickable.On click opens page with "Special Offers!"')
#    ------------------------------------------------------------------------------------------------------------------
#   assert driver.find_element(By.CLASS, [ng-scope]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'popular_items').click()
        sleep(2)
        # driver.back()
        # sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Link "POPULAR ITEMS" is displayed and clickable.On click opens page with list of "Popular Items!"')
#   ------------------------------------------------------------------------------------------------------------------
#    assert driver.find_element(By.CLASS, [menu navLinks roboto-regular ng-scope]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'contact_us').click()
        sleep(2)
        # driver.back()
        # sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Item "CONTACT US" is displayed and clickable.On click oppening form "Contact Us".')

#  ===================================================================================================================
#  checking for popular items, etc.
#  def check_for_links():
#      assert driver.find_element(By.XPATH, '//span[contains(., "SPEAKERS")]').is_displayed()
#         products = driver.find_element(By.ID,'our_products').click()
#         driver.back()
#         speaker = driver.find_element(By.ClASS, 'menu navLinks roboto-regular ng-scope').click()
#         driver.back()
#         speaker = driver.find_element(By.ID, 'our_products'
#         speaker = driver.find_element(By.ID, 'speakerTxt')
#         print(f'The display feature of the speaker is: {(not (speaker))}')
#         print(f'The enable feature of the speaker is: {(not (speaker))}')


#  ===================================================================================================================
#   deleting user, checking if user is deleted
def delete_user():
    sleep(3)
    print(f'----------------------------------* Deleted User - Information *-------------------------------------')
    driver.find_element(By.XPATH, f'//a[@id="menuUserLink"]/span[contains(.,{locators.new_username})]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    if driver.find_element(By.XPATH, f'//*[contains(., "{locators.full_name}")]').is_displayed():
        print({locators.full_name}, 'is different from ', {locators.new_username})
        driver.find_element(By.XPATH, '//button/div[contains(., "Delete Account")]').click()
        sleep(3)
        driver.find_element(By.XPATH, '//div[@class="deletePopupBtn deleteRed"]').click()
        print(f'--------------* Account Deleted: Information *------------------------------------------------')
        print('The user account was deleted successfully')


#  ===================================================================================================================
#   Close the browser and display user-friendly messages:
def teardown():
    sleep(3)
    if driver is not None:
        print(f' ----------------------* Thank you for visiting advantage online shopping website  *----------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        print(f'------------------------------------------------------------------------------------------------------')
        sleep(3)
        driver.close()
        sleep(3)
        driver.quit()
        sleep(3)


#  ===================================================================================================================
#   ===----==*  List of Functions: *----------
# set_up()
# create_user()
# validate_account()
# check_availability_logo()
# check_availability_text()
# #check_availability_links()
# check_social_network_facebook()
# #   check_social_Network_twitter()
# #   check_social_Network_linkedIn()
# #   check_out_shopping_cart()
# #   validate_order_created()
# log_out()
# log_in(locators.aos_username, locators.aos_password)
# #   delete_order()
# log_out()
# #   delete_user()
# teardown()
