from selenium import webdriver
from LoginClass import Nti
import time

def teste4():
	ff = webdriver.Firefox()
	d = Nti(ff)
	d.navigate()
	time.sleep(5)
	d.login('teste','teste')
	d.buttonClick()
	time.sleep(5)
	result = d.getChangeScreen()
	if result == False:
		print("Green")  #passou no teste
	else:
		print("Red")    #não passou no teste. Voltar pra arrumar :)

teste4()
