from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get("https://repl.it/login")

username_input = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div[3]/div[2]/div/div[2]/form/div[1]/div/div/input"
)
password_input = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div[3]/div[2]/div/div[2]/form/div[2]/div/div/div/input"
)
login_btn = browser.find_element_by_class_name("jsx-3955410531")

username_input.send_keys("serranoarevalo")
password_input.send_keys(input("What is your password?"))
login_btn.click()
