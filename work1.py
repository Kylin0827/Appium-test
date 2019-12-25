from appium import webdriver
import time,traceback

a=1

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'D:\com.ibox.calculators_3.0.5_1305.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
# desired_caps['unicodeKeyboard']  = True
# desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    driver.find_element_by_id("com.ibox.calculators:id/digit3").click()
    driver.find_element_by_id("com.ibox.calculators:id/plus").click()
    driver.find_element_by_id("com.ibox.calculators:id/digit9").click()
    driver.find_element_by_id("com.ibox.calculators:id/equal").click()
    driver.find_element_by_id("com.ibox.calculators:id/mul").click()
    driver.find_element_by_id("com.ibox.calculators:id/digit5").click()
    driver.find_element_by_id("com.ibox.calculators:id/equal").click()
    res= driver.find_element_by_xpath("//*[@resource-id='com.ibox.calculators:id/cv']//android.widget.TextView[2]").text
    if res == '60':
        print('测试通过')
    else:
        print('测试不通过')
except:
    print (traceback.format_exc())

input('**** Press to quit..')
driver.quit()
