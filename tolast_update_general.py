if __name__ == "__main__":
    import time
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By

### Following variables must be given. ####

    login_pass = "Your login pass."
    email = "Your email address" 
    birth_y = "Your birth year"
    birth_m = "Your birth month"
    birth_d = "Your birth date"

############################################
    
    url = "http://www.ansin-teacher.net/"
    browser = webdriver.Chrome()  #Mac
    browser.implicitly_wait(3)
    url = "http://www.ansin-teacher.net/tutor/edit1.html"
    browser.get(url)
    time.sleep(2)

    elem = browser.find_element(By.XPATH,"//*[@id=\"form\"]/table/tbody/tr[3]/td[2]/input")
    elem.clear()
    elem.send_keys(login_pass)

    elem = browser.find_element(By.XPATH,'//*[@id="form"]/table/tbody/tr[4]/td[2]/input')
    elem.clear()
    elem.send_keys(email)

    elem = browser.find_element(By.XPATH,'//*[@id="form"]/table/tbody/tr[5]/td[2]/select[1]')
    elem.send_keys(birth_y)

    elem = browser.find_element(By.XPATH,'//*[@id="form"]/table/tbody/tr[5]/td[2]/select[2]')
    elem.send_keys(birth_m)

    elem = browser.find_element(By.XPATH,'//*[@id="form"]/table/tbody/tr[5]/td[2]/select[3]')
    elem.send_keys(birth_d)

    browser.execute_script("window.scrollTo(0, 500);")
    time.sleep(1)

    elem = browser.find_element(By.XPATH,'//*[@id="form"]/table/tbody/tr[6]/td[2]/span/input')
    browser.execute_script("arguments[0].click();", elem)  #　画面範囲外の要素をクリックする方法！
    time.sleep(1)

    elem = browser.find_element(By.XPATH,'//*[@id="accordion"]/form/table/tbody/tr[60]/td[2]/div/span/input')
    browser.execute_script("arguments[0].click();", elem)
    time.sleep(1)

    elem = browser.find_element(By.XPATH,'//*[@id="article"]/form/div/table[2]/tbody/tr/td/div/span/input')
    browser.execute_script("arguments[0].click();", elem)
    time.sleep(1)
    print(datetime.datetime.now().strftime('%Y/%m/%d/%H:%M:%S'))

    browser.close()
