from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time as time 


info = {'email':'guirox.wd@gmail.com','senha':'Lask1234','model':'ACG-Air-Deschutz','size':'42'}

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.nike.com.br/Snkrs#estoque')
def comprar(driver):
    return driver.find_elements_by_class_name('btn')
estoque = WebDriverWait(driver,120).until(comprar)
link_produto = [
    produto.get_attribute('href')
    for produto in estoque
    if ( produto.get_attribute("href") is not None and produto.get_attribute("href").find(('/{}/').format(info['model'])) != -1 )
]

def sizeOff(driver):
    return driver.find_elements_by_class_name('tamanho-desabilitado')

driver.get(link_produto[0])
size_off =  WebDriverWait(driver,120).until(sizeOff)
size_off = [size.text for size in size_off]
if info['size'] in size_off:
    print('desculpe mas nao temos mais exemplares neste tamanho')
else:
    def click_compra(driver):
        return driver.find_element_by_id('anchor-acessar')
    WebDriverWait(driver,120).until(click_compra).click()
    def capturar_form_login(driver):
        email_campo = driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div[5]/form/div[2]/input")
        senha_campo = driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div[5]/form/div[3]/input")
        return [email_campo , senha_campo ]
    [email , senha ] = WebDriverWait(driver,120).until(capturar_form_login)
    '''email.send_keys(info['email'])
    senha.send_keys(info['senha'])'''
    driver.execute_script("arguments[0].setAttribute('value','{}')".format(info['email']),email)
    driver.execute_script("arguments[0].setAttribute('value','{}')".format(info['senha']),senha)
    WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[8]/div/div/div[2]/div[5]/form/div[6]/input"))).click()
    print('logado')
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 400)")
    WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'{}')]".format(info['size'])))).click()
