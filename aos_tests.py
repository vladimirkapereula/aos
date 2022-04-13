import unittest
import aos_methods as methods
import aos_locators as locators


class AosPositiveTestCases(unittest.TestCase):
    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    
    def test_aos():
         methods.set_up()       #  open thee browser
#        methods.create_user()      #  create NEW user
         methods.log_in(locators.aos_username, locators.aos_password)   #  log in the browser
#        methods.validate_account()     # check we are looged in with the correct credentials
         methods.log_out()      #  log out from the account
#        methods.log_in(locators.aos_username, locators.aos_password)     #  log in the browser
#        methods.log_out()   # log out from the browser
#        methods.delete_user()
         methods.tearDown()      # close the web browser