import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


def wait_for(locator):
    return WebDriverWait(browser, 1).until(
        EC.presence_of_element_located(locator))


main_hashtag = "dog"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

header = wait_for((By.TAG_NAME, "header"))

search_bar = browser.find_element_by_class_name("XTCLo")
search_bar.send_keys("#", main_hashtag)
search_bar.send_keys(Keys.ENTER)

header = WebDriverWait(browser, 1).until(
    EC.presence_of_element_located((By.CLASS_NAME, "drKGC")))
hashtags = header.find_elements_by_class_name("Ap253")
links = header.find_elements_by_class_name("yCE8d")


for link in links[:10]:
    browser.execute_script(
        '''
      const add = arguments[0]
      window.open(add, "_blank");
      ''',
        link
    )

counted_hashtags = []
used_hashtags = []

for window in browser.window_handles:
    # * browser.window_handles : 브라우저에 열려있는 tab들의 list array
    browser.switch_to.window(window)
    hashtag_name = wait_for((By.TAG_NAME, "h1"))
    post_count = wait_for((By.CLASS_NAME, "g47SY"))
    if post_count:
        post_count = int(post_count.text.replace(",", ""))
    if hashtag_name:
        hashtag_name = hashtag_name.text[1:]
    if hashtag_name and post_count:
        if hashtag_name not in used_hashtags:
            counted_hashtags.append((hashtag_name, post_count))
            used_hashtags.append(hashtag_name)

for window in browser.window_handles[0:-1]:
    browser.switch_to.window(window)
    browser.close()

print(counted_hashtags)
