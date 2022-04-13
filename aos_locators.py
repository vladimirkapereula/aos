
from faker import Faker
fake = Faker(locale='en_CA')

aos_url = 'https://www.advantageonlineshopping.com/#/'  #/html/body/login-modal/div/div/div[3]/sec-form
aos_title = ' Advantage Shopping'
aos_login_url = 'https://advantageonlineshopping.com/#/loginMiniTitle/'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
aos_username = "simon"
aos_password = "Dale12345"[:12]
new_username = fake.user_name()
email = fake.email()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone_number = fake.phone_number()
country = fake.country()
city = fake.city()
postal_code = fake.postalcode_in_province()
state_province_region = fake.province_abbr()
address = fake.address().replace('\n','')[:49]
address1 = f'{fake.street_address()}'[:49]
address2 = f'{fake.street_address()},{city},{fake.province_abbr},{fake.postalcode_in_province},{country}'[:49]