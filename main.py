from selenium import webdriver
from PIL import Image
import time, smtplib, selenium
#import os, sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import ddddocr
from selenium.webdriver.support.ui import Select
la = ['2616220080','2616220061']
lc = ['Fjsy@150232','Fjsy@202016']
for i in range(0,2):
        options = Options()
        options.add_argument('-headless')
# 打开chrome浏览器
        driver = webdriver.Chrome()
# 进入健康情况填报官网
        url = r'https://xg.fjsdxy.com/SPCP/Web'
        driver.get(url)
# 最大化窗口
        driver.maximize_window()
    # 登录信息
        username = driver.find_element(By.XPATH,'//*[@id="StudentId"]')
        stu_number = la[i]
        username.send_keys(stu_number)
        while True:
            try:
                driver.find_element(By.XPATH,'//*[@id="platfrom1"]/a/img')  # 尝试获取填体温页面 成功即登录成功
                break
            except:
                namess = driver.find_element(By.XPATH, '//*[@id="codeInput"]')
                namess.clear()
                stu_password = lc[i]
                password = driver.find_element(By.XPATH, '//*[@id="Name"]')
                password.send_keys(stu_password)
                driver.save_screenshot("2.png")#获取页面截图
                img = Image.open('2.png') ## 打开2.png文件，并赋值给img
                region = img.crop((1091,343,1173,366))#对获取的截图进行裁剪
                region.save('3.png')#保存裁剪后的图片
                ocr = ddddocr.DdddOcr()#导入验证码识别
                with open("3.png", "rb") as f:
                    img_bytes = f.read()
                res = ocr.classification(img_bytes)#将识别出来的验证码赋给res
                print(res)
                name = driver.find_element(By.XPATH,'//*[@id="codeInput"]')
                number = res
                name.send_keys(number)
                driver.find_element(By.XPATH, '//*[@id="Submit"]').click()
                try:
                    driver.find_element(By.XPATH, '//*[@id="layui-m-layer0"]/div[2]/div/div/div[2]/span').click()
                except:
                    break
        driver.find_element(By.XPATH,'//*[@id="platfrom2"]').click()# 选择信息采集表
        while True:
            try:
                while True:
                    try:
                        las = driver.find_element(By.XPATH,'//*[@id="platfrom1"]')
                        break
                    except:
                        namesss = driver.find_element(By.XPATH, '//*[@id="codeInput"]')
                        namesss.clear()
                        s1 = Select(driver.find_element(By.XPATH, '//*[@id="form1"]/div[1]/div[3]/div[2]/div[2]/select[3]'))
                        time.sleep(6)
                        s1.select_by_value('350481')
                        js1 = "window.scrollTo(0, document.body.scrollHeight)"
                        driver.execute_script(js1)
                        time.sleep(1)
                        driver.save_screenshot("2.png")#获取页面截图
                        img = Image.open('2.png') ## 打开2.png文件，并赋值给img
                        region = img.crop((1190,671,1296,711))#对获取的截图进行裁剪
                        region.save('3.png')#保存裁剪后的图片
                        ocr = ddddocr.DdddOcr()#导入验证码识别
                        with open("3.png", "rb") as f:
                            img_bytes = f.read()
                        res = ocr.classification(img_bytes)#将识别出来的验证码赋给res
                        print(res)
                        name = driver.find_element(By.XPATH,'//*[@id="codeInput"]')
                        number = res
                        name.send_keys(number)
                        driver.find_element(By.XPATH, '// *[ @ id = "ckCLS"]').click()
                        driver.find_element(By.XPATH, '//*[@id="SaveBtnDiv"]/button').click()
                        try:
                            driver.find_element(By.XPATH, '//*[@id="layui-m-layer0"]/div[2]/div/div/div[2]/span').click()
                        except:
                            break
            except:
                print('已填报完成')
                driver.find_element(By.XPATH, '// *[ @ id = "layui-m-layer0"] / div[2] / div / div / div[2] / span').click()
                break
        while True:
            try:
                driver.find_element(By.XPATH, '//*[@id="platfrom1"]').click()
                s1 = Select(driver.find_element(By.XPATH, '//*[@id="Temper1"]'))
                s2 = Select(driver.find_element(By.XPATH, '//*[@id="Temper2"]'))
                s1.select_by_value('36')
                s2.select_by_value('5')
                while True:
                    try:
                        las = driver.find_element(By.XPATH,'//*[@id="platfrom1"]/a/img')
                        break
                    except:
                        namesss = driver.find_element(By.XPATH, '//*[@id="codeInput"]')
                        namesss.clear()
                        driver.save_screenshot("D:\d12\pythonProject1/2.png")#获取页面截图
                        img = Image.open('D:\d12\pythonProject1/2.png') ## 打开2.png文件，并赋值给img
                        region = img.crop((1071,441,1148,471))#对获取的截图进行裁剪
                        region.save('D:\d12\pythonProject1/3.png')#保存裁剪后的图片
                        ocr = ddddocr.DdddOcr()#导入验证码识别
                        with open("3.png", "rb") as f:
                            img_bytes = f.read()
                        res = ocr.classification(img_bytes)#将识别出来的验证码赋给res
                        print(res)
                        name = driver.find_element(By.XPATH,'//*[@id="codeInput"]')
                        number = res
                        name.send_keys(number)
                        driver.find_element(By.XPATH, '//*[@id="SaveBtnDiv"]/div/button').click()
                        try:
                            driver.find_element(By.XPATH, '//*[@id="layui-m-layer0"]/div[2]/div/div/div[2]/span').click()
                        except:
                            break
            except:
                print('已填报完成')
                driver.find_element(By.XPATH, '// *[ @ id = "layui-m-layer0"] / div[2] / div / div / div[2] / span').click()
                break
        driver.quit()

















