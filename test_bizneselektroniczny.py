import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Order():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test(self):
    random.seed(None, 2)
    mail = "client" + str(random.randrange(0, 10000, 1)) + "@randommail.com"
    # Test name: Test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://efilmy.best/")
    # 2 | setWindowSize | 1032x728 | 
    self.driver.set_window_size(1032, 728)
    # 3 | click | css=#category-1000 > .dropdown-item | 
    self.driver.find_element(By.CSS_SELECTOR, "#category-1000 > .dropdown-item").click()
    # 4 | click | linkText=DVD | 
    self.driver.find_element(By.LINK_TEXT, "DVD").click()
    # 5 | click | css=.product-miniature:nth-child(1) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-miniature:nth-child(1) img").click()
    # 6 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 8 | click | linkText=DVD | 
    self.driver.find_element(By.LINK_TEXT, "DVD").click()
    # 9 | click | css=.product-miniature:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-miniature:nth-child(2) img").click()
    # 10 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 11 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 15 | click | css=li:nth-child(3) span |
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) span").click()
    # 16 | click | css=.product-miniature:nth-child(3) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-miniature:nth-child(3) img").click()
    # 17 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 19 | click | css=ol > li:nth-child(2) span | 
    self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(2) span").click()
    # 20 | click | linkText=Blu-Ray | 
    self.driver.find_element(By.LINK_TEXT, "Blu-Ray").click()
    # 21 | click | css=.product-miniature:nth-child(1) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-miniature:nth-child(1) img").click()
    # 22 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 23 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 27 | click | css=li:nth-child(3) span | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) span").click()
    # 28 | click | css=.product-miniature:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-miniature:nth-child(2) img").click()
    # 29 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 31 | click | css=li:nth-child(3) span | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) span").click()
    # 32 | click | css=.product-miniature:nth-child(3) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-miniature:nth-child(3) img").click()
    # 33 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 34 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 36 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 38 | click | css=.header .hidden-sm-down |
    self.driver.find_element(By.CSS_SELECTOR, ".header .hidden-sm-down").click()

    time.sleep(1)
    # 39 | click | css=.cart-item:nth-child(1) .col-md-2 .material-icons | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-item:nth-child(1) .col-md-2 .material-icons").click()

    time.sleep(1)
    # 40 | click | css=.logo | 
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 41 | click | css=.user-info .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, ".user-info .hidden-sm-down").click()
    # 42 | click | linkText=Nie masz konta? Załóż je tutaj | 
    self.driver.find_element(By.LINK_TEXT, "Nie masz konta? Załóż je tutaj").click()
    # 43 | click | name=id_gender | 
    self.driver.find_element(By.NAME, "id_gender").click()
    # 44 | click | name=firstname | 
    self.driver.find_element(By.NAME, "firstname").click()
    # 45 | type | name=firstname | imie
    self.driver.find_element(By.NAME, "firstname").send_keys("imie")
    # 46 | type | name=lastname | nazwisko
    self.driver.find_element(By.NAME, "lastname").send_keys("nazwisko")
    # 47 | type | name=email | imienaziwsko12@jakismail.pl
    self.driver.find_element(By.NAME, "email").send_keys(mail)
    # 48 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 49 | type | name=password | 12345
    self.driver.find_element(By.NAME, "password").send_keys("12345")

    time.sleep(2)
    # 52 | click | css=.form-control-submit | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-control-submit").click()
    # 53 | click | css=a:nth-child(1) > .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .hidden-sm-down").click()
    # 54 | click | css=.text-sm-center > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
    # 56 | type | name=address1 | ulica
    self.driver.find_element(By.NAME, "address1").send_keys("ulica")
    # 57 | type | name=postcode | 12-345
    self.driver.find_element(By.NAME, "postcode").send_keys("12-345")
    # 58 | type | name=city | miasto
    self.driver.find_element(By.NAME, "city").send_keys("miasto")

    time.sleep(2)
    # 59 | click | name=confirm-addresses | 
    self.driver.find_element(By.NAME, "confirm-addresses").click()
    # 60 | click | css=.row:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4)").click()
    # 61 | click | id=delivery_option_2 |
    self.driver.find_element(By.ID, "delivery_option_4")

    time.sleep(2)
    # 62 | click | name=confirmDeliveryOption | 
    self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
    # 63 | click | id=payment-option-2 |
    self.driver.find_element(By.ID, "payment-option-2").click()
    # 64 | click | id=conditions_to_approve[terms-and-conditions] | 
    self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()

    time.sleep(2)
    # 65 | click | css=.ps-shown-by-js > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
    # 66 | click | css=.account > .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
    # 67 | click | css=#history-link .material-icons | 
    self.driver.find_element(By.CSS_SELECTOR, "#history-link .material-icons").click()
    # 68 | click | linkText=Szczegóły | 
    self.driver.find_element(By.LINK_TEXT, "Szczegóły").click()

    time.sleep(3)

