import urlparse

from tests.components import AuthForm, TopMenu, CreateForm, Topic


class Page(object):
    BASE_URL = 'http://ftest.stud.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

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

    @property
    def form(self):
        return CreateForm(self.driver)


class TopicPage(Page):
    @property
    def topic(self):
        return Topic(self.driver)


class BlogPage(Page):
    @property
    def topic(self):
        return Topic(self.driver)