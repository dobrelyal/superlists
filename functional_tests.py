from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    '''тест нового посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''подтверждение строки в таблице списка'''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        #Эдит слышала ро крутое новое приложение со списком
        #неотложных дел Она решает оценить его домашнюю страничку
        self.browser.get('http://localhost:8000')

        #Она видит что заголовок и шапка страницы говорит о списке неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Когда она нажимает enter страница обновляется и теперь она содержит
        #"1: Купить павлиньи перья" в качестве элемента таблицы списка
        #inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)
        #self.check_for_row_in_list_table('1: Купить павлиньи перья')

        #Текстовое поле по-прежнему приглашает ее добавить еще один елемент
        #Она вводит"Сделать мушку из павлиных перьев" (Эдит очень методична)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #Страница снова обновляется и теперь показывает оба елемента ее списка
        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

        #Эдит интересно запомнит ли сайт ее список Далее она видит что сайт
        #сгенирировал для нее уникальный URL-адрес
        #об этом выводится небольшой текст с пояснениями
        self.fail('Закончить тест')
        #Она посещает этот адрес и ее список по-прежнему там
if __name__ == '__main__':
    unittest.main(warnings='ignore')
