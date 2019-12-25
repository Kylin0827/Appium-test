from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'D:\com.ibox.calculators_3.0.5_1305.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
# desired_caps['unicodeKeyboard']  = True
# desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    ele = driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
    text1 =ele.text
    ele.click()
    ele2 = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
    if text1 ==ele2.text:
        print('标题一致')
    else:
        print('标题不一致')
    driver.press_keycode(4)
    ele3 = driver.find_element_by_id('io.manong.developerdaily:id/tab_bar_plus')
    if ele3:
        print('返回成功')
    else:
        print('返回失败')

except:
    print (traceback.format_exc())

input('**** Press to quit..')
driver.quit()
