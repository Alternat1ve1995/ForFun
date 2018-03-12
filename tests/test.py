from selenium import webdriver
import subprocess

browser = webdriver.Chrome('...\chromedriver.exe')
browser.get('https://facebook.com')
browser.maximize_window()
browser.find_element_by_id('email').send_keys('')
browser.find_element_by_id('pass').send_keys('')
browser.find_element_by_css_selector('input[value*=\"Увійти\"]').click()
