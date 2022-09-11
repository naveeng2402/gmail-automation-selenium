import csv
import unittest
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import os

from gmail_pages import InitialPage


class CreateGmailTest(unittest.TestCase):
    def setUp(self) -> None:
        self.URL = "https://accounts.google.com/signup"

        self.driver = Chrome(service=Service(os.path.join("bin", "chromedriver")))
        self.driver.implicitly_wait(10)
        self.driver.get(self.URL)

    def test_first_page(self):
        page = InitialPage(self.driver)
        data = []
        with open("gmail_data.csv") as f:
            reader = csv.reader(f)
            next(reader)
            data = [row for row in reader]

        for row in data:
            page.fill_form(*row[:5])
            try:
                page.get_errors()
            except:
                pass

            print(f"\n\n")

            if row[5] == "UN":
                print(
                    f"data:{row[6]}\nelement_text={page.username_error}\nresult:{row[6] in (page.username_error)}"
                )
                self.assertTrue(
                    row[6] in page.username_error.lower(), "Invalid Username"
                )
            elif row[5] == "PW":
                print(
                    f"data:{row[6]}\nelement_text={page.password_error}\nresult:{row[6] in page.password_error}"
                )
                self.assertTrue(
                    row[6] in page.password_error.lower(), "Invalid Password"
                )
            else:
                print(
                    f"data:{row[6]}\nelement_text={page.password_error}\nresult:{row[6] in page.password_error}"
                )
                self.assertTrue(
                    row[6] in page.password_error.lower(), "Invalid Password"
                )

    def tearDown(self) -> None:
        self.driver.quit()
