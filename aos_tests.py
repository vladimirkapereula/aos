import unittest
import aos_methods as methods
import aos_locators as locators


class AosPositiveTestCases(unittest.TestCase):
    @staticmethod  # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_aos():
        methods.set_up()
        methods.create_user()
        methods.validate_account()
        methods.log_out()
        methods.log_in(locators.aos_username, locators.new_password)
        methods.teardown()
