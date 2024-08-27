from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(2)
    button.click()
    time.sleep(2)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    def calc(x):
        return str(math.log(abs(12* math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(2)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
