import time
import os
from PIL import Image,ImageEnhance
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from application.main.chaojiying import Chaojiying_Client
from application.main import ali


class Bill(object):
    def __init__(self):
        self.url = "https://etax.hainan.chinatax.gov.cn/sword?ctrl=FPlxcxLnCtrl_initView"
        # option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options=option)
        # self.driver = webdriver.Firefox()
        # self.driver.set_window_size(1920, 1080)
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.wait = WebDriverWait(self.driver, 10)


    def get_image(self,bill_code,bill_num):
        self.driver.get(self.url)
        now_time = str(int(time.time()))
        create_dir("F:\\bill\\"+now_time+"\\")

        #     输入发票代码
        self.wait.until(EC.presence_of_all_elements_located((By.ID, "cxForm_fpdm")))
        input_bill_code = self.driver.find_element_by_id("cxForm_fpdm")
        input_bill_code.clear()
        input_bill_code.send_keys(bill_code)

        #  输入发票号码
        self.wait.until(EC.presence_of_all_elements_located((By.ID, "cxForm_fphm")))
        input_bill_num = self.driver.find_element_by_id("cxForm_fphm")
        input_bill_num.clear()
        input_bill_num.send_keys(bill_num)

        captcha = self.get_captcha("F:\\bill\\" + now_time + "\\")

        #     输入验证码
        self.wait.until(EC.presence_of_all_elements_located((By.ID, "cxForm_yzm")))
        input_captcha = self.driver.find_element_by_id("cxForm_yzm")
        input_captcha.clear()
        input_captcha.send_keys(captcha)

        time.sleep(5)

        button_search = self.driver.find_element_by_css_selector(".tb_mini_box .mini_tb")
        button_search.click()

        time.sleep(10)

        # 如果提示验证码错误

        result_path = "F:\\bill\\"+now_time+"\\result.png";
        self.driver.get_screenshot_as_file(result_path)  # 对整个网页截取保存

        self.driver.close()

        return result_path


    def get_captcha(self, path):
        print("请求验证码")
        time.sleep(1)
        text_captcha = auto_img(path, self.driver)
        chaojiying = Chaojiying_Client('chenhz', '123456789', '897482')
        im = open(text_captcha, 'rb').read()
        result = chaojiying.PostPic(im, 1902)
        print( "验证码："+ result['pic_str'])
        return result['pic_str']

    def get_result(self,path):
        bill_code, bill_num = ali.get(path)
        return self.get_image(bill_code, bill_num)


# 获取截取页面图片，保存至本地
def auto_img(path, driver):
    old_path = path+"old.png"
    new_path = path+"new.png"
    driver.get_screenshot_as_file(old_path)  # 对整个网页截取保存
    imgelement = driver.find_element_by_xpath('.//*[@id="picimg"]')  # 定位验证码
    # imgelement = driver.find_element_by_css_selector(".wrapper .swordfrom_div img")
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open(old_path)  # 打开截图
    i = i.convert('RGB')
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save(new_path)
    qq = Image.open(new_path)
    # 对图片，做了二值化处理，可以忽略
    imgry = qq.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save(new_path)
    return new_path




def create_dir(path):
    """
    :type path: str
    """
    if not os.path.exists(path):
        os.mkdir(path)

