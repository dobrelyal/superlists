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

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        #Эдит слышала ро крутое новое приложение со списком
        #неотложных дел Она решает оценить его домашнюю страничку
        self.browser.get('http://localhost:8000')

        #Она видит что заголовок и шапка страницы говорит о списке неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #Текстовое поле по-прежнему приглашает ее добавить еще один елемент
        #Она вводит"Сделать мушку из павлиных перьев" (Эдит очень методична)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #Страница снова обновляется и теперь показывает оба елемента ее списка
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        self.assertIn(
            '2: Сделать мушку из павлиньих перьев',
            [row.text for row in rows]
        )

        #Эдит интересно запомнит ли сайт ее список Далее она видит что сайт
        #сгенирировал для нее уникальный URL-адрес
        #об этом выводится небольшой текст с пояснениями
        self.fail('Закончить тест')
        #Она посещает этот адрес и ее список по-прежнему там 
if __name__ == '__main__':
    unittest.main(warnings='ignore')
