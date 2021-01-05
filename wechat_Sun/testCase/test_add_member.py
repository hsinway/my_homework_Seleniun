from time import sleep

import pytest

from wechat_Sun.pageObject.base_page import BasePage
from wechat_Sun.pageObject.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        self.main_page = MainPage()

    # 回复到首页还原一开始的状态
    def teardown(self):
        self.main_page.back_to_main()

    def teardown_class(self):
        self.main_page.quit()

    def test_add_member(self):
        """
        添加成员测试用例
        :return:
        """
        # 1.跳转到添加成员页面 2.添加成员 3.自动跳转到通讯录页面
        res = self.main_page.goto_add_member().add_member().get_member()
        assert "username" in res

    @pytest.mark.parametrize("accid, phone, expected", [("XinWei", "18662722301", '该帐号已被“辛慰”占有'),
                                                        ("xinwei1", "18662722307", '该手机号已被“辛慰”占有')])
    # 第一次参数化,传入重复的acctid,正确的手机号,断言信息18662722307
    # 第二次参数化,传入正确的acctid,重复的手机号,断言信息
    def test_add_member_fail(self, accid, phone, expected):
        """

        :param accid: 输入的account id
        :param phone: 输入的phone
        :param expected:
        :return:
        """
        # 1.跳转到添加成员页面 2.添加成员 3.自动跳转到通讯录页面
        res = self.main_page.goto_add_member().add_member_fail(accid, phone)
        assert expected in res

    def test_add_member_by_contact(self):
        """
        通过通讯录页面添加成
        :return:
        """
        self.main_page.goto_contact().goto_add_member().add_member()

    # 作业
    def test_add_department(self):
        """
        在通讯录页面添加部门
        :return:
        """
        res = self.main_page.goto_contact().add_department()
        assert "test_department_1" in res
