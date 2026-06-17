#  Импортируем необходимые библиотеки и модули
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
time.sleep(1)

#  Проверка для случая, когда изначально слайдер стоит в крайнем левом (нулевом) положении, смещение на 1 шаг меняет отображаемое значение слайдера на 0.5 единиц

#  Найдём слайдер и запомним его отображаемое числовое значение
slider = driver.find_element(By.XPATH, "//input[@type='range']")
time.sleep(1)
initial_slider_value = driver.find_element(By.ID, "range").text

step_number = 0  #  Счётчик шагов проверки
print('_'*21,'\nStep\t|Expect\t|Fact',sep='')  #  Заголовок таблицы

#  Передвинем слайдер вправо 10 раз на 1 шаг и проконтролируем смещение
for i in range(10):
    slider.send_keys(Keys.ARROW_RIGHT)
    time.sleep(0.5)
    step_number += 1
    expected_shift = (0 + 0.5 * (i + 1))
    fact_position = driver.find_element(By.ID, "range").text
    fact_shift = float(fact_position) - float(initial_slider_value)
    print(step_number, '\t'*2, expected_shift, '\t', fact_shift)
    assert fact_shift == float(expected_shift), 'Смещение не соответствует ожидаемому'

#  Передвинем слайдер влево 10 раз на 1 шаг и проконтролируем смещение
for i in range(10):
    slider.send_keys(Keys.ARROW_LEFT)
    time.sleep(0.5)
    step_number += 1
    expected_shift = (5 - 0.5 * (i + 1))
    fact_position = driver.find_element(By.ID, "range").text
    fact_shift = float(fact_position) - float(initial_slider_value)
    print(step_number, '\t'*2, expected_shift, '\t', fact_shift)
    assert fact_shift == float(expected_shift), 'Смещение не соответствует ожидаемому'

time.sleep(1)
print('_'*20,'\nСмещения слайдера внутри диапазона перемещения корректны',sep='')

time.sleep(2)
driver.close()  #  Закрываем браузер