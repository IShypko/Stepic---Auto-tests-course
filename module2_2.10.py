from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html") #Открыть страницу http://suninjuly.github.io/explicit_wait2.html

button = browser.find_element_by_css_selector("button.btn")
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    ) #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
button.click() #Нажать на кнопку "Book"

def calc(x):
    return str(math.log(abs (12 *math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value") 
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

submit = browser.find_element_by_id("solve").click()

time.sleep(9)
browser.quit()

