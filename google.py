# coding=utf-8

# Импорт webdriver для создания объекта Chrome
from selenium import webdriver

# Импрот ChromeDriverManager для автоматической загрузки драйвера
from webdriver_manager.chrome import ChromeDriverManager

# Импорт Keys для константы Keys.RETURN
from selenium.webdriver.common.keys import Keys

# Загрузка драйвера, запуск
driver = webdriver.Chrome(ChromeDriverManager().install())

# Получение страницы Google
driver.get("https://www.google.by/")

# Поиск элемета по имени (<input name="q"></input>)
search_bar = driver.find_element_by_name('q')

# Отправка в строку поиска google (python + <Enter>)
search_bar.send_keys('python')
search_bar.send_keys(Keys.RETURN)

# Поиск выдачи результатов Google
h3s = driver.find_elements_by_xpath('//div[contains(@class,"g")]//a/h3')

# Распечатка найденых элеметов
for web_element in h3s:
    print web_element.text

# Завершение драйвера
driver.quit()
