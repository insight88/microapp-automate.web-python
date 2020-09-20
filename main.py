from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# ? webdriver : 브라우저 동작을 컨트롤하는 모듈
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenShooter:

    def __init__(self, keyword, screenshot_dir):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshot_dir = screenshot_dir

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        try:
            shitty_element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "kp-blk"))
            )
            self.browser.execute_script(
                """
                const shitty = arguments[0];
                shitty.parentElement.removeChild(shitty)
                """,
                shitty_element,
            )
        except Exception:
            pass
        search_results = self.browser.find_elements_by_class_name("g")
        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshot_dir}/{self.keyword}x{index}.png")

    def finish(self):
        self.browser.quit()


# domain_competitors = GoogleKeywordScreenShooter("buy domain", "screenshots")
# domain_competitors.start()
# domain_competitors.finish()
python_competitors = GoogleKeywordScreenShooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()


# KEYWORD = "hello!"
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("https://google.com")

# search_bar = browser.find_element_by_class_name("gLFyf")
# # ? find_element_by_class_name() : return WebElement
# search_bar.send_keys("hello!")
# # ? WebElement.send_keys("string")
# search_bar.send_keys(Keys.ENTER)

# shitty_element = WebDriverWait(browser, 5).until(
#     # ? WebDriverWait(browser, time) : browser가 time동안 어떤 조건을 만족할 때까지 대기
#     EC.presence_of_element_located((By.CLASS_NAME, "liYKde")))
# # ? expected_conditions.presence_of_element_located : 웹페이지의 DOM에 element가 있는지 확인

# browser.execute_script(
#     # ! .execute_script(script, *args) : javascript의 script를 *args를 이용해 실행
#     """
#     const shitty = arguments[0];
#     shitty.parentElement.removeChild(shitty)
#     """,
#     shitty_element,
#     # ? shitty_element == arguments[0], arguments는 python이 javascript에게 전달하는 인자
# )

# search_results = browser.find_elements_by_class_name("g")

# for index, search_result in enumerate(search_results):
#     # ? enumerate(iterable) : return indexed list (1, seq[1]), (2, seq[2]) ...
#     search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
