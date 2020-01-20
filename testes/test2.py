from selenium import webdriver
from LoginClass import Nti
import time

def teste2():
	ff = webdriver.Firefox()
	d = Nti(ff)
	d.navigate()
	time.sleep(5)
	d.login('admin','admin')
	d.buttonClick()
	time.sleep(5)
	result = d.getChangeScreen()
	if result == True:
		print("Green")  #passou no teste
	else:
		print("Red")    #não passou no teste. Voltar pra arrumar :)

teste2()