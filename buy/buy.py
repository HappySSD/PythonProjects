import time

from selenium import webdriver
import datetime
import logging

""""
抢购指定页面的商品
"""
# 本地chrome驱动路径
driver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

# 目标商品页面
target_url = "https://item.jd.com/6949475.html#crumb-wrap"
# 抢购时需要点击的按钮关键字
button_keyword = "立即抢购"
# 抢购页面停留时间
page_sleep_time = 100000

# 抢购时间
launch_time = "2018-05-18 0:00:00"
# 抢购时间格式
time_format = "%Y-%m-%d %H:%M:%S"


# 定时发起抢购
def main():
    sched_time = datetime.datetime.strptime(launch_time, time_format)
    logging.info("设定抢购时间为[{}]", sched_time)
    while True:
        now = datetime.datetime.now()
        if sched_time < now < (sched_time + datetime.timedelta(seconds=1)):
            open_browser()
            break
    time.sleep(page_sleep_time)


# 打开浏览器开始抢购
def open_browser():
    browser = webdriver.Chrome(driver_path)
    logging.info("抢购开始!")
    browser.get(target_url)
    browser.find_element_by_link_text(button_keyword).click()
    logging.info("抢购结束!")


if __name__ == '__main__':
    main()
