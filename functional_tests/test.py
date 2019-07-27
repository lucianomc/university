from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


class Courses(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_homepage(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Universidade', self.browser.title)

        self.assertTrue(
            self.browser.find_element_by_tag_name('h1').text, 'Cursos')

        links = self.browser.find_elements_by_tag_name('a')

        self.assertTrue(['Novo Curso' for link in links])
        self.assertTrue(['Nova Matéria' for link in links])
        self.assertTrue(['Novo Estudante' for link in links])

        # self.fail('Finish the test!')

    def test_novo_curso(self):
        self.browser.get(self.live_server_url)

        novoCurso = self.browser.find_element_by_link_text('Novo Curso')

        novoCurso.click()

        self.assertTrue(
            self.browser.find_element_by_tag_name('h1').text, 'Novo Curso')

        inputName = self.browser.find_element_by_id('id_nameCourse')
        inputDesc = self.browser.find_element_by_id('id_descriptionCourse')

        inputName.send_keys('Psicologia')
        inputDesc.send_keys('Bla bla bla')

        inputButton = self.browser.find_element_by_tag_name('button')

        self.assertEqual(inputButton.text, 'Salvar')

        inputButton.click()

        self.assertTrue(
            self.browser.find_element_by_tag_name('h1').text, 'Cursos')
