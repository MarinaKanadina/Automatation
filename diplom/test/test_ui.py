from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import allure
driver = webdriver.Chrome()
movie_name_locator = "span[data-tid='75209b22']"

@allure.title("Поиск фильма по герою")
@allure.description("Ввод в поисковую строку имени героя, вход на страницу с героем для выбора фильмов с ним")
@allure.severity("normal")
def test_hero():
  driver.get("https://www.kinopoisk.ru/")
  driver.find_element(By.NAME, "kp_query").send_keys("шрек")
  driver.find_element(By.ID, "suggest-item-film-430").click()
  assert driver.find_element(By.CSS_SELECTOR, movie_name_locator).text == "Шрек"


@allure.title("Поиск фильма по актеру")
@allure.description("Ввод в поисковую строку имени актера, вход на страницу с актером для выбора фильмов с ним")
@allure.severity("normal")
def test_actors(chrome):
  driver.get("https://www.kinopoisk.ru/")
  driver.find_element(By.NAME, "kp_query").send_keys("Джеки Чан")
  driver.find_element(By.ID, "suggest-item-person-29855").click()
  assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='f22e0093']").text == "Джеки Чан"
  
@allure.title("Поиск фильма по режиссеру")
@allure.description("Ввод в поисковую строку имени режиссера, вход на страницу с режиссером для выбора фильмов с ним")
@allure.severity("normal")
def test_director(chrome):
  driver.get("https://www.kinopoisk.ru/")
  driver.find_element(By.NAME, "kp_query").send_keys("Балабанов")
  driver.find_element(By.ID, "suggest-item-person-64249").click()
  assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='f22e0093']").text == "Балабанов"

@allure.title("Поиск фильма по певцу")
@allure.description("Ввод в поисковую строку имени певца, вход на страницу с певцом для выбора фильмов с ним")
@allure.severity("normal")
def test_singer(chrome):
  driver.get("https://www.kinopoisk.ru/")
  driver.find_element(By.CSS_SELECTOR, "kp_query").send_keys("Майкл Джексон")
  driver.find_element(By.ID, "suggest-item-person-39233").click()
  assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='f22e0093']").text == "Майкл Джексон"

@allure.title("Поиск фильма по городу")
@allure.description("Ввод в поисковую строку название города, вход на страницу с названием города для выбора фильмов с ним")
@allure.severity("normal")
def test_city(chrome):
  driver.get("https://www.kinopoisk.ru/")
  driver.find_element(By.CSS_SELECTOR, "kp_query").send_keys("Москва")
  driver.find_element(By.ID, "suggest-item-film-46708").click()
  assert chrome.find_element(By.CSS_SELECTOR, movie_name_locator).text == "Москва"
