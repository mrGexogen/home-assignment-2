# coding=utf-8
import urlparse

from selenium.webdriver.support.wait import WebDriverWait

from components import AuthForm, TopMenu, CreateForm, Topic


class Page(object):
    BASE_URL = 'http://ftest.stud.tech-mail.ru/'
    PATH = ''
    WAIT_COND = '//a[contains(text(),"Вход для участников")]'

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.WAIT_COND)
        )

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    def login(self, login, password):
        self.form.open_form()
        self.form.set_login(login)
        self.form.set_password(password)
        self.form.submit()


class CreatePage(Page):
    PATH = '/blog/topic/create/'
    WAIT_COND = '//a[@id="modal_write_show"]'

    @property
    def form(self):
        return CreateForm(self.driver)

    def open(self):
        self.wait()
        super(CreatePage, self).open()


class TopicPage(Page):
    @property
    def topic(self):
        return Topic(self.driver)


class BlogPage(Page):
    @property
    def topic(self):
        return Topic(self.driver)