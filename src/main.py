

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import os 
import constants as const


class Driver():
    def __init__(self):
        super (Driver, self).__init__()
        self.now = datetime.now()
        self.mm__dd__yyyy = self.now.strftime("%m%d%Y")
        self.options = Options()
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--start-maximized")
        self.options.headless = True
        self.service = Service(executable_path=const.WEBDRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service, options=self.options) 
        self.driver.get(const.URL)

        print("Welcome to Crypto-Top10 Automation")
        print("...")
        print("Initializing Server...")

        self.driver.implicitly_wait(25)
        print("Server Initialized")
        print("Updating Currency...")
        print("(This may take a while...)")

        self.currency_change()


    def currency_change(self):
            self.dropdown = self.driver.find_element(by='xpath', value=const.currency_dropdown)
            self.dropdown.click()
            self.driver.implicitly_wait(5)
            self.search = self.driver.find_element(by='xpath', value=const.currency_search)
            self.search.send_keys("PHP")
            self.driver.implicitly_wait(3)
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, const.currency_php)
                )
            )

    def collecting(self):
        index = 0
        coin_count = 1
        while index <= 9:           
            coin = self.driver.find_element(by='xpath', value=const.COINS[index])
            coin.click()
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, const.value)
                )
            )
            self.driver.implicitly_wait(3)
            self.coin_text = self.driver.find_element(by='xpath', value=const.coin).text
            self.coin_value = self.driver.find_element(by='xpath', value=const.value).text
            self.coin_trend = self.driver.find_element(by='xpath', value=const.trend).text
            coins.append(self.coin_text)
            values.append(self.coin_value)
            trends.append(self.coin_trend)
            print(f'{coin_count}/10 collected')
            self.currency_change()
            self.driver.back()
            self.driver.implicitly_wait(7)
            coin_count += 1
            index += 1
            if index == 10:
                break

driver_init = Driver()

final_currency = driver_init.driver.find_element(by='xpath', value=const.currency_php)
final_currency.click()
print("Currency successfully changed to PHP.")


print("Collecting Cryptocurrencies...")
coins = []
values = []
trends = []
driver_init.collecting()

csv_path = "/Users/robertbailey/Documents/Crpyto-Top10-csv's"
collection = {"Coins": coins, "Values": values, "Extras": trends}
df_collection = pd.DataFrame(collection)
file_name = f'Crypto-Top10{driver_init.mm__dd__yyyy}.csv'
complete_path = os.path.join(csv_path, file_name)
df_collection.to_csv(complete_path, index=False)

print("File has been successfully created.")
print("Thank you for using Crypto Top-10 Automation!")
driver_init.driver.quit()


