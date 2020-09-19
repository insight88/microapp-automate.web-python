from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# ? webdriver : 브라우저 동작을 컨트롤하는 모듈
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = "buy domain"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")
# * find_element_by_class_name() : return WebElement
search_bar.send_keys("hello!")
# * WebElement.send_keys("string")
search_bar.send_keys(Keys.ENTER)

shitty_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "liYKde")))

print(shitty_element)

# search_results = browser.find_elements_by_class_name("g")

# for index, search_result in enumerate(search_results):
#     # ? enumerate(iterable) : return indexed list (1, seq[1]), (2, seq[2]) ...
#     search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
