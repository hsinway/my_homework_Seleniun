import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, base_driver=None):
        # 注解,不是赋值操作,用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument('lang=zh-CN.UTF-8')
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    # 私有函数,不可以被外部访问
    def __cookie_login(self):
        # 使用cookie登陆
        yaml_data = yaml.safe_load(open("../file/cookie.yaml", encoding="UTF-8"))
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    # 封装self.driver.find_element
    def find(self, by, value=None):
        if value is None:
            # 如果传入的数据是元组,则加*解包为两个元素,第一个作为find_element的by参数第二个作为find_element的value参数
            return self.driver.find_element(*by)
        else:
            # 如果传入的数据是正常
            return self.driver.find_element(by=by, value=value)

    # 封装self.driver.find_elements
    def finds(self, by, value=None):
        if value is None:
            # 如果传入的数据是元组,则加*解包为两个元素,第一个作为find_element的by参数第二个作为find_element的value参数
            return self.driver.find_elements(*by)
        else:
            # 如果传入的数据是正常
            return self.driver.find_elements(by=by, value=value)

    def wait_clickable(self, locator):
        """
        封装显示等待
        :return:
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        """
        退出二次封装
        :return:
        """
        self.driver.quit()


def test_get_cookie():
    option = webdriver.ChromeOptions()
    # 设置debug地址
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    print(cookies)
    yaml.dump(cookies, open('../file/cookie.yaml', 'w', encoding='UTF-8'))
    # with open('cookie.yaml','w',encoding='UTF-8') as f:
    #     yaml.dump(cookies,f)
