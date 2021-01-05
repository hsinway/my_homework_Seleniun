from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from wechat_Sun.pageObject.add_member_page import AddMemberPage
from wechat_Sun.pageObject.base_page import BasePage
from wechat_Sun.pageObject.contact_page import ContactPage


class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # 这里需要加*解元组为两个元素,第一个元素为第一参数,第二个元素为第二参数传入
        self.find(*self._location_goto_member).click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def back_to_main(self):
        self.find(By.ID, "menu_index").click()
        ele = self.finds((By.CSS_SELECTOR, "a[node-type='cancel'"))
        if len(ele) == 1:
            self.find((By.CSS_SELECTOR, "a[node-type='cancel'")).click()
