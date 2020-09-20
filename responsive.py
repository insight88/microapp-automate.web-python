from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ResponsiveTester:

    def __init__(self, urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [960, 1920]

    def screenshot(self, url):

        BROWSER_HEIGHT = 1096
        self.browser.get(url)

        for size in sizes:
        self.browser.set_window_size(size, BROWSER_HEIGHT)
        self.browser.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)
        scroll_size = self.browser.execute_script(
            "return document.body.scrollHeight")
        total_sections = ceil(scroll_size / BROWSER_HEIGHT)

        for section in range(total_sections+1):
            self.browser.execute_script(
                f"window.scrollTo(0, {(section) * BROWSER_HEIGHT})")
            self.browser.save_screenshot(f"screenshots/{size}x{section+1}.png")
            time.sleep(1)

    def start(self):
        for url in urls:
            self.screenshot(url)


# BROWSER_HEIGHT = 1096

# browser = webdriver.Chrome(ChromeDriverManager().install())

# browser.get("https://nomadcoders.co")
# browser.maximize_window()

# sizes = [960, 1920]

# for size in sizes:
#     browser.set_window_size(size, BROWSER_HEIGHT)
#     browser.execute_script("window.scrollTo(0, 0)")
#     time.sleep(1)
#     scroll_size = browser.execute_script("return document.body.scrollHeight")
#     # ! browser.execute_script()는 python -> javascript로 명령어를 보낸다
#     # ! browser.execute_sceript(return "")은 javascript -> python으로 값을 반환한다
#     total_sections = ceil(scroll_size / BROWSER_HEIGHT)
#     for section in range(total_sections+1):
#         browser.execute_script(
#             f"window.scrollTo(0, {(section) * BROWSER_HEIGHT})")
#         browser.save_screenshot(f"screenshots/{size}x{section+1}.png")
#         time.sleep(1)
