#  Проверка для случая, когда изначально ползунок слайдер стоит в крайнем левом (нулевом) положении, смещение ползунка слайдера на 1 шаг соответствует изменению отображаемого значения слайдера на 0.5 единиц.

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

print('_'*13,'\nExpect\t|Fact',sep='')  #  Заголовок таблицы

#  Найдём слайдер
slider = driver.find_element(By.XPATH, "//input[@type='range']")

expected_position = 0  #  Зададим нулевое начальное ожидаемое положение ползунка слайдера

#  Передвинем ползунок слайдера вправо 10 раз на 1 шаг, потом влево 10 раз на 1 шаг с пошаговым контролем положения ползунка слайдера
for n in range(20):
    time.sleep(0.2)
    if n < 10:
        slider.send_keys(Keys.ARROW_RIGHT)
        expected_position += 0.5
    else:
        slider.send_keys(Keys.ARROW_LEFT)
        expected_position += - 0.5
    fact_position = driver.find_element(By.ID, "range").text
    print(expected_position, '\t', fact_position)
    assert float(fact_position) == expected_position, 'Смещение не соответствует ожидаемому'

time.sleep(1)
print('_'*13,'\nСмещения ползунка слайдера внутри диапазона перемещения корректны',sep='')

time.sleep(2)
driver.close()  #  Закрываем браузер