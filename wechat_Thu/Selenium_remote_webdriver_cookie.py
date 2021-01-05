from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    # def setup(self):
    #     # self.driver = webdriver.Chrome(executable_path='')  # 也可以填写绝对路径,但是绝对路径要写到可执行文件未见位置,例如.exe文件
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(5)
    #     self.driver.maximize_window()

    # remote复用已有的浏览器,每次运行不会打开新的浏览器,并且每次调试只会在当前的tab下
    # 开启方式:
    # 1.关闭所有Chrome页面和后台程序(可能需要重启电脑).
    # 2.右键Chrome快捷方式,查看Target内chrome.exe前的路径.例如C:\Program Files (x86)\Google\Chrome\Application
    # 3.1.打开命令行,cd到该路径下,执行chrome --remote-debugging-port=9222 命令
    # 3.2.或者将C:\Program Files (x86)\Google\Chrome\Application加入到环境变量的Path下,然后打开命令行直接输入上述命令
    # 4.若成功则会自动打开一个空的Chrome页面,输入http://127.0.0.1:9222/会看到插件等文字信息
    # 坑:如果使用remote复用浏览器,要把浏览器调成100%缩放,否则元素识别会出现错误
    def test_demo(self):
        option = webdriver.ChromeOptions()
        # 设置debug地址
        option.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=option)
        driver.get('https://work.weixin.qq.com/wework_admin/frame')
        driver.implicitly_wait(10)
        # driver.find_element(By.CSS_SELECTOR, '[id=menu_contacts]').click()
        driver.find_element_by_id('menu_contacts').click()
        print(driver.get_cookies())


# 使用cookie登陆
def test_cookie():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh-CN.UTF-8')
    driver = webdriver.Chrome(chrome_options=options)
    # 使用cookie前要先打开一次和cookie的domain一致的页面,
    # selenium的默认域名是data:,如果不先打开一次cookie相同域名的地址则会卡在空白的data:,
    driver.get('https://work.weixin.qq.com/')
    # 该cookie是上面打印出来的s
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
                'path': '/', 'secure': False, 'value': '1608217642'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
                'value': '1688851969834148'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639753641, 'httpOnly': False,
                                               'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                               'secure': False, 'value': '1608102758,1608217090,1608217642'},
               {'domain': '.qq.com', 'expiry': 1909383510, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
                'secure': False, 'value': '1_49445279'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                'value': 'UUg4uqgoKxZbU0aWdbXnjrTpRZ3k6ghsCbHLVLh9MPyCvIz7EVIzP1E7C1vdcj2ZXBxQzWtZjF7saZwfdL1D7xLFxIP1ZyS3ZkkTkzAARzSrko3GbIIvYfr25DeFJye-Ka9ORojXe4DZ2GlDHLL47r8hmBXVhBnHoh9NVzCExg98TTlMzDxsWrle3vSCATiGZxDspTrtAFb4L5H9HG7yBJQs1uiQMETkKj4n8jfcEyE0F3Z-GYxwFDtheWPMFnzYCUGCcLDLUPcpJCUWzBYGyA'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
                'value': '1688851969834148'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                'secure': False, 'value': '3528104912'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                'secure': False, 'value': '6619830272'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                'secure': False,
                'value': '1970325025206127'},
               {'domain': '.qq.com', 'expiry': 1608304584, 'httpOnly': False, 'name': '_gid', 'path': '/',
                'secure': False, 'value': 'GA1.2.1295589623.1608102758'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': 'c4Nd0qAByPQ5o_dd_VRF8vTZpgxVVPdbATzrBB24L1cTjQ3fEBpldnZUu22GlTYy'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                'value': 'a5496208'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
                'value': '31587247203452328'},
               {'domain': 'work.weixin.qq.com', 'expiry': 1608248589, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
                'secure': False, 'value': '7d3ivqm'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1610810297, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                'path': '/', 'secure': False, 'value': 'zh'},
               {'domain': '.qq.com', 'expiry': 1671290184, 'httpOnly': False, 'name': '_ga', 'path': '/',
                'secure': False, 'value': 'GA1.2.1295752398.1608102758'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1639638757, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                'path': '/', 'secure': False, 'value': '0'},
               {'domain': '.qq.com', 'expiry': 1609769445, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
                'secure': False, 'value': '49445279'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
                'secure': False, 'value': '49445279'},
               {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                'secure': False, 'value': 'a5816a3f209362e4a0b015791bbbcfe200c6d0506a5dd8371b87ba6e6dd4e9ff'},
               {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/',
                'secure': False,
                'value': 'uJ7kHQiMED'},
               {'domain': '.qq.com', 'expiry': 1907311303, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/',
                'secure': False, 'value': '0'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                'value': 'direct'}]
    # 将cookie传入webdriver
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, '[id=menu_contacts]').click()
    sleep(5)
    driver.quit()

# 通过remote复用浏览器获取已经登陆成功的页面cookie
def test_get_cookie():
    option = webdriver.ChromeOptions()
    # 设置debug地址
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    print(cookies)
    yaml.dump(cookies, open('../test_wechat/file/cookie.yaml', 'w', encoding='UTF-8'))
    # with open('cookie.yaml','w',encoding='UTF-8') as f:
    #     yaml.dump(cookies,f)


# 使用序列化的cookie登陆
def test_login():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh-CN.UTF-8')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get('https://work.weixin.qq.com/')
    # 读取cookie
    cookies_yaml = yaml.safe_load(open('cookie.yaml', encoding='UTF-8'))
    # print(cookies_yaml)
    for cookie in cookies_yaml:
        # print(f'开始 {cookie}')
        driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.find_element(By.CSS_SELECTOR, '[id=menu_contacts]').click()
    driver.find_element_by_link_text('添加成员').click()
    # driver.find_element(By.XPATH,'//*[@id="js_contacts47"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
    sleep(3)
    # driver.quit()


