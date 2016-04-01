from unittest import  TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        self.browser.implicitly_wait(3)

        nombre = self.browser.find_element_by_id('nombre')
        nombre.send_keys('Jorge')

        apellidos = self.browser.find_element_by_id('apellidos')
        apellidos.send_keys('Runza')

        self.browser.find_element_by_xpath("//select[@id='idServicio']/option[text()='Plomeria']").click()

        aniosExperiencia = self.browser.find_element_by_id('aniosExperiencia')
        aniosExperiencia.send_keys('1')

        telefono = self.browser.find_element_by_id('telefono')
        telefono.send_keys('6718771')

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('jorger@gmail.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('calve123')

        foto = self.browser.find_element_by_id('foto')
        foto.send_keys('C:\Users\jd.runza\Desktop\lfxfr5W.jpg')

        botonGuardar = self.browser.find_element_by_id('id_grabar')
        botonGuardar.click()
        self.browser.implicitly_wait(3)
        p = self.browser.find_element(By.XPATH, "//p[text()='Jorge Runza']")

        self.assertIn('Jorge Runza', p.text)

    def test_view_detail(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(20)
        p = self.browser.find_element(By.XPATH, "//p[text()='Jorge Runza']")
        p.click()

        self.browser.implicitly_wait(5)
        nombre = self.browser.find_element_by_id('nombre')
        apellido = self.browser.find_element_by_id('apellido')

        self.assertIn('Jorge', nombre.text)
        self.assertIn('Runza', apellido.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(10)

        link = self.browser.find_element_by_id('pagLog')
        link.click()

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('jorger@gmail.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('calve123')

        botonLogin = self.browser.find_element_by_id('botLog')
        botonLogin.click()
        self.browser.implicitly_wait(3)
        p = self.browser.find_element(By.XPATH, "//p[text()='Jorge Runza']")