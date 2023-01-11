import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='[путь до хромдрайвер]/chromedriver.exe')
base_url = ' https://b2c.passport.rt.ru/'
driver.implicitly_wait(10)


def test_clicks_by_tab():  # 1,2,3,4 test
    from config import data_for_tab_tests
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(0.5)
    for id, result in data_for_tab_tests:
        btn_tab = driver.find_element(By.ID, id)
        btn_tab.click()
        text = driver.find_element(By.XPATH, '//span[contains(@class, "rt-input__placeholder")]').text
        assert text == result
        time.sleep(1)


def test_automatic_tab_change():  # 5,6,7,8 test
    from config import data_for_automatic_change_tests
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(0.5)
    for id, data, result in data_for_automatic_change_tests:
        driver.find_element(By.ID, id).click()  # клик по табу выбора аутентификации
        input_field = driver.find_element(By.XPATH, '//*[@id="username"]')
        input_field.click()  # клик по полю ввода логина
        time.sleep(0.5)
        input_field.send_keys(data)  # ввод данных
        driver.find_element(By.XPATH, '//*[@id="password"]').click()  # клик по полю ввода пароля
        text = driver.find_element(By.XPATH, '//span[contains(@class, "rt-input__placeholder")]').text
        assert text == result
        time.sleep(1)


def test_pass_recovery_link():  # 9 test
    driver.get(base_url)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    result = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]').text
    assert result == "Восстановление пароля"


def test_button_whith_unfilled_fields():  # 10 test
    from config import data_button_whith_unfilled_fields
    driver.get(base_url)
    driver.maximize_window()
    for id, result in data_button_whith_unfilled_fields:
        driver.find_element(By.ID, id).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
        text = driver.find_element(By.XPATH,
                                   '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]').text
        assert text == result


def test_autorisation_with_valid_phone():  # 11 test
    from config import valid_user_phone, valid_user_password
    driver.get(base_url)
    driver.maximize_window()
    # переключим таб выбора на "телефон" т.к. с пердыдущего теста он остался на "лицевом счете"
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    input_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    input_field.click()  # клик по полю ввода логина
    input_field.send_keys(valid_user_phone)  # ввод данных
    input_pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    input_pass_field.click()  # клик по полю ввода пароля
    input_pass_field.send_keys(valid_user_password)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()  # клик по кнопке авторизация
    time.sleep(2)
    text = driver.find_element(By.XPATH, '//*[@id="lk-btn"]').text
    assert text == "Личный кабинет"
    time.sleep(0.5)
    driver.find_element(By.XPATH, '// *[ @ id = "logout-btn"]').click()


def test_autorisation_with_valid_email():  # 12 test
    from config import valid_user_email, valid_user_password
    driver.get(base_url)
    driver.maximize_window()
    input_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    input_field.click()  # клик по полю ввода логина
    time.sleep(0.5)
    input_field.send_keys(valid_user_email)  # ввод данных
    input_pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    input_pass_field.click()
    input_pass_field.send_keys(valid_user_password)
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(2)
    text = driver.find_element(By.XPATH, '//*[@id="lk-btn"]').text
    assert text == "Личный кабинет"
    time.sleep(0.5)
    driver.find_element(By.XPATH, '// *[ @ id = "logout-btn"]').click()


def test_pass_registration_link():  # 13 test
    driver.get(base_url)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    result = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]').text
    assert result == "Регистрация"


def test_autorisation_invalid_phone():  # 14 test
    from config import valid_user_password, invalid_email
    driver.get(base_url)
    driver.maximize_window()
    input_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    input_field.click()  # клик по полю ввода логина
    time.sleep(0.5)
    input_field.send_keys(invalid_email)  # ввод данных
    input_pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    input_pass_field.click()
    input_pass_field.send_keys(valid_user_password)
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(1)
    text = driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text
    assert text == "Неверный логин или пароль"


def test_autorisation_invalid_email():  # 15 test
    from config import valid_user_email, invalid_password
    driver.get(base_url)
    driver.maximize_window()
    input_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    input_field.click()  # клик по полю ввода логина
    time.sleep(0.5)
    input_field.send_keys(valid_user_email)  # ввод данных
    input_pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    input_pass_field.click()
    input_pass_field.send_keys(invalid_password)
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(1)
    text = driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text
    assert text == "Неверный логин или пароль"


def test_password_correct_input_check():  # 16, 17, 18, 19 test
    from config import password_correct_input_check
    driver.get(base_url)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(1)
    for data, result in password_correct_input_check:
        input_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        input_field.click()                 # клик по полю ввода пароля
        input_field.send_keys("\b" * 10)
        time.sleep(0.5)
        input_field.send_keys(data)         # ввод данных
        driver.find_element(By.XPATH, '//*[@id="password-confirm"]').click()  # клик по полю ввода подтверждения пароля
        text = driver.find_element(By.XPATH, '//form[1]/div[4]/div[1]/span[1]').text
        assert text == result

def test_password_confirm_correct_input_check():  # 20, 21, 22, 23 test
    from config import password_correct_input_check
    driver.get(base_url)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(1)
    for data, result in password_correct_input_check:
        input_field = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
        input_field.click()  # клик по полю ввода подтверждения пароля
        input_field.send_keys("\b" * 10) # очистка поля, .clear() не работает
        time.sleep(0.5)
        input_field.send_keys(data)  # ввод данных
        driver.find_element(By.XPATH, '//*[@id="password"]').click()  # клик по полю ввода пароля
        text = driver.find_element(By.XPATH, '//form[1]/div[4]/div[2]/span[1]').text
        assert text == result





