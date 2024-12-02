
### Following variables must be given. ############
login_pass = "Your login pass"
family_name = "family name"
given_name = "Given name"
ruby_familyname = "ruby of your family name"
ruby_givenname = "ruby of your given name"
birth_y = "Your birth year"
birth_m = "Your birth month" # e.g. September → 09 
birth_d = "Your birth date"  # e.g. 2nd → 02
age = "age"
email = "email"
grade = "Your grade" # 4年生　→ 4年

###################################################

if __name__ == "__main__":
    import time
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    
    url = "https://www.abilityfuse.co.jp/ask/teacher/change/index.html"

    browser = webdriver.Chrome()  #Mac
    browser.implicitly_wait(3)
    browser.get(url)
    time.sleep(2)
    print("ログインしました")

    elem1 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[2]/td/input[1]')
    elem1.click()

    elem2 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[3]/td/input')
    elem2.clear()
    elem2.send_keys(login_pass)

    elem3 = browser.find_element(By.XPATH,'//*[@id="姓-氏名"]')
    elem3.clear()
    elem3.send_keys(family_name)

    elem4 = browser.find_element(By.XPATH,'//*[@id="名-氏名"]')
    elem4.clear()
    elem4.send_keys(given_name)

    elem5 = browser.find_element(By.XPATH,'//*[@id="姓-ふりがな"]')
    elem5.clear()
    elem5.send_keys(ruby_familyname)

    elem6 = browser.find_element(By.XPATH,'//*[@id="名-ふりがな"]')
    elem6.clear()
    elem6.send_keys(ruby_givenname)

    elem7 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[5]/td/input[1]')
    elem7.click()

    elem8 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[6]/td/select[1]')
    elem8.send_keys(birth_y)

    elem9 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[6]/td/select[2]')
    elem9.send_keys(birth_m)


    elem10 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[6]/td/select[3]')
    elem10.send_keys(birth_d)

    elem11 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[6]/td/select[4]')
    elem11.send_keys(age)

    elem12 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[7]/td/input')
    elem12.clear()
    elem12.send_keys(email)

    elem13 = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[8]/td/select')
    elem13.send_keys(grade)

    send = browser.find_element(By.XPATH,\
    '//*[@id="t_Change"]/form/table/tbody/tr[51]/th/div/input')
    browser.execute_script("arguments[0].click();", send)

    send = browser.find_element(By.XPATH,\
    '//*[@id="form_change"]/form/table/tbody/tr[47]/th/div/input')
    browser.execute_script("arguments[0].click();", send)

    browser.close()
    print("ASKONEの登録情報を更新しました")

