from faker import Faker
fake = Faker(locale='en_CA')
aos_url = 'https://www.advantageonlineshopping.com/#/'  #/html/body/login-modal/div/div/div[3]/sec-form
aos_title = ' Advantage Shopping'
aos_login_url = 'https://advantageonlineshopping.com/#/loginMiniTitle/'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
aos_username = "simon"[:15]
aos_password = "Dale12345"[:12]
new_username = f'{fake.user_name()}{fake.pyint(111,999)}'[:15]
email = fake.email()
new_password = fake.password()[:15]
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
order_number = "8878567635"
tracking_number = "8878543683"