from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType

from codepen import get_codepen_data

DATA_FILE = "links.txt"
OUTPUT_FILE = 'output.txt'

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path="./geckodriver")

# set loding time for website & send request
driver.implicitly_wait(10)

with open(OUTPUT_FILE, 'a') as write_file:
    i = 1
    with open(DATA_FILE) as read_file:
        for url in read_file:
            URL = url.replace('\n', '')

            codepen_data = get_codepen_data(driver, URL)

            write_file.write(f"{URL}\n")
            write_file.write(f"Title : {codepen_data['title']}\n")
            write_file.write(f"Author : {codepen_data['author-name']}\n")
            write_file.write(f"Made with : {codepen_data['made-with']}\n")
            write_file.write(
                f"Created date : {codepen_data['created-date']}\n")
            write_file.write("\n\n\n\n")

            print(f"{i} ✅")
            i += 1

    driver.close()
