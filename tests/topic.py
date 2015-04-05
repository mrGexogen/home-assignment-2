# coding=utf-8
import os
from time import sleep
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

    def setUp(self):
        browser = os.environ.get("TTHA2BROWSER", "CHROME")
        self.driver = webdriver.Remote(desired_capabilities=getattr(DesiredCapabilities, browser))
        self.TOPIC_PAGE = TopicPage(self.driver)

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(self.USER_EMAIL, self.USER_PASSWD)
        self.create_page = CreatePage(self.driver)
        self.create_page.open()

    def tearDown(self):
        self.TOPIC_PAGE.topic.delete()
        self.driver.quit()

    def test_create_simple_topic(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TITLE, self.TOPIC_PAGE.topic.get_title())
        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text(""))

    def test_create_bold(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.bold()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/strong"))

    def test_create_italic(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.italic()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/em"))

    def test_create_stroke(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.stroke()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/s"))

    def test_create_underline(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.underline()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/u"))

    # после клика на quote каретка устанавливается в конце <blockquote></blockquote>
    # по сравнению с остальными кнопками - баг
    def test_create_blockquote(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.quote()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        # self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/blockquote"))
        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text(""))

    def test_create_code(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.code()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/code"))

    def test_create_ul(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.ul()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/ul/li"))

    def test_create_ol(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.ol()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/ol/li"))

    def test_create_h4(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.h4()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/h4"))

    def test_create_h5(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.h5()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/h5"))

    def test_create_h6(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.editor.h6()
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text("/h6"))

    def test_create_img_upload(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.img()
        self.create_page.form.img_menu.set_img("img/logo.png")
        self.create_page.form.img_menu.set_title_local(self.TITLE)
        self.create_page.form.img_menu.submit_local()

        sleep(0.1)  # Element is not clickable at point - chromedriver's bug
        self.create_page.form.submit()

        self.assertIsNotNone(self.TOPIC_PAGE.topic.get_img_src())

    def test_create_img_remote(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.img()
        self.create_page.form.img_menu.img_src_remote()
        self.create_page.form.img_menu.set_img_url("ftest.stud.tech-mail.ru/media/site/logo_1.png")
        self.create_page.form.img_menu.set_title_remote(self.TITLE)
        self.create_page.form.img_menu.submit_remote()

        sleep(0.5)  # Element is not clickable at point - chromedriver's bug
        self.create_page.form.submit()

        self.assertIsNotNone(self.TOPIC_PAGE.topic.get_img_src())

    def test_create_img_remote_link(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.img()
        self.create_page.form.img_menu.img_src_remote()
        self.create_page.form.img_menu.set_img_url("ftest.stud.tech-mail.ru/media/site/logo_1.png")
        self.create_page.form.img_menu.set_title_remote(self.TITLE)
        self.create_page.form.img_menu.submit_remote_link()

        sleep(0.5)  # Element is not clickable at point - chromedriver's bug
        self.create_page.form.submit()

        self.assertEqual("http://ftest.stud.tech-mail.ru/media/site/logo_1.png", self.TOPIC_PAGE.topic.get_img_src())

    # выравнивание по центру не отлиается от нет и слева - баг
    def test_create_img_upload_align(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.img()
        self.create_page.form.img_menu.set_img("img/logo.png")
        self.create_page.form.img_menu.set_title_local(self.TITLE)
        self.create_page.form.img_menu.align_open_local()
        self.create_page.form.img_menu.align_select_local('по центру')
        self.create_page.form.img_menu.submit_local()

        sleep(0.1)  # Element is not clickable at point - chromedriver's bug
        self.create_page.form.submit()

        self.assertEqual('center', self.TOPIC_PAGE.topic.get_img_align())

    def test_create_img_remote_align(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.img()
        self.create_page.form.img_menu.img_src_remote()
        self.create_page.form.img_menu.set_img_url("ftest.stud.tech-mail.ru/media/site/logo_1.png")
        self.create_page.form.img_menu.set_title_remote(self.TITLE)
        self.create_page.form.img_menu.align_open_remote()
        self.create_page.form.img_menu.align_select_remote('по центру')
        self.create_page.form.img_menu.submit_remote()

        sleep(0.5)  # Element is not clickable at point - chromedriver's bug
        self.create_page.form.submit()

        self.assertEqual('center', self.TOPIC_PAGE.topic.get_img_align())

    def test_create_img_remote_link_align(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.img()
        self.create_page.form.img_menu.img_src_remote()
        self.create_page.form.img_menu.set_img_url("ftest.stud.tech-mail.ru/media/site/logo_1.png")
        self.create_page.form.img_menu.set_title_remote(self.TITLE)
        self.create_page.form.img_menu.set_title_remote(self.TITLE)
        self.create_page.form.img_menu.align_open_remote()
        self.create_page.form.img_menu.align_select_remote('по центру')
        self.create_page.form.img_menu.submit_remote_link()

        sleep(0.5)  # Element is not clickable at point - chromedriver's bug
        self.create_page.form.submit()

        self.assertEqual('center', self.TOPIC_PAGE.topic.get_img_align())

    def test_create_link(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.link()
        self.create_page.form.link_input.set_link("http://ya.ru/")
        self.create_page.form.link_input.submit()

        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.submit()

        self.assertEqual(self.TEXT, self.TOPIC_PAGE.topic.get_text('/a'))
        self.assertEqual("http://ya.ru/", self.TOPIC_PAGE.topic.get_link())

    def test_create_user(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)

        self.create_page.form.editor.user()
        self.create_page.form.user_input.set_search(u"Котегов")
        self.create_page.form.user_input.choose_user()

        self.create_page.form.submit()

        self.assertEqual(u'Дмитрий Котегов', self.TOPIC_PAGE.topic.get_text('/a'))
        self.assertEqual(u"http://ftest.stud.tech-mail.ru/profile/dm.kotegov/", self.TOPIC_PAGE.topic.get_link())

    def test_create_no_comment(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.set_main_text(self.TEXT)
        self.create_page.form.toggle_comment()
        self.create_page.form.submit()

        self.assertFalse(self.TOPIC_PAGE.topic.is_comment_present())

    def test_create_poll(self):
        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(self.TITLE)
        self.create_page.form.set_main_text(self.TEXT)

        self.create_page.form.toggle_poll()
        self.create_page.form.poll.set_question("Question")
        self.create_page.form.poll.set_answer(0, "Answer 1")
        self.create_page.form.poll.set_answer(1, "Answer 2")

        self.create_page.form.submit()

        self.assertTrue(self.TOPIC_PAGE.topic.is_answer_present())