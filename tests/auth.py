# coding=utf-8
import os
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from tests.components import TopMenu
from tests.page_obj import AuthPage


class AuthTest(TestCase):
    USER_NAME = u"Дядя Митяй"
    USER_EMAIL = "ftest9@tech-mail.ru"
    USER_PASSWD = os.getenv('TTHA2PASSWORD')

    def setUp(self):
        browser = os.environ.get("TTHA2BROWSER", "CHROME")
        self.driver = webdriver.Remote(desired_capabilities=getattr(DesiredCapabilities, browser))

    def tearDown(self):
        self.driver.quit()

    def test_auth(self):
        page = AuthPage(self.driver)
        page.open()
        page.login(self.USER_EMAIL, self.USER_PASSWD)
        username = TopMenu(self.driver).get_username()
        self.assertEqual(username, self.USER_NAME)