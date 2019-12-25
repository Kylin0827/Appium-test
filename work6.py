from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'D:\com.ibox.calculators_3.0.5_1305.apk'
desired_caps['appPackage'] = 'com.example.jcy.wvtest'
desired_caps['appActivity'] = 'com.example.jcy.wvtest.MainActivity'
# desired_caps['unicodeKeyboard']  = True
# desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
desired_caps['chromedriverExecutable'] = r'D:\test1\chromedriver.exe'
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    print(driver.contexts)
    driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')
    driver.find_element_by_id('index-kw').send_keys('松勤')
    driver.find_element_by_id('index-bn').click()
    driver.switch_to.context('NATIVE_APP')
    driver.find_element_by_id('com.example.jcy.wvtest:id/navigation_notifications').click()

except:
    print (traceback.format_exc())

input('**** Press to quit..')
driver.quit()
