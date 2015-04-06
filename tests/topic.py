# coding=utf-8
import os
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from page_obj import AuthPage, CreatePage, TopicPage


class TopicTest(TestCase):
    USER_EMAIL = "ftest9@tech-mail.ru"
    USER_PASSWD = os.getenv('TTHA2PASSWORD')
    BLOG = 'Флудилка'
    TITLE = 'Awesome title'
    TEXT = 'Awesome text'
    IMG = "img/logo.png"
    IMG_URL = "ftest.stud.tech-mail.ru/media/site/logo_1.png"

    def setUp(self):
        self.LINK = "http://ya.ru/"
        browser = os.environ.get("TTHA2BROWSER", "CHROME")
        self.driver = webdriver.Remote(desired_capabilities=getattr(DesiredCapabilities, browser))
        self.topic = TopicPage(self.driver).topic

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(self.USER_EMAIL, self.USER_PASSWD)

        create_page = CreatePage(self.driver)
        create_page.open()

        self.form = create_page.form
        self.form.blog_select_open()
        self.form.blog_select_set_option(self.BLOG)
        self.form.set_title(self.TITLE)

    def tearDown(self):
        self.topic.delete()
        self.driver.quit()

    def test_create_simple_topic(self):
        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TITLE, self.topic.get_title())
        self.assertEqual(self.TEXT, self.topic.get_text(""))

    def test_create_bold(self):
        self.form.editor.bold()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/strong"))

    def test_create_italic(self):
        self.form.editor.italic()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/em"))

    def test_create_stroke(self):
        self.form.editor.stroke()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/s"))

    def test_create_underline(self):
        self.form.editor.underline()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/u"))

    # после клика на quote каретка устанавливается в конце <blockquote></blockquote>
    # по сравнению с остальными кнопками - баг
    def test_create_blockquote(self):
        self.form.editor.quote()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertTrue(self.topic.is_present(self.topic.TEXT.format('/blockquote')))
        self.assertEqual(self.TEXT, self.topic.get_text(""))

    def test_create_blockquote_select(self):
        self.form.set_main_text(self.TEXT)
        self.form.select_text()
        self.form.editor.quote()

        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/blockquote"))

    def test_create_code(self):
        self.form.editor.code()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/code"))

    def test_create_ul(self):
        self.form.editor.ul()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/ul/li"))

    def test_create_ol(self):
        self.form.editor.ol()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/ol/li"))

    def test_create_h4(self):
        self.form.editor.h4()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/h4"))

    def test_create_h5(self):
        self.form.editor.h5()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/h5"))

    def test_create_h6(self):
        self.form.editor.h6()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text("/h6"))

    def test_create_img_upload(self):
        self.form.editor.img()

        img_menu = self.form.img_menu
        img_menu.img_input_local()
        img_menu.set_img(self.IMG)
        img_menu.set_title_local(self.TITLE)
        img_menu.submit_local()

        self.form.submit()

        self.assertIsNotNone(self.topic.get_tag_attr("/img", "src"))

    def test_create_img_remote(self):
        self.form.editor.img()

        img_menu = self.form.img_menu
        img_menu.img_input_remote()
        img_menu.set_img_url(self.IMG_URL)
        img_menu.set_title_remote(self.TITLE)
        img_menu.submit_remote()

        self.form.submit()

        self.assertIsNotNone(self.topic.get_tag_attr("/img", "src"))

    def test_create_img_remote_link(self):
        self.form.editor.img()

        img_menu = self.form.img_menu
        img_menu.img_input_remote()
        img_menu.set_img_url(self.IMG_URL)
        img_menu.set_title_remote(self.TITLE)
        img_menu.submit_remote_link()

        self.form.submit()

        self.assertEqual("http://" + self.IMG_URL, self.topic.get_tag_attr("/img", "src"))

    # выравнивание по центру не отлиается от нет и слева - баг
    def test_create_img_upload_align(self):
        self.form.editor.img()

        img_menu = self.form.img_menu
        img_menu.img_input_local()
        img_menu.set_img(self.IMG)
        img_menu.set_title_local(self.TITLE)

        img_menu.align_open_local()
        img_menu.align_select_local('по центру')
        img_menu.submit_local()

        self.form.submit()

        self.assertEqual('center', self.topic.get_tag_attr("/img", "align"))

    def test_create_img_remote_align(self):
        self.form.editor.img()

        img_menu = self.form.img_menu
        img_menu.img_input_remote()
        img_menu.set_img_url(self.IMG_URL)
        img_menu.set_title_remote(self.TITLE)

        img_menu.align_open_remote()
        img_menu.align_select_remote('по центру')
        img_menu.submit_remote()

        self.form.submit()

        self.assertEqual('center', self.topic.get_tag_attr("/img", "align"))

    def test_create_img_remote_link_align(self):
        self.form.editor.img()

        img_menu = self.form.img_menu
        img_menu.img_input_remote()
        img_menu.set_img_url(self.IMG_URL)
        img_menu.set_title_remote(self.TITLE)

        img_menu.align_open_remote()
        img_menu.align_select_remote('по центру')
        img_menu.submit_remote_link()

        self.form.submit()

        self.assertEqual('center', self.topic.get_tag_attr("/img", "align"))

    def test_create_link(self):
        self.form.editor.link()

        link_input = self.form.link_input
        link_input.set_link(self.LINK)
        link_input.submit()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertEqual(self.TEXT, self.topic.get_text('/a'))
        self.assertEqual(self.LINK, self.topic.get_tag_attr('/a', 'href'))

    def test_create_user(self):
        self.form.editor.user()

        user_input = self.form.user_input
        user_input.set_search(u"Котегов")
        user_input.choose_user()

        self.form.submit()

        self.assertEqual(u'Дмитрий Котегов', self.topic.get_text('/a'))
        self.assertEqual(u"http://ftest.stud.tech-mail.ru/profile/dm.kotegov/", self.topic.get_tag_attr('/a', 'href'))

    def test_create_no_comment(self):
        self.form.toggle_comment()

        self.form.set_main_text(self.TEXT)
        self.form.submit()

        self.assertFalse(self.topic.is_comment_present())

    def test_create_poll(self):
        self.form.set_main_text(self.TEXT)

        self.form.toggle_poll()
        poll = self.form.poll
        poll.set_question("Question")
        poll.set_answer(0, "Answer 1")
        poll.set_answer(1, "Answer 2")

        self.form.submit()

        self.assertTrue(self.topic.is_answer_present())