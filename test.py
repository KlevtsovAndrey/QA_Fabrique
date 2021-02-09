from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time


driver = webdriver.Chrome('./drivers/chromedriver.exe')


class Test_Fabrique:
    def test_setup(self):
        driver.get('https://finance.dev.fabrique.studio/accounts/login/')
        driver.maximize_window()
        driver.implicitly_wait(2)

    # Авторизация на сайте
    def test_login(self):
        driver.find_element(By.XPATH, "//form/div[1]/div/div/label").send_keys('admin@admin.ad')
        driver.find_element(By.XPATH, "//form/div[2]/div/div/label").send_keys('admin')
        driver.find_element(By.XPATH, "//button/div[3]").click()
        time.sleep(2)
        assert driver.title == 'Finance'

    # Создание нового юр. лица
    def test_add_new_organization(self):
        driver.find_element(By.XPATH, "//div[contains(text(), 'Юр. лица')]").click()
        driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить юридическое лицо')]").click()
        organization_name = 'ООО "Тест"'
        driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(1) > div > div > div > div > .form-field .input").click()
        driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys(organization_name)
        driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(2) > div > div > div > div > .form-field .input").click()
        driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys("тест")
        driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

    # Создание счёта
    class Test_Create_Account:
        def test_add_existing_account(self):
            # Для юр. лица существующего
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Счета')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить счёт')]").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Поставщик СБЕР')
            driver.find_element(By.XPATH, "//div[@class='multiselect__tags']/span").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect__input").send_keys('ООО "Тест"')
            driver.find_element(By.CSS_SELECTOR, ".multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div > div > div .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('1234 5678 9101 1121')
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Поставщик мебели')
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

        # Для юр. лица нового
        def test_add_new_account(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Счета')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить счёт')]").click()
            driver.find_element(By.CSS_SELECTOR,
                                "div:nth-child(1) > div > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Поставщик АЛЬФАБАНК')
            driver.find_element(By.XPATH, "//div[@class='multiselect__tags']/span").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect__input").send_keys('ООО "Новое юр. лицо"')
            driver.find_element(By.CSS_SELECTOR, ".multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div > div > div .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('4568 5678 9101 1121')
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Поставщик техники')
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

        # Создание одного счета для нескольких юр. лиц
        def test_add_multiple_accounts(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Счета')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить счёт')]").click()
            driver.find_element(By.CSS_SELECTOR,
                                "div:nth-child(1) > div > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Поставщики ПСБ')
            driver.find_element(By.XPATH, "//div[@class='multiselect__tags']/span").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect__input").send_keys('ООО "Тест"')
            driver.find_element(By.CSS_SELECTOR, ".multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[@class='multiselect__tags']").click()
            driver.find_element(By.XPATH, "//input[@class='multiselect__input']").send_keys('ООО "Новое юр. лицо"')
            driver.find_element(By.CSS_SELECTOR, ".multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div > div > div .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('4568 5678 9101 1121')
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Поставщики техники и мебели')
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

    # Создание статей расходов
    class Test_Create_Costs:
        # Создание обычной статьи расходов
        def test_add_regular_cost(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Статьи расходов')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить статью')]").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Мебель')
            driver.find_element(By.XPATH, "//textarea").send_keys('офисная')
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

        # Создание уменьшаемый план
        def test_add_planned_cost(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Статьи расходов')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить статью')]").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('ТЕСТ_Плановые долговые обязательства')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Уменьшаемый план')]").click()
            driver.find_element(By.XPATH, "//textarea").send_keys('МФУ')
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Статьи расходов')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить статью')]").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('ТЕСТ_Долговые обязательства')
            driver.find_element(By.XPATH, "//textarea").send_keys('офисная')
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

    # Создание новых платежей
    class Test_Add_New_Payment:
        # Создание платежа "Доход"
        def test_add_payment_income(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить платёж')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Доход/приход')]").click()
            driver.find_element(By.XPATH, "//textarea").send_keys('Продажа товаров')
            driver.find_element(By.CSS_SELECTOR, ".form-field:nth-child(1) > .form-field__field > .checkbox .icon").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('200')
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('200')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Оплачен')]").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > .form-field .date").click()
            driver.find_element(By.CSS_SELECTOR, ".dp-today").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > .form-field .date").click()
            driver.find_element(By.CSS_SELECTOR, ".dp-today").click()
            driver.find_element(By.XPATH, "//div/div[10]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Тестовый контрагент_1')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[11]/div/div[2]/div/div/div/div/div").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('textarea')
            driver.find_element(By.XPATH, "//div/div[12]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Счет выставлен')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[15]/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('ООО "Тест"')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[16]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Тестовый контрагент_1')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[17]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Поставщик СБЕР')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[18]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Поставщик АЛЬФАБАНК')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[19]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('test')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

        # Создание платежа "Расхода" с уменьшаемым планом (плановые долговые обязательства)
        def test_add_payment_planned_cost(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить платёж')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Расход')]").click()
            driver.find_element(By.XPATH, "//textarea").send_keys('Покупка мебели')
            driver.find_element(By.XPATH, "//div[13]/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('ТЕСТ_Плановые долговые обязательства')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.CSS_SELECTOR, ".form-field:nth-child(1) > .form-field__field > .checkbox .icon").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('10000')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Оплачен')]").click()
            driver.find_element(By.XPATH, "//div[14]/div/div[2]/div/div/div/div/div").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Оплата за технику')
            driver.find_element(By.XPATH, "//div[15]/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('ООО "Новое юр. лицо"')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[16]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Тестовый контрагент_2')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[19]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('test')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

        # Создание платежа "Расхода" с уменьшаемым планом (долговые обязательства)
        def test_add_payment_cost(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить платёж')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Расход')]").click()
            driver.find_element(By.XPATH, "//textarea").send_keys('Покупка мебели')
            driver.find_element(By.XPATH, "//div[13]/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('ТЕСТ_Долговые обязательства')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.CSS_SELECTOR, ".form-field:nth-child(1) > .form-field__field > .checkbox .icon").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('8000')
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('8000')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Оплачен')]").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > .form-field .date").click()
            driver.find_element(By.CSS_SELECTOR, ".dp-today").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > .form-field .date").click()
            driver.find_element(By.CSS_SELECTOR, ".dp-today").click()
            driver.find_element(By.XPATH, "//div[13]/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Оплата за мебель')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[14]/div/div[2]/div/div/div/div/div").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('Оплата за мебель')
            driver.find_element(By.XPATH, "//div[15]/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('ООО "Новое юр. лицо"')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[16]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Тестовый контрагент_2')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[17]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Поставщик АЛЬФАБАНК')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[18]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Поставщик ПСБ')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[19]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('test')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

        # Создание нового платежа "Перевод"
        def test_add_payment_transfer(self):
            driver.get('https://finance.dev.fabrique.studio/')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Добавить платёж')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(), 'Перевод средств')]").click()
            driver.find_element(By.XPATH, "//textarea").send_keys('Оплата труда')
            driver.find_element(By.CSS_SELECTOR, ".form-field:nth-child(1) > .form-field__field > .checkbox .icon").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > .form-field .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('80000')
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) .input").click()
            driver.find_element(By.CSS_SELECTOR, ".input--is-focused .input__input").send_keys('80000')
            driver.find_element(By.XPATH, "//div[contains(text(), 'Оплачен')]").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > .form-field .date").click()
            driver.find_element(By.CSS_SELECTOR, ".dp-today").click()
            driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > .form-field .date").click()
            driver.find_element(By.CSS_SELECTOR, ".dp-today").click()
            driver.find_element(By.XPATH, "//div[17]/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Поставщик СБЕР')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[18]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('Поставщик АЛЬФАБАНК')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[19]/div/div[2]/div/div/div/div/div/div/div[2]").click()
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys('test')
            driver.find_element(By.CSS_SELECTOR, ".multiselect--active .multiselect__input").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//button/div[contains(text(), 'Добавить')]").click()

    def test_teardown(self):
        driver.close()
        driver.quit()