import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import numpy as np


# ToLastの"家庭教師求人募集掲示板"にある時給3500円以上の案件で性別指定などの条件を満たすもの全てに自動応募するプログラム(ただし最大20件までとした)
# 過去に一度、自動応募したことがある案件には二度と応募は送らないこととし、次回以降の実行の際は、応募したことがない案件からスタートするものとする。
# 自動応募したことがない案件からスタートするために、過去に応募した案件の求人番号をcsvファイルに記録しておき、実行開始時にそのファイルを参照することで、未応募の案件から始めて自動応募をする。
# 応募した案件は"求人情報画面"をスクショしておく。
#　　応募確認メールが届くのでそれは手入力する。適宜、求人情報のスクショを参照しながら応募するかを決めること。
# 求人情報の"ご家庭からの質問"の欄が空欄でない案件に対してはブラウザのタブを閉じずに応募申し込み画面直前で止まっておく、質問への回答を手入力して応募すれば良い。

email = "Your email address"
phone_nem = "Your phone number"
txt = "Your introduction"
path = "logfile.csv"
gender = "Your gender"


    
url = "http://www.ansin-teacher.net/offer/active.html"
screenshot_path = "/Users/mnmgchjsk/Downloads/ScreenShot"

if __name__ == "__main__":
    
    if gender == "man":
        gender_cond = "かならず女性"
    elif gender == "woman":
        gender_cond = "かならず男性"
    else:
        gender_cond = "---"
    
    browser = webdriver.Chrome()
    browser.implicitly_wait(0.1)

    browser.get(url)
    time.sleep(0.1)
    original_window = browser.current_window_handle

    info = browser.find_elements(By.CLASS_NAME, "td-result5")

    num = []
    for i in np.arange(0, len(info), 6):
        num.append(int(info[i].text[3:]))

    price = []
    for i in np.arange(1, len(info), 6):
        tmp = info[i].text
        tmp = int(tmp[1:-1])
        price.append(tmp)

    log = pd.read_csv(path)

    obj = []
    for i in range(len(price)):
        tmp = []
        if price[i] >= 3500 and num[i] > max(list(log["job_number"])):
            tmp.append(i)
            tmp.append(num[i])
            tmp.append(price[i])
            obj.append(tmp)

    app_ls = []
    for i in range(min(len(obj),20)):
        browser.switch_to.window(original_window)
        browser.switch_to.new_window('tab')
        browser.get(url)
        time.sleep(0.1)

        btn = browser.find_elements(By.CLASS_NAME, "filter")
        browser.execute_script("arguments[0].click();", btn[obj[i][0]])

        class_way = browser.find_element(By.XPATH,'//*[@id="article"]/table/tbody/tr[5]/td[2]')
        gender = browser.find_element(By.XPATH,'//*[@id="article"]/table/tbody/tr[6]/td[2]')
        if class_way.text == "かならず対面" or gender.text == gender_cond:
            browser.close()
            continue

        app_num = browser.find_element(By.XPATH, '//*[@id="article"]/table/tbody/tr[1]/td[2]')
        print(int(app_num.text))
        if int(app_num.text) in list(log["job_number"]):
            browser.close()
            continue

        browser.execute_script("window.scrollTo(0, 660);")
        time.sleep(0.1)

        question = browser.find_element(By.XPATH, '//*[@id="article"]/table/tbody/tr[14]/td[2]')
        if question.text == "とくになし":
            T = datetime.datetime.now()

            browser.save_screenshot(f"{screenshot_path}/apply_{int(app_num.text)}_{T.hour}{T.minute}.png")
            app_ls.append([T, app_num.text])

            app_btn = browser.find_element(By.XPATH, '//*[@id="article"]/div[3]/form/span/input')
            browser.execute_script("arguments[0].click();", app_btn)
            time.sleep(0.1)

            address = browser.find_element(By.XPATH, '//*[@id="article"]/form/table/tbody/tr[2]/td[2]/input')
            address.clear()
            address.send_keys(email)

            last_name = browser.find_element(By.XPATH, '//*[@id="article"]/form/table/tbody/tr[3]/td[2]/input[1]')
            last_name.clear()
            last_name.send_keys(family_name)

            first_name = browser.find_element(By.XPATH, '//*[@id="article"]/form/table/tbody/tr[3]/td[2]/input[2]')
            first_name.clear()
            first_name.send_keys(given_name)


            message = browser.find_element(By.XPATH, '//*[@id="article"]/form/table/tbody/tr[5]/td[2]/textarea')
            message.send_keys(txt)

            phon = browser.find_element(By.XPATH, '//*[@id="article"]/form/table/tbody/tr[6]/td[2]/input')
            phon.clear()
            phon.send_keys(phone_num)

            check1 = browser.find_element(By.XPATH, '//*[@id="article"]/form/table/tbody/tr[7]/td[2]/input[1]')
            browser.execute_script("arguments[0].click();", check1)

            check2 = browser.find_element(By.XPATH, '//*[@id="article"]/form/table/tbody/tr[7]/td[2]/input[2]')
            browser.execute_script("arguments[0].click();", check2)

            comfirm = browser.find_element(By.XPATH, '//*[@id="article"]/form/div/span/input')
            browser.execute_script("arguments[0].click();", comfirm)

            time.sleep(0.1)

            send = browser.find_element(By.XPATH, '//*[@id="article"]/form/div/span/input')
            browser.execute_script("arguments[0].click();", send)

            print("Application completed.")

            browser.close()

    app_ls = pd.DataFrame(app_ls, columns=["timestamp","job_number"])
    app_ls.to_csv(path, mode='a', header=False)
    browser.switch_to.window(original_window)
    browser.close()
