from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os

def write(x, content):
    x.clear
    x.send_keys(content)
    x.send_keys(Keys.RETURN)

def copyFile(recive, send):
    f = open(send, "r")
    f1 = open(recive, "w")
    for line in f:
        f1.write(line)

target_user = ""
attacker_user = ""
attacker_pswrd = ""

chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)
driver.get("https://www.instagram.com/" + target_user)
driver.implicitly_wait(20)

followers_button = driver.find_element("xpath", "(//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade'])[2]")
followers_button.click()
driver.implicitly_wait(20)
user_field = driver.find_element("xpath", "(//input[contains(@name,'username')])[1]")
write(user_field, attacker_user)
pswrd_field = driver.find_element("xpath", "(//input[@name='password'])[1]")
write(pswrd_field, attacker_pswrd)
notif_button = driver.find_element("xpath", "//button[normalize-space()='Ahora no']")
notif_button.click()
driver.implicitly_wait(20)
new_followers_button = driver.find_element("xpath", "(//div[contains(@class,'_aacl _aacp _aacu _aacx _aad6 _aade')])[2]")
new_followers_button.click()
amount_followers = driver.find_element("xpath", "(//ul[contains(@class,'xieb3on')])[1]/li[2]/a/div/span").text

# scroll down the followers list
pop_up_window = WebDriverWait(
    driver, 2).until(EC.element_to_be_clickable(
        ("xpath", "//div[@class='_aano']")))  

for i in range(int(int(amount_followers)/6)):    
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
    pop_up_window)
    time.sleep(3)

new_followers = open("new_followers.txt", "w")
for i in range(int(amount_followers)-1):
    try:
        user = driver.find_element("xpath", "(//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np'])[" + str(i+1) + "]/div[2]/div/div/div/span/div/div/div/a/span/div")
        new_followers.write(str(i+1) + " " + user.text + "\n")
    except NoSuchElementException:
        new_followers.write("User " + str(i+1) + " not founded" + "\n")
        continue

copyFile("last_followers.txt", "new_followers.txt")
new_followers.close()

driver.quit()

#1033 -> 1200
#1325 -> 1841