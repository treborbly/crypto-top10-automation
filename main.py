

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import os 
import constants as const


now = datetime.now()
mm_dd_yyyy = now.strftime("%m%d%Y")


service = Service(executable_path=const.WEBDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(const.URL)
print('Welcome to Crypto-Top10 Automation')
print('...')
print('...')
print('Initializing Server...')


driver.implicitly_wait(25)

print('Server Initialized.')
print('Updating Currency...')
print('(this may take a while...)')
def currency_change():
    dropdown = driver.find_element(by='xpath', value=const.currency_dropdown)
    dropdown.click()
    driver.implicitly_wait(5)
    search = driver.find_element(by='xpath', value=const.currency_search)
    search.send_keys("PHP")
    driver.implicitly_wait(3)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, const.currency_php)
        )
    )
currency_change()


final_currency = driver.find_element(by='xpath', value=const.currency_php)
final_currency.click()
print('Currency successfully changed to PHP.')


print('Collecting Cryptocurrencies...')
coins = []
values = []
trends = []

def collecting():
    coin_one = driver.find_element(by='xpath', value=const.COINS["Coin 1"])
    coin_one.click()
    driver.implicitly_wait(10)
    coin_one_text = driver.find_element(by='xpath', value=const.coin).text
    coin_one_value = driver.find_element(by='xpath', value=const.value).text
    coin_one_trend = driver.find_element(by='xpath', value=const.trend).text
    print("1/10")
    coins.append(coin_one_text)
    values.append(coin_one_value)
    trends.append(coin_one_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_two = driver.find_element(by='xpath', value=const.COINS["Coin 2"])
    coin_two.click()
    driver.implicitly_wait(10)
    coin_two_text = driver.find_element(by='xpath', value=const.coin).text
    coin_two_value = driver.find_element(by='xpath', value=const.value).text
    coin_two_trend = driver.find_element(by='xpath', value=const.trend).text
    print("2/10")
    coins.append(coin_two_text)
    values.append(coin_two_value)
    trends.append(coin_two_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_three = driver.find_element(by='xpath', value=const.COINS["Coin 3"])
    coin_three.click()
    driver.implicitly_wait(10)
    coin_three_text = driver.find_element(by='xpath', value=const.coin).text
    coin_three_value = driver.find_element(by='xpath', value=const.value).text
    coin_three_trend = driver.find_element(by='xpath', value=const.trend).text
    print("3/10")
    coins.append(coin_three_text)
    values.append(coin_three_value)
    trends.append(coin_three_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_four = driver.find_element(by='xpath', value=const.COINS['Coin 4'])
    coin_four.click()
    driver.implicitly_wait(10)
    coin_four_text = driver.find_element(by='xpath', value=const.coin).text
    coin_four_value = driver.find_element(by='xpath', value=const.value).text
    coin_four_trend = driver.find_element(by='xpath', value=const.trend).text
    print("4/10")
    coins.append(coin_four_text)
    values.append(coin_four_value)
    trends.append(coin_four_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_five = driver.find_element(by='xpath', value=const.COINS["Coin 5"])
    coin_five.click()
    driver.implicitly_wait(10)
    coin_five_text = driver.find_element(by='xpath', value=const.coin).text
    coin_five_value = driver.find_element(by='xpath', value=const.value).text
    coin_five_trend = driver.find_element(by='xpath', value=const.trend).text
    print("5/10")
    coins.append(coin_five_text)
    values.append(coin_five_value)
    trends.append(coin_five_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_six = driver.find_element(by='xpath', value=const.COINS["Coin 6"])
    coin_six.click()
    driver.implicitly_wait(10)
    coin_six_text = driver.find_element(by='xpath', value=const.coin).text
    coin_six_value = driver.find_element(by='xpath', value=const.value).text
    coin_six_trend = driver.find_element(by='xpath', value=const.trend).text
    print("6/10")
    coins.append(coin_six_text)
    values.append(coin_six_value)
    trends.append(coin_six_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_seven = driver.find_element(by='xpath', value=const.COINS['Coin 7'])
    coin_seven.click()
    driver.implicitly_wait(10)
    coin_seven_text = driver.find_element(by='xpath', value=const.coin).text
    coin_seven_value = driver.find_element(by='xpath', value=const.value).text
    coin_seven_trend = driver.find_element(by='xpath', value=const.trend).text
    print("7/10")
    coins.append(coin_seven_text)
    values.append(coin_seven_value)
    trends.append(coin_seven_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_eight = driver.find_element(by='xpath', value=const.COINS["Coin 8"])
    coin_eight.click()
    driver.implicitly_wait(10)
    coin_eight_text = driver.find_element(by='xpath', value=const.coin).text
    coin_eight_value = driver.find_element(by='xpath', value=const.value).text
    coin_eight_trend = driver.find_element(by='xpath', value=const.trend).text
    print("8/10")
    coins.append(coin_eight_text)
    values.append(coin_eight_value)
    trends.append(coin_eight_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_nine = driver.find_element(by='xpath', value=const.COINS["Coin 9"])
    coin_nine.click()
    driver.implicitly_wait(10)
    coin_nine_text = driver.find_element(by='xpath', value=const.coin).text
    coin_nine_value = driver.find_element(by='xpath', value=const.value).text
    coin_nine_trend = driver.find_element(by='xpath', value=const.trend).text
    print("9/10")
    coins.append(coin_nine_text)
    values.append(coin_nine_value)
    trends.append(coin_nine_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    coin_ten = driver.find_element(by='xpath', value=const.COINS["Coin 10"])
    coin_ten.click()
    driver.implicitly_wait(10)
    coin_ten_text = driver.find_element(by='xpath', value=const.coin).text
    coin_ten_value = driver.find_element(by='xpath', value=const.value).text
    coin_ten_trend = driver.find_element(by='xpath', value=const.trend).text
    print("10/10")
    coins.append(coin_ten_text)
    values.append(coin_ten_value)
    trends.append(coin_ten_trend)
    driver.back()
    currency_change()

    driver.implicitly_wait(5)

    print("Cryptocurrencies successfully collected.")

    
collecting()

csv_path = "/Users/robertbailey/Documents/Crpyto-Top10-csv's"
collection = {"Coins": coins, "Values": values, "Extras": trends}
df_collection = pd.DataFrame(collection)

file_name = f'Crypto-Top10{mm_dd_yyyy}.csv'
complete_path = os.path.join(csv_path, file_name)
df_collection.to_csv(complete_path)

print("File has been successfully created.")
print("Thank you for using Crypto Top-10 Automation!")


driver.quit()


