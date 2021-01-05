from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wechat_Sun.pageObject.base_page import BasePage
from wechat_Sun.pageObject.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 私有变量,不暴露PO设计内部的元素给外部访问
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID, "memberAdd_acctid")
    _location_phone = (By.ID, "memberAdd_phone")
    _location_save = (By.CSS_SELECTOR, ".js_btn_save")
    _location_error_msg = (By.XPATH, '//*[@class="ww_inputWithTips_tips"]')

    def add_member(self):
        """
        添加成员操作
        :return:
        """
        # 加*解元组
        self.driver.find_element(*self._location_username).send_keys("username")
        self.driver.find_element(*self._location_acctid).send_keys("account1")
        self.driver.find_element(*self._location_phone).send_keys("12312341234")
        self.find(self._location_save).click()
        return ContactPage(self.driver)

    def add_member_fail(self, acctid, phone):
        """
        添加成员失败
        :return:
        """

        self.find(self._location_username).send_keys("username")
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        self.driver.find_element(*self._location_phone).send_keys(phone)
        self.wait_clickable(self._location_save)
        self.find(self._location_save).click()
        # sleep(1)
        # account_error_message = self.driver.find_element(By.CSS_SELECTOR,
        #                                                  ".member_edit_item.member_edit_item_Account .ww_inputWithTips_tips").text
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(self._location_error_msg))
        # res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        res = self.finds(self._location_error_msg)
        # print(res)
        # is_displayed_list = [i.is_displayed() for i in res]
        # print(is_displayed_list)
        error_message_list = [i.text for i in res]
        print(error_message_list)
        return error_message_list
        # return ContactPage(self.driver)
