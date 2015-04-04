# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class TopMenu(Component):
    USERNAME = '//a[@class="username"]'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )


class CreateForm(Component):
    BLOGSELECT = '//a[@class="chzn-single"]'
    OPTION = '//li[text()="{}"]'
    TITLE = '//input[@name="title"]'
    SHORT_TEXT = '//textarea[@name="text_short"]'
    MAIN_TEXT = '//textarea[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_short_text(self, short_text):
        self.driver.find_element_by_xpath(self.SHORT_TEXT).send_keys(short_text)

    def set_main_text(self, main_text):
        self.driver.find_element_by_xpath(self.MAIN_TEXT).send_keys(main_text)

    def submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()


class Topic(Component):
    TITLE = '//*[@class="topic-title"]/a'
    TEXT = '//*[@class="topic-content text"]/p'
    BLOG = '//*[@class="topic-blog"]'
    DELETE_BUTTON = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def get_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT).text
        )

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM).click()
