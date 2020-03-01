from selenium import webdriver
from time import sleep
from fb_secrets import username, password, link


class MessageBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(link)
        sleep(5)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        sleep(0.5)
        login_btn.click()

    def like(self):
        like = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/a')
        like.click()
        
    def auto_like(self):
        while True:
            sleep(2)
            # sleep(0.1)
            self.like()


bot = MessageBot()
bot.login()
bot.auto_like()







