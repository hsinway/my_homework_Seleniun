from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wechat_Sun.pageObject.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_add = (By.XPATH, "//*[@class='member_colLeft_top_addBtn']")
    _location_add_depart = (By.LINK_TEXT, "添加部门")
    _location_depart_name = (By.XPATH, "//*[@class='qui_inputText ww_inputText' and @name='name']")
    _location_depart_list = (By.LINK_TEXT, "选择所属部门")
    # 这里指定选择一个部门
    _location_depart_choose = (By.XPATH, "//*[@class='js_parent_party_name']/../..//a[text()='test']")
    _location_confirm = (By.LINK_TEXT, "确定")
    # _location_expand_button = (By.CSS_SELECTOR, "[id='1688851952198781'] > .jstree-icon")
    _location_expand_button = (By.XPATH, "//a[(text()='test')][1]/../i[@class='jstree-icon jstree-ocl']")
    _location_expand_depart = (By.XPATH,
                               "//a[(text()='test')][1]/..//*[@class='jstree-children']//a[@class='jstree-anchor']")

    def goto_add_member(self):
        # 导入模块如果不放在函数里,则会触发python循环导入的错误 cannot import xxxx
        from wechat_Sun.pageObject.add_member_page import AddMemberPage
        """
        添加成员操作
        :return:
        """
        # 添加显式等待,保证按钮可以点击
        # WebDriverWait(self.driver, 9).until(
        #     expected_conditions.element_to_be_clickable(self._location_goto_add_member))
        self.wait_clickable(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMemberPage(self.driver)

    def get_member(self):
        """
        获取成员列表,用来做断言
        :return:
        """
        # 加*解元组
        member_list = self.driver.find_elements(*self._location_member_list)

        # member_list2 = []
        # for i in member_list:
        #     member_list2.append(i.text)
        # return member_list2

        # 优化,列表推导式
        member_list_res = [i.text for i in member_list]
        return member_list_res

    def add_department(self):
        # 1.打开添加部门
        self.find(self._location_add).click()
        self.find(self._location_add_depart).click()
        # 2.输入新部门名称选择归属部门
        self.find(self._location_depart_name).send_keys("test_department_1")
        self.find(self._location_depart_list).click()
        self.find(self._location_depart_choose).click()
        self.find(self._location_confirm).click()
        # 3.刷新页面并点开test部门列表
        self.driver.refresh()
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.(self._location_expand_button))
        self.wait_clickable(self._location_expand_button)
        self.find(self._location_expand_button).click()
        # 显式等待test部门下所有的部门is_displayed=True
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(self._location_expand_depart))
        # 4.获取test部门下所有部门元素并输出text值
        depart_list = self.finds(self._location_expand_depart)
        # is_displayed_res = [i.is_displayed() for i in depart_list]
        # print(is_displayed_res)
        depart_list_res = [i.text for i in depart_list]
        return depart_list_res
