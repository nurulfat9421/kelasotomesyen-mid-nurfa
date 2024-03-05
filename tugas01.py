
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()


#driver.minimize_window()

site=['Tiket','Tokopedia','Orang Siber','Demo QA','The Boring Stuff']
print("GET SITE TITLE \n")

for i in site:
    if i=='Tiket':
        driver.get('https://tiket.com')
        print(f"Tiket : {driver.title}")
        sleep(3)
    elif i=='Tokopedia':
        driver.get('https://tokopedia.com')
        print(f"Tokopedia : {driver.title}")
        sleep(3)
    elif i=='Orang Siber':
        driver.get('https://orangsiber.com')
        print(f"Orang Siber : {driver.title}")
        sleep(3)
    elif i=='Demo QA':
        driver.get('https://demoqa.com')
        print(f"Demo QA : {driver.title}")
        sleep(3)
    elif i=='The Boring Stuff':
        driver.get('https://automatetheboringstuff.com')
        print(f"The Boring Stuff : {driver.title}")
        sleep(3)

driver.close()
