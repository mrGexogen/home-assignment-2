# coding=utf-8
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present, invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, xpath):
        return self.driver.find_element_by_xpath(xpath)


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
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )


class CreateForm(Component):
    BLOGSELECT = '//a[@class="chzn-single"]'
    OPTION = '//li[text()="{}"]'
    TITLE = '//input[@name="title"]'
    MAIN_TEXT = '//textarea[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'
    COMMENT = '//input[@id="id_forbid_comment"]'
    POLL = '//input[@name="add_poll"]'

    def blog_select_open(self):
        self.find(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.find(self.OPTION.format(option_text)).click()

    def set_title(self, title):
        self.find(self.TITLE).send_keys(title)

    def set_main_text(self, main_text):
        self.find(self.MAIN_TEXT).send_keys(main_text)

    def submit(self):
        self.find(self.CREATE_BUTTON).click()

    def toggle_comment(self):
        self.find(self.COMMENT).click()

    def toggle_poll(self):
        self.find(self.POLL).click()

    @property
    def editor(self):
        return EditorMenu(self.driver)

    @property
    def img_menu(self):
        return ImgMenu(self.driver)

    @property
    def link_input(self):
        return LinkInput(self.driver)

    @property
    def user_input(self):
        return UserInput(self.driver)

    @property
    def poll(self):
        return Poll(self.driver)


class Poll(Component):
    QUESTION = '//input[@id="id_question"]'
    ANSWER = '//input[@id="id_form-{}-answer"]'

    def set_question(self, question):
        self.find(self.QUESTION).send_keys(question)

    def set_answer(self, index, answer):
        self.find(self.ANSWER.format(index)).send_keys(answer)


class UserInput(Component):
    INPUT = '//input[@id="search-user-login-popup"]'
    USER = '//tbody[@id="list-body"]/descendant::p[@class="realname"]/a[@class="user_profile_path"]'

    def set_search(self, name):
        self.find(self.INPUT).send_keys(name)

    def choose_user(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USER)
        )
        self.find(self.USER).click()


class LinkInput(Component):
    def __init__(self, driver):
        super(LinkInput, self).__init__(driver)
        WebDriverWait(self.driver, 5, 0.1).until(alert_is_present())
        self._alert = self.driver.switch_to_alert()

    def set_link(self, link):
        self._alert.send_keys(link)

    def submit(self):
        self._alert.accept()


class EditorMenu(Component):
    _menu_key = '//div[@class="blogs"]/descendant::li[contains(@class, "editor-{}")]/a'

    H4 = _menu_key.format("h4")
    H5 = _menu_key.format("h5")
    H6 = _menu_key.format("h6")
    BOLD = _menu_key.format("bold")
    ITALIC = _menu_key.format("italic")
    STROKE = _menu_key.format("stroke")
    UNDERLINE = _menu_key.format("underline")
    QUOTE = _menu_key.format("quote")
    CODE = _menu_key.format("code")
    UL = _menu_key.format("ul")
    OL = _menu_key.format("ol")
    IMG = _menu_key.format("picture")
    LINK = _menu_key.format("link")
    USER = _menu_key.format("user")

    def h4(self):
        self.find(self.H4).click()

    def h5(self):
        self.find(self.H5).click()

    def h6(self):
        self.find(self.H6).click()

    def bold(self):
        self.find(self.BOLD).click()

    def italic(self):
        self.find(self.ITALIC).click()

    def stroke(self):
        self.find(self.STROKE).click()

    def underline(self):
        self.find(self.UNDERLINE).click()

    def quote(self):
        self.find(self.QUOTE).click()

    def code(self):
        self.find(self.CODE).click()

    def ul(self):
        self.find(self.UL).click()

    def ol(self):
        self.find(self.OL).click()

    def img(self):
        self.find(self.IMG).click()

    def link(self):
        self.find(self.LINK).click()

    def user(self):
        self.find(self.USER).click()


class ImgMenu(Component):
    IMG_INPUT = '//input[@id="img_file"]'
    IMG_URL = '//input[@id="img_url"]'
    IMG_TITLE = '//input[@id="{}"]'
    SUBMIT = '//button[@id="{}"]'
    ALIGN = '//select[@id="{}"]'
    ALIGN_OPT = ALIGN + '/option[contains(text(),"{}")]'
    IMG_SRC = '//a[contains(text(),"{}")]'

    def _img_input(self, src):
        self.find(self.IMG_SRC.format(src)).click()

    def img_input_local(self):
        self._img_input("С компьютера")

    def img_input_remote(self):
        self._img_input("Из интернета")

    def set_img(self, img):
        self.find(self.IMG_INPUT).send_keys(os.path.abspath(img))

    def set_img_url(self, url):
        self.find(self.IMG_URL).send_keys(url)

    def _set_title(self, title, dst):
        self.find(self.IMG_TITLE.format(dst)).send_keys(title)

    def set_title_local(self, title):
        self._set_title(title, "form-image-title")

    def set_title_remote(self, title):
        self._set_title(title, "form-image-url-title")

    def _submit(self, dst):
        self.find(self.SUBMIT.format(dst)).click()
        WebDriverWait(self.driver, 5, 0.1).until(
            invisibility_of_element_located((By.XPATH, '//div[@id="window_upload_img"]'))
        )

    def submit_local(self):
        self._submit('submit-image-upload')

    def submit_remote(self):
        self._submit('submit-image-upload-link-upload')

    def submit_remote_link(self):
        self._submit('submit-image-upload-link')

    def _align_open(self, dst):
        self.find(self.ALIGN.format(dst)).click()

    def align_open_local(self):
        self.find(self.ALIGN.format('form-image-align')).click()

    def align_open_remote(self):
        self.find(self.ALIGN.format('form-image-url-align')).click()

    def _align_select(self, dst, align):
        self.find(self.ALIGN_OPT.format(dst, align)).click()

    def align_select_local(self, align):
        self.find(self.ALIGN_OPT.format('form-image-align', align)).click()

    def align_select_remote(self, align):
        self.find(self.ALIGN_OPT.format('form-image-url-align', align)).click()


class Topic(Component):
    TITLE = '//*[@class="topic-title"]/a'
    TEXT = '//*[@class="topic-content text"]{}'
    DELETE_BUTTON = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'
    COMMENT = '//a[@class="comment-add-link link-dotted"]'
    ANSWER = '//input[@class="answer"]'

    def get_title(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def get_text(self, tag):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format(tag)).text
        )

    def get_tag_attr(self, tag, attr):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format(tag)).get_attribute(attr)
        )

    def delete(self):
        try:
            self.find(self.DELETE_BUTTON).click()
            self.find(self.DELETE_BUTTON_CONFIRM).click()
        except NoSuchElementException:
            pass

    def is_comment_present(self):
        try:
            self.find(self.COMMENT)
        except NoSuchElementException:
            return False
        return True

    def is_answer_present(self):
        try:
            self.find(self.ANSWER)
        except NoSuchElementException:
            return False
        return True
