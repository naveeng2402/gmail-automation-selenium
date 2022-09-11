from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InitialPage:
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver

        self.username_error = None
        self.password_error = None

        self.get_inputs()

    def get_inputs(self) -> None:
        self.first_name = self.driver.find_element(by=By.NAME, value="firstName")
        self.last_name = self.driver.find_element(by=By.NAME, value="lastName")
        self.user_name = self.driver.find_element(by=By.NAME, value="Username")
        self.password = self.driver.find_element(by=By.NAME, value="Passwd")
        self.confirm_password = self.driver.find_element(
            by=By.NAME, value="ConfirmPasswd"
        )

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        user_name: str,
        password: str,
        confirm_password: str,
    ) -> None:
        self.first_name.clear()
        self.first_name.send_keys(first_name)

        self.last_name.clear()
        self.last_name.send_keys(last_name)

        self.user_name.clear()
        self.user_name.send_keys(user_name)

        self.password.clear()
        self.password.send_keys(password)

        self.confirm_password.clear()
        self.confirm_password.send_keys(confirm_password)
        self.confirm_password.send_keys(Keys.RETURN)

    def get_errors(self):
        self.username_error = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div",
        ).text
        self.password_error = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[2]/div[2]/span",
        ).text
        # print(self.username_error.text)


if __name__ == "__main__":
    from selenium.webdriver.chrome.service import Service
    import os

    URL = "https://accounts.google.com/signup"

    driver = Chrome(service=Service(os.path.join("..", "bin", "chromedriver")))
    driver.implicitly_wait(10)

    driver.get(URL)

    init_page = InitialPage(driver)
    init_page.fill_form(
        first_name="",
        last_name="",
        user_name="",
        password="",
        confirm_password="",
    )
    try:
        init_page.get_errors()
    except:
        pass

    sleep(5)

    driver.quit()
