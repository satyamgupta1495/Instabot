from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def login():
    chromedriver = "D:\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://instagram.com")
    driver.implicitly_wait(10)
    username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    username.send_keys("")
    password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("")

    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
    login.click()

    notnow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notnow.click()


    skip = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    skip.click()

    search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    search.send_keys("#poems")

    animeart = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div")
    animeart.click()

    likeandcomment(driver)


def likeandcomment(driver):
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[8]/div[3]/a/div").click()
    while True:
        time.sleep(2)
        post = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[8]/div[3]/a/div")
        actionChains1 = ActionChains(driver)
        actionChains1.double_click(post).perform()
        # select comment input
        driver.find_element_by_css_selector(".Ypffh").click()
        comment = driver.find_element_by_css_selector(".Ypffh")
        comment.send_keys("damnn..hahaha..... this is epic... ")
        time.sleep(1)
        comment.send_keys(Keys.ENTER)
        time.sleep(2)
        # next post
        driver.find_element_by_css_selector("._65Bje").click()


if __name__ == "__main__":
    login()
