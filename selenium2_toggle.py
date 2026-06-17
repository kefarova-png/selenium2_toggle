#  Проверка для случая, когда изначально ползунок слайдер стоит в крайнем левом (нулевом) положении, смещение ползунка слайдера на 1 шаг соответствует изменению отображаемого значения слайдера на 0.5 единиц.

#  Импортируем необходимые библиотеки и модули
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


expected_shift = 0  #  Начальное ожидаемое смещение (нулевое)


def motion_control():  #  Функция сравнения ожидаемого и фактического смещения
    time.sleep(0.2)
    global expected_shift
    expected_shift = expected_shift + direction_sign  #  ожидаем, что смещение на 1 шаг меняет значение слайдера на ±0.5 единиц за шаг
    fact_position = driver.find_element(By.ID, "range").text  #  фактическое значение слайдера
    print(expected_shift, '\t', fact_position)
    assert float(fact_position) == expected_shift, 'Смещение не соответствует ожидаемому'


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

#  Передвинем слайдер вправо 10 раз на 1 шаг и проконтролируем смещение
direction_sign = 0.5  #  Параметр движения вправо, для изменения значения слайдера на 0.5 единиц/шаг
for _ in range(10):
    slider.send_keys(Keys.ARROW_RIGHT)
    motion_control()

#  Передвинем слайдер влево 10 раз на 1 шаг и проконтролируем смещение
direction_sign = -0.5  #  Параметр движения влево, для изменения значения слайдера на -0.5 единиц/шаг
for _ in range(10):
    slider.send_keys(Keys.ARROW_LEFT)
    motion_control()

time.sleep(1)
print('_'*13,'\nСмещения ползунка слайдера внутри диапазона перемещения корректны',sep='')

time.sleep(2)
driver.close()  #  Закрываем браузер