'''
Autor : Victor Gabryel da Silva Santos
Objetivo : Teste Prático NTI


Serão 2 testes:

Primeiro irá testar se o login com 
'''

from selenium import webdriver
import time

class Nti:

	def __init__(self, driver):
		self.driver = driver
		self.url = 'http://localhost:9292/simple-app'
		self.user = 'username'
		self.password = 'password'
		self.button = 'submit'

	def navigate(self):
		self.driver.get(self.url)

	def login(self, user, password):
		self.driver.find_element_by_id(self.user).send_keys(user)
		self.driver.find_element_by_id(self.password).send_keys(password)

	def buttonClick(self):
		self.driver.find_element_by_id(self.button).click()

	def errorCheck(self):
		items = self.driver.find_element_by_id('js_itemlist')

	def getChangeScreen(self):
		container = self.driver.current_url
		if container == 'http://localhost:9292/simple-app/login':
			print("Logado com sucesso!")
			return True
		else:
			print("Não logado!")
			return False


