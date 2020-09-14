from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains 
from time import time, sleep , mktime 
import schedule

options = Options()
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

'Dados do Login'
info = {}
try:
    manipulador = open('config.txt', 'r', encoding ='utf-8')
    for linha in manipulador:
        valor = linha[6::].strip()
        chave = linha[0:5].strip()
        info[chave] = valor
    manipulador.close()
except FileNotFoundError:
    print('O arquivo de configuração não foi encontrado.')
    input()
    

'Configuracao do Driver'
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
driver.get('https://www.nike.com.br')
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,'anchor-acessar'))).click()
driver.maximize_window()


'Formulario de Login'
def login_form(driver):
    email = driver.find_element_by_name("emailAddress")
    senha = driver.find_element_by_name("password")
    return [email ,senha]
[email , senha ] = WebDriverWait(driver,30).until(login_form)
sleep(0.7)


'Login Usuario'
driver.execute_script("arguments[0].setAttribute('value','{}')".format(info['email']),email)
driver.execute_script("arguments[0].setAttribute('value','{}')".format(info['senha']),senha)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[9]/div/div/div[2]/div[5]/form/div[4]/label"))).click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div[2]/div[5]/form/div[6]/input'))).click()
sleep(5.7)

def Buy(driver,info):
    time_start = time()
    'Redirecionamento para Pagina do Produto'
    driver.get('https://www.nike.com.br/Snkrs/Produto/{}'.format(info['model']))

    'Configuracao da Compra'
    driver.execute_script('window.scrollTo(0,300)')
    sleep(0.5)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'{}')]".format(info['sizeM'])))).click()
    sleep(0.1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div/div[1]/div[3]/div/div[2]/div[4]/div/div[2]/button[1]"))).click()

    'Confirmacao da Compra'
    ' Selecao de Frete WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div[4]/div/div[1]/div[1]/div[2]/div[2]/label"))).click()'

    'Usar frete Padrao e selecionar Endereco'
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div[4]/div/div[4]/a"))).click()
    sleep(0.5)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div/div[3]/div[4]/div[5]/button"))).click()
    sleep(1.2)

    'Tentativa de clicar nas Diferentes divs de Confirmar Endereco'
    try:
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[13]/div/div/div[3]/button[1]"))).click()
    except TimeoutException as exception:
        try:
            WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[15]/div/div/div[3]/button[1]"))).click()
        except TimeoutException as exception:
            WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[12]/div/div/div[3]/button[1]"))).click()
            try:
                WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div/div[3]/div[4]/div[5]/button"))).click()
            except TimeoutException as exception:
                try:
                    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[14]/div/div/div[3]/button[1]"))).click()
                except TimeoutException as exception:
                    print('Termine a Compra de forma Manual')
            
    driver.execute_script('window.scrollTo(0,200)')
    sleep(1)

    'Aceitar Politica de Trocas'
    'WebDriverWait(driver,5).until(EC.element_located_to_be_selected((By.ID,"politica-trocas"))).click()'
    'WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[13]/div/div/div[3]/button"))).click()'
    ActionChains(driver).move_to_element(driver.find_element_by_id('politica-trocas-label')).move_by_offset(137.3,0).click().perform()
    

    'Confirmar Pagamento'
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"confirmar-pagamento"))).click()
    time_stop = time()
    print('A compra foi feita em {}s'.format(time_stop - time_start))
    sleep(6)

    'Gerar comprovante da Compra'
    driver.save_screenshot('Comprovantes/{}_Comprovante.png'.format(info['model'].split('/')[0]))
    driver.quit()
    print('Sucesso , verifique a pasta Comprovantes.')
    c_ex = False
    

schedule.every().day.at("16:35").do(lambda: Buy(driver,info))
c_ex = True
try:
    while c_ex:
        schedule.run_pending()
        sleep(1)
except KeyboardInterrupt:
    print('Agradecemos...')
