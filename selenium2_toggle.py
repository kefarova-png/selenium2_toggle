#  Импортируем необходимые библиотеки и модули
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#  Chrome. Создаём переменную для опций браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver. Chrome (
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

#  Открываем вебдрайвером ссылку
base_url = 'https://the-internet.herokuapp.com/horizontal_slider'
driver.get(base_url)
driver.set_window_size(920, 1080)
time.sleep(2)
print('_'*20)

#  Создаём экземпляр класса ActionChains для перемещения по окну браузера
actions = ActionChains(driver)

#  Найдём слайдер и найдём-запомним его значение
slider = driver.find_element(By.XPATH, "//input[@type='range']")
time.sleep(3)
slider_value_element = driver.find_element(By.ID, "range")
initial_slider_value = slider_value_element.text

#  Передвинем слайдер вправо на 50 пикселей
actions.click_and_hold(slider).move_by_offset(50,0).release().perform()
time.sleep(2)
print("Слайдер передвинут в сторону увеличения")

#  Проверим, что значение слайдера изменилось
final_slider_value = slider_value_element.text
delta = float(final_slider_value) - float(initial_slider_value)
assert delta > 0, 'Значение слайдера должно увеличиться.'
print(f"Значение слайдера увеличилось на {delta}")

time.sleep(3)
#  Закрываем браузер
driver.close()