# import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig
headless_option =webdriver.ChromeOptions()
headless_option.add_argument("headless")

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    def test_homepageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
