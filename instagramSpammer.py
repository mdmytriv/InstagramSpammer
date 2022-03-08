from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def sendMessage(driver, userName, message):
    driver.get("https://www.instagram.com/direct/inbox/")
    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//button[contains(@class, 'L3NKy')]"))
    msgButton = driver.find_element(by=By.XPATH, value="//button[contains(@class, 'L3NKy')]")
    msgButton.click()

    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//input[contains(@class, 'j_2Hd')]"))
    searchInput = driver.find_element(by=By.XPATH, value="//input[contains(@class, 'j_2Hd')]")
    searchInput.send_keys(userName)

    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//div[contains(@class, '-qQT3')]"))
    foundUser = driver.find_element(by=By.XPATH, value="//div[contains(@class, '-qQT3')]")
    foundUser.click()

    nextButton = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'XfCBB')]/button[contains(@class, 'sqdOP')]")
    nextButton.click()

    WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//div[contains(@class, 'ItkAi')]/textarea"))
    textArea = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'ItkAi')]/textarea")
    textArea.send_keys(message)
    textArea.send_keys(Keys.RETURN)

    print(f'Message was sent to, {userName}.')
    return 1

username = ''
pwd = ''
message = 'Русский военный корабль, иди на ...й.'


f = open("instaUsers.txt", "r")
users = f.read().splitlines()

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")

WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//input[@name='username']"))

# assert "Python" in driver.ti
userInput = driver.find_element(by=By.XPATH, value="//input[@name='username']")
userInput.send_keys(username)
pwdInput = driver.find_element(by=By.XPATH, value="//input[@name='password']")
pwdInput.send_keys(pwd)
pwdInput.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//div[contains(@class, 'f5C5x')]"))
saveInfoBtn = driver.find_element(by=By.XPATH, value="//button[contains(@class, 'L3NKy')]")
saveInfoBtn.click()

WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//button[contains(@class, 'HoLwm')]"))
notNowBtn = driver.find_element(by=By.XPATH, value="//button[contains(@class, 'HoLwm')]")
notNowBtn.click()

for user in users:
    try:
        sendMessage(driver, user, message)
    except:
        print("An exception occurred")
    
driver.close()
