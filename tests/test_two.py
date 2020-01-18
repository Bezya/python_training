# -*- config: utf-8 -*- (needed if not latin letters are used)
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import  Group

def is alert_present(wd):
    try:
        wd.switch_to_alert().text
        return true
    exept:
        return False

class   test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicity_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/...")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group_page(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd

        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group_page(wd, Group(name ="dfgdfg", header="dfgdfg", footer="dfgdfg"))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd

        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group_page(wd, Group(name="", header="", footer=""))
        self.return_to_group_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if _name_ == '_main_':
    unittest.main()






