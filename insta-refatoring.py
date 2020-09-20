import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

initial_hashtag = "dog"
max_hashtags = 10
browser = webdriver.Chrome(ChromeDriverManager().install())
counted_hashtags = []
used_hashtags = []


def wait_for(locator):
    return WebDriverWait(browser, 3).until(
        EC.presence_of_element_located(locator))


def clean_link(links):
    return links[1:]


def extract_data():
    hashtag_name = wait_for((By.TAG_NAME, "h1"))
    post_count = wait_for((By.CLASS_NAME, "g47SY"))
    if post_count:
        post_count = int(post_count.text.replace(",", ""))
    if hashtag_name:
        hashtag_name = clean_link(hashtag_name.text)
    if hashtag_name and post_count:
        if hashtag_name not in used_hashtags:
            counted_hashtags.append((hashtag_name, post_count))
            used_hashtags.append(hashtag_name)


def get_related(target_url):

    browser.get(target_url)
    search_bar = browser.find_element_by_class_name("XTCLo")
    search_bar.send_keys("#", initial_hashtag)
    search_bar.send_keys(Keys.ENTER)
    header = wait_for((By.CLASS_NAME, "drKGC"))
    hashtags = header.find_elements_by_class_name("Ap253")
    links = header.find_elements_by_class_name("yCE8d")

    for link in links[1:31]:
        link_name = clean_link(link.text)
        if link_name not in used_hashtags:
            browser.execute_script(
                '''
            const add = arguments[0]
            window.open(add, "_blank");
            ''',
                link
            )

    for window in browser.window_handles:
        # * browser.window_handles : 브라우저에 열려있는 tab들의 list array
        browser.switch_to.window(window)
        extract_data()

    if len(used_hashtags) < max_hashtags:
        for window in browser.window_handles[0:-1]:
            browser.switch_to.window(window)
            browser.close()
        browser.switch_to.window(browser.window_handles[0])
        get_related(browser.current_url)


get_related(f"https://www.instagram.com/explore/tags/{initial_hashtag}")

file = open(f"{initial_hashtag}-report.csv", "w")
writer = csv.writer(file)
writer.writerow(["Hashtag", "Post Count"])

for hashtag in counted_hashtags:
    writer.writerow(hashtag)

browser.quit()
